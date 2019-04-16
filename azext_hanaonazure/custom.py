# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=no-self-use,too-many-lines


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

def enable_monitoring_hanainstance(client, resource_group_name, instance_name, hana_vnet, hana_hostname, hana_instance_num, hana_db_username, hana_db_password, db_container="single", hana_database=None):
    monitoring_details = {
        "hanaInstanceNum": hana_instance_num,
        "hanaVnet": hana_vnet,
        "hanaHostname": hana_hostname,
        "hanaDbUsername": hana_db_username,
        "hanaDbPassword": hana_db_password,
        "dbContainer": db_container
    }
    if hana_database is not None:
        if db_container is "multiple":
            monitoring_details['hanaDatabase'] = hana_database
    return client.enable_monitoring(resource_group_name, instance_name, monitoring_details)