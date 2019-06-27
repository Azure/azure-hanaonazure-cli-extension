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

def cf_sapmonitor_groups(cli_ctx, *_):
    return _hana_instance_client_factory(cli_ctx).sap_monitors
