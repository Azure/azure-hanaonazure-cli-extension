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