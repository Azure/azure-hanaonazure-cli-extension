# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=no-self-use,too-many-lines


def create_hanainstance(client, location, resource_group_name, instance_name, partner_node_id, ssh_public_key, os_computer_name, ip_address):
    try:
        from .modules_sdk.models.os_profile_py3 import OSProfile
        from .modules_sdk.models.ip_address_py3 import IpAddress
        from .modules_sdk.models.network_profile_py3 import NetworkProfile
        from .modules_sdk.models.hana_instance_py3 import HanaInstance
    except (SyntaxError, ImportError):
        from .modules_sdk.models.os_profile import OSProfile
        from .modules_sdk.models.ip_address import IpAddress
        from .modules_sdk.models.network_profile import NetworkProfile
        from .modules_sdk.models.hana_instance import HanaInstance

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
    custom_header = {}
    custom_header['Content-Type'] = 'application/json; charset=utf-8'
    return client.restart(resource_group_name, instance_name, custom_header)


def update_hanainstance(client, resource_group_name, instance_name, **kwargs):
    return client.update(resource_group_name, instance_name, kwargs['parameters'].tags)


def delete_hanainstance(client, resource_group_name, instance_name):
    return client.delete(resource_group_name, instance_name)


def enable_monitoring_hanainstance(client, resource_group_name, instance_name, hana_subnet, hana_hostname, hana_db_sql_port, hana_db_username, hana_db_password, hana_db_name=""):
    monitoring_details = {
        "hanaSubnet": hana_subnet,
        "hanaHostname": hana_hostname,
        "hanaDbName": hana_db_name,
        "hanaDbSqlPort": hana_db_sql_port,
        "hanaDbUsername": hana_db_username,
        "hanaDbPassword": hana_db_password
    }
    return client.enable_monitoring(resource_group_name, instance_name, monitoring_details)

def list_sapmonitor(client):
    return client.list()

def show_sapmonitor(client, resource_group_name, monitor_name):
    return client.get(resource_group_name, monitor_name)

def create_sapmonitor(client, resource_group_name, monitor_name, region, hana_subnet, hana_hostname, hana_db_sql_port, hana_db_username, hana_db_password, hana_db_name):
    monitoring_details = {
        "location": region,
        "hanaSubnet": hana_subnet,
        "hanaHostname": hana_hostname,
        "hanaDbName": hana_db_name,
        "hanaDbSqlPort": hana_db_sql_port,
        "hanaDbUsername": hana_db_username,
        "hanaDbPassword": hana_db_password
    }
    return client.create(resource_group_name, monitor_name, monitoring_details)

def delete_sapmonitor(client, resource_group_name, monitor_name):
    return client.delete(resource_group_name, monitor_name)