# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def _hana_instance_client_factory(cli_ctx, *_):
    from azext_hanaonazure.modules_sdk import HanaManagementClient
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, HanaManagementClient)

def cf_hanainstance_groups(cli_ctx, *_):
    return _hana_instance_client_factory(cli_ctx).hana_instances

def _msi_client_factory(cli_ctx, subscription_id=None):
    from azure.mgmt.msi import ManagedServiceIdentityClient
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, ManagedServiceIdentityClient, subscription_id=subscription_id)

def _keyvault_client_factory(cli_ctx, subscription_id=None):
    from azure.mgmt.keyvault import KeyVaultManagementClient
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, KeyVaultManagementClient, subscription_id=subscription_id)

def _loganalytics_client_factory(cli_ctx, subscription_id=None):
    from azure.mgmt.loganalytics import LogAnalyticsManagementClient
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, LogAnalyticsManagementClient, subscription_id=subscription_id)

def cf_sapmonitor_groups(cli_ctx, *_):
    return _hana_instance_client_factory(cli_ctx).sap_monitors
