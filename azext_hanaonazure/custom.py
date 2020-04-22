# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=no-self-use,too-many-lines

import re
from azext_hanaonazure.modules_sdk.v2020_02_07_preview import models
from msrestazure.azure_exceptions import CloudError

keyvault_id_format = '/subscriptions/([\w\d-]+)/resourceGroups/([\w\d-]+)/providers/Microsoft.KeyVault/vaults/([\w\d-]+)'
msi_id_format = '/subscriptions/([\w\d-]+)/resourcegroups/([\w\d-]+)/providers/Microsoft.ManagedIdentity/userAssignedIdentities/([\w\d-]+)'
arm_resource_id_format = '/subscriptions/{}/resourceGroups/{}/providers/Microsoft.HanaOnAzure/sapMonitors/{}'
loganalytics_arm_id_format = '/subscriptions/([\w\d-]+)/resourceGroups/([\w\d-]+)/providers/Microsoft.OperationalInsights/workspaces/([\w\d-]+)'

def create_hanainstance(client, location, resource_group_name, instance_name, partner_node_id, ssh_public_key, os_computer_name, ip_address):
    try:
        from .modules_sdk.v2017_11_03_preview.models_py3 import OSProfile
        from .modules_sdk.v2017_11_03_preview.models_py3 import IpAddress
        from .modules_sdk.v2017_11_03_preview.models_py3 import NetworkProfile
        from .modules_sdk.v2017_11_03_preview.models_py3 import HanaInstance
    except (SyntaxError, ImportError):
        from .modules_sdk.v2017_11_03_preview.models import OSProfile
        from .modules_sdk.v2017_11_03_preview.models import IpAddress
        from .modules_sdk.v2017_11_03_preview.models import NetworkProfile
        from .modules_sdk.v2017_11_03_preview.models import HanaInstance

    hana_instance_to_create = HanaInstance(location=location,
                                           hardware_profile=None,
                                           storage_profile=None,
                                           os_profile=OSProfile(computer_name=os_computer_name,
                                                                ssh_public_key=ssh_public_key),
                                           network_profile=NetworkProfile(network_interfaces=[IpAddress(ip_address=ip_address)]),
                                           partner_node_id=partner_node_id)

    return client.create(resource_group_name, instance_name, hana_instance_to_create)


def show_hanainstance(client, resource_group_name, instance_name):
    return client.get(resource_group_name, instance_name)


def list_hanainstance(client, resource_group_name=None):
    if resource_group_name is None:
        return client.list()
    return client.list_by_resource_group(resource_group_name)


def restart_hanainstance(client, resource_group_name, instance_name):
    # The restart hanainstance REST API is a POST with no body.
    # The HANA RP API requires the Content-Type to be set.
    # Swagger does not add the Content-Type in the header if there is no body.
    # We need to add a custom header to force the API call to add the Content-Type.
    custom_header = {'Content-Type': 'application/json; charset=utf-8'}
    return client.restart(resource_group_name, instance_name, custom_header)

def start_hanainstance(client, resource_group_name, instance_name):
    # The start hanainstance REST API is a POST with no body.
    # The HANA RP API requires the Content-Type to be set.
    # Swagger does not add the Content-Type in the header if there is no body.
    # We need to add a custom header to force the API call to add the Content-Type.
    custom_header = {'Content-Type': 'application/json; charset=utf-8'}
    return client.start(resource_group_name, instance_name, custom_header)


def shutdown_hanainstance(client, resource_group_name, instance_name):
    # The shutdown hanainstance REST API is a POST with no body.
    # The HANA RP API requires the Content-Type to be set.
    # Swagger does not add the Content-Type in the header if there is no body.
    # We need to add a custom header to force the API call to add the Content-Type.
    custom_header = {'Content-Type': 'application/json; charset=utf-8'}
    return client.shutdown(resource_group_name, instance_name, custom_header)

def update_hanainstance(client, resource_group_name, instance_name, **kwargs):
    return client.update(resource_group_name, instance_name, kwargs['parameters'].tags)


def delete_hanainstance(client, resource_group_name, instance_name):
    return client.delete(resource_group_name, instance_name)

def list_sapmonitor(client):
    return client.list()

def show_sapmonitor(cmd, client, resource_group_name, monitor_name):
    # Try using new API version
    try:
        return client.get(resource_group_name, monitor_name)
    except (models.ErrorResponseException, CloudError) as error:
        print('{0} Attempting old API version'.format(error))

    # Use old version
    from azext_hanaonazure._client_factory import cf_sapmonitor_groups_v2017_11_03_preview
    sapmonitor_client_v2017_11_03_preview = cf_sapmonitor_groups_v2017_11_03_preview(cmd.cli_ctx)
    return sapmonitor_client_v2017_11_03_preview.get(resource_group_name, monitor_name)

def create_sapmonitor(
        cmd,
        client,
        resource_group_name,
        monitor_name,
        region,
        hana_subnet,
        hana_hostname=None,
        hana_db_sql_port=None,
        hana_db_username=None,
        hana_db_name=None,
        hana_db_password=None,
        hana_db_password_key_vault_url=None,
        key_vault_id=None,
        disable_customer_analytics=False,
        log_analytics_workspace_arm_id=None):

    monitoring_details = {}

    # Retrieve the log analytics workspace ID and shared key
    if log_analytics_workspace_arm_id is not None:
        # Log analytics workspace arm ID has been provided
        from ._client_factory import _loganalytics_client_factory

        # Extract Log analytics workspace information
        match = re.search(loganalytics_arm_id_format, log_analytics_workspace_arm_id)
        if not match:
            raise ValueError("Log Analytics workspace ARM ID is of incorrect format. The format starts with /subscriptions")

        loganalytics_subscription_id = match.group(1)
        loganalytics_resource_group = match.group(2)
        loganalytics_resource_name = match.group(3)
        workspaceClient = _loganalytics_client_factory(cmd.cli_ctx,loganalytics_subscription_id)
        workspaceObj = workspaceClient.workspaces.get(loganalytics_resource_group, loganalytics_resource_name)
        workspaceSharedkey = workspaceClient.workspaces.get_shared_keys(loganalytics_resource_group, loganalytics_resource_name)

        monitoring_details.update({
            "logAnalyticsWorkspaceArmId": log_analytics_workspace_arm_id,
            "logAnalyticsWorkspaceId": workspaceObj.customer_id,
            "logAnalyticsWorkspaceSharedKey": workspaceSharedkey.primary_shared_key
        })

    monitoring_details.update({
        "location": region,
        "monitorSubnet": hana_subnet,
        "enableCustomerAnalytics": not disable_customer_analytics
    })

    # Try creating using new API version
    try:
        return client.create(resource_group_name, monitor_name, monitoring_details)
    except (models.ErrorResponseException, CloudError) as error:
        print('{0} Attempting old API version'.format(error))

    # Use old version
    monitoring_details.update({
        "hanaSubnet": hana_subnet,
        "hanaHostname": hana_hostname,
        "hanaDbName": hana_db_name,
        "hanaDbSqlPort": hana_db_sql_port,
        "hanaDbUsername": hana_db_username
    })

    if hana_db_password is not None:
        # Password was passed in
        monitoring_details.update({"hanaDbPassword": hana_db_password})
    elif hana_db_password_key_vault_url is not None and key_vault_id is not None:
        # Keyvault URL was passed in
        from ._client_factory import (_msi_client_factory, _keyvault_client_factory)
        from azure.mgmt.keyvault.v2018_02_14.models import (VaultAccessPolicyProperties, AccessPolicyEntry, Permissions, SecretPermissions)

        # Create MSI
        msi_client = _msi_client_factory(cmd.cli_ctx)
        csi_name = get_csi_name(msi_client.config.subscription_id, resource_group_name, monitor_name)
        csi = msi_client.user_assigned_identities.create_or_update(resource_group_name, csi_name, region)

        # Extract Key Vault information
        match = re.search(keyvault_id_format, key_vault_id)
        if not match:
            raise ValueError("key_vault_id is of incorrect format. The ID should start with /subscriptions/")

        kv_subscription_id = match.group(1)
        kv_resource_group = match.group(2)
        kv_resource_name = match.group(3)
        kv_client = _keyvault_client_factory(cmd.cli_ctx, kv_subscription_id)

        # Get Key Vault Tenant ID
        kv = kv_client.vaults.get(kv_resource_group, kv_resource_name)

        # Add MSI to Key Vault
        secret_permissions = [SecretPermissions("get")]
        access_policy_entries = [AccessPolicyEntry(tenant_id=kv.properties.tenant_id, object_id=csi.principal_id, permissions=Permissions(secrets=secret_permissions))]
        properties = VaultAccessPolicyProperties(access_policies=access_policy_entries)
        kv_client.vaults.update_access_policy(kv_resource_group,kv_resource_name, 'add', properties)
        monitoring_details.update({
            "hanaDbPasswordKeyVaultUrl": hana_db_password_key_vault_url,
            "hanaDbCredentialsMsiId": csi.id,
            "keyVaultId": key_vault_id
        })

    else:
        raise ValueError("Either --hana-db-password or both --hana-db-password-key-vault-url and --key-vault-id.")

    from azext_hanaonazure._client_factory import cf_sapmonitor_groups_v2017_11_03_preview
    sapmonitor_client_v2017_11_03_preview = cf_sapmonitor_groups_v2017_11_03_preview(cmd.cli_ctx)
    return sapmonitor_client_v2017_11_03_preview.create(resource_group_name, monitor_name, monitoring_details)

def delete_sapmonitor(cmd, client, resource_group_name, monitor_name):
    # Try creating using new API version
    try:
        return client.delete(resource_group_name, monitor_name)
    except (models.ErrorResponseException, CloudError) as error:
        print('{0} Attempting old API version'.format(error))

    # Use old version
    from azext_hanaonazure._client_factory import cf_sapmonitor_groups_v2017_11_03_preview
    sapmonitor_client_v2017_11_03_preview = cf_sapmonitor_groups_v2017_11_03_preview(cmd.cli_ctx)

    sapmonitor = sapmonitor_client_v2017_11_03_preview.get(resource_group_name, monitor_name)
    if sapmonitor.key_vault_id is not None and sapmonitor.hana_db_credentials_msi_id is not None:
        # KeyVault ID found, unassigning CSI and deleting it
        from ._client_factory import (_msi_client_factory, _keyvault_client_factory)
        from azure.cli.core.profiles import ResourceType

        # Get CSI
        match = re.search(msi_id_format, sapmonitor.hana_db_credentials_msi_id)
        csi_subscription_id = match.group(1)
        csi_resource_group = match.group(2)
        csi_resource_name = match.group(3)

        msi_client = _msi_client_factory(cmd.cli_ctx, csi_subscription_id)
        msi = msi_client.user_assigned_identities.get(csi_resource_group, csi_resource_name)

        # Unassign CSI from KeyVault
        match = re.search(keyvault_id_format, sapmonitor.key_vault_id)
        if not match:
            raise ValueError("key_vault_id is of incorrect format. The ID should start with /subscriptions/")

        kv_subscription_id = match.group(1)
        kv_resource_group = match.group(2)
        kv_resource_name = match.group(3)
        kv_client = _keyvault_client_factory(cmd.cli_ctx, kv_subscription_id)
        kv = kv_client.vaults.get(kv_resource_group, kv_resource_name)

        kv.properties.access_policies = [p for p in kv.properties.access_policies if
                                    kv.properties.tenant_id.lower() != p.tenant_id.lower() or
                                    msi.principal_id.lower() != p.object_id.lower()]

        vault_create_or_update_parameters = cmd.get_models('VaultCreateOrUpdateParameters', resource_type=ResourceType.MGMT_KEYVAULT)
        kv_client.vaults.create_or_update(
            resource_group_name=kv_resource_group,
            vault_name=kv_resource_name,
            parameters=vault_create_or_update_parameters(
                location=kv.location,
                tags=kv.tags,
                properties=kv.properties))

        # Delete CSI
        msi_client.user_assigned_identities.delete(csi_resource_group, csi_resource_name)

    return sapmonitor_client_v2017_11_03_preview.delete(resource_group_name, monitor_name)

def update_sapmonitor(cmd, client, resource_group_name, monitor_name, **kwargs):
    # Try using new API version
    try:
        return client.update(resource_group_name, monitor_name, kwargs['parameters'].tags)
    except (models.ErrorResponseException, CloudError) as error:
        print('{0} Attempting old API version'.format(error))

    from azext_hanaonazure._client_factory import cf_sapmonitor_groups_v2017_11_03_preview
    sapmonitor_client_v2017_11_03_preview = cf_sapmonitor_groups_v2017_11_03_preview(cmd.cli_ctx)
    return sapmonitor_client_v2017_11_03_preview.update(resource_group_name, monitor_name, kwargs['parameters'].tags)

def list_providerinstance(client, resource_group_name, monitor_name):
    return client.list(resource_group_name, monitor_name)

def show_providerinstance(client, resource_group_name, monitor_name, provider_instance_name):
    return client.get(resource_group_name, monitor_name, provider_instance_name)

def create_providerinstance(
      cmd,
      client,
      resource_group_name,
      monitor_name,
      provider_instance_name,
      provider_instance_type,
      provider_instance_properties,
      provider_instance_metadata=None):
    import json
    properties_json = json.loads(provider_instance_properties)

    # Validate metadata is of JSON format if provided
    metadata = None
    if provider_instance_metadata is not None:
       m = json.loads(provider_instance_metadata)
       metadata = json.dumps(m)

    if provider_instance_type == 'SapHana':
        if 'hanaDbPasswordKeyVaultUrl' in properties_json and 'keyVaultId' in properties_json:
            # Keyvault URL was passed in
            from ._client_factory import (_msi_client_factory, _keyvault_client_factory)
            from azure.mgmt.keyvault.v2018_02_14.models import (VaultAccessPolicyProperties, AccessPolicyEntry, Permissions, SecretPermissions)
            from azext_hanaonazure._client_factory import cf_sapmonitor_groups

            # Get the associated SapMonitor
            sapmonitor_client = cf_sapmonitor_groups(cmd.cli_ctx)
            sap_monitor = sapmonitor_client.get(resource_group_name, monitor_name)

            # Create MSI
            msi_client = _msi_client_factory(cmd.cli_ctx)
            csi_name = get_csi_name(msi_client.config.subscription_id, resource_group_name, monitor_name)
            csi = msi_client.user_assigned_identities.create_or_update(resource_group_name, csi_name, sap_monitor.location)

            # Extract Key Vault information
            match = re.search(keyvault_id_format, properties_json['keyVaultId'])
            if not match:
                raise ValueError("key_vault_id is of incorrect format. The ID should start with /subscriptions/")

            kv_subscription_id = match.group(1)
            kv_resource_group = match.group(2)
            kv_resource_name = match.group(3)
            kv_client = _keyvault_client_factory(cmd.cli_ctx, kv_subscription_id)

            # Get Key Vault Tenant ID
            kv = kv_client.vaults.get(kv_resource_group, kv_resource_name)

            # Add MSI to Key Vault
            secret_permissions = [SecretPermissions("get")]
            access_policy_entries = [AccessPolicyEntry(tenant_id=kv.properties.tenant_id, object_id=csi.principal_id, permissions=Permissions(secrets=secret_permissions))]
            vault_access_policy_properties = VaultAccessPolicyProperties(access_policies=access_policy_entries)
            kv_client.vaults.update_access_policy(kv_resource_group,kv_resource_name, 'add', vault_access_policy_properties)
            properties_json.update({
                "hanaDbCredentialsMsiId": csi.id,
            })
        elif 'hanaDbPassword' not in properties_json:
            raise ValueError("Either hanaDbPassword or both hanaDbPasswordKeyVaultUrl and keyVaultId.")

    from azext_hanaonazure.modules_sdk.v2020_02_07_preview.models import ProviderInstance
    pi = ProviderInstance(provider_instance_type=provider_instance_type, properties=json.dumps(properties_json), metadata=metadata)
    return client.create(resource_group_name, monitor_name, provider_instance_name, pi)

def delete_providerinstance(cmd, client, resource_group_name, monitor_name, provider_instance_name):
    import json

    from azext_hanaonazure._client_factory import cf_sapmonitor_groups
    sapmonitor_client = cf_sapmonitor_groups(cmd.cli_ctx)
    sapmonitor = sapmonitor_client.get(resource_group_name, monitor_name)

    provider_instance = client.get(resource_group_name, monitor_name, provider_instance_name)
    if provider_instance.type == "SapHana":
        properties = json.loads(provider_instance.properties.properties)
        if 'hanaDbPasswordKeyVaultUrl' in properties:
            # KeyVault ID found, unassigning CSI and deleting it
            from ._client_factory import (_msi_client_factory, _keyvault_client_factory)
            from azure.cli.core.profiles import ResourceType

            # Get CSI
            match = re.search(msi_id_format, properties['hanaDbCredentialsMsiID'])
            csi_subscription_id = match.group(1)
            csi_resource_group = match.group(2)
            csi_resource_name = match.group(3)

            msi_client = _msi_client_factory(cmd.cli_ctx, csi_subscription_id)
            msi = msi_client.user_assigned_identities.get(csi_resource_group, csi_resource_name)

            # Unassign CSI from KeyVault
            match = re.search(keyvault_id_format, sapmonitor.key_vault_id)
            if not match:
                raise ValueError("key_vault_id is of incorrect format. The ID should start with /subscriptions/")

            kv_subscription_id = match.group(1)
            kv_resource_group = match.group(2)
            kv_resource_name = match.group(3)
            kv_client = _keyvault_client_factory(cmd.cli_ctx, kv_subscription_id)
            kv = kv_client.vaults.get(kv_resource_group, kv_resource_name)

            kv.properties.access_policies = [p for p in kv.properties.access_policies if
                                             kv.properties.tenant_id.lower() != p.tenant_id.lower() or
                                             msi.principal_id.lower() != p.object_id.lower()]

            vault_create_or_update_parameters = cmd.get_models('VaultCreateOrUpdateParameters', resource_type=ResourceType.MGMT_KEYVAULT)
            kv_client.vaults.create_or_update(
                resource_group_name=kv_resource_group,
                vault_name=kv_resource_name,
                parameters=vault_create_or_update_parameters(
                    location=kv.location,
                    tags=kv.tags,
                    properties=kv.properties))

            # Delete CSI
            msi_client.user_assigned_identities.delete(csi_resource_group, csi_resource_name)

    return client.delete(resource_group_name, monitor_name, provider_instance_name)

def get_csi_name(subscription_id, resource_group, resource_name):
    arm_resource_id = arm_resource_id_format.format(subscription_id, resource_group, resource_name)
    return 'sapmon-csi-{}'.format(hash(arm_resource_id))

def hash(str):
    hval = 0x811c9dc5
    fnv_32_prime = 0x01000193
    uint32_max = 2 ** 32
    for s in str:
        hval = hval ^ ord(s)
        hval = (hval * fnv_32_prime) % uint32_max
    return hval
