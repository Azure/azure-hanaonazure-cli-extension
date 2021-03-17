# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (resource_group_name_type,
                                                get_location_type,
                                                tags_type)


def load_arguments(self, _):
    with self.argument_context('hanainstance') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   help='Location of the SAP HANA instance. Default is the location of target resource group.')
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('instance_name', options_list=[
                   '--instance-name', '-n'], help="The name of the SAP HANA instance", id_part='name')
        c.argument('partner_node_id', options_list=[
                   '--partner-node-id'], help="ARM ID of a HANA Instance on the network to connect the SAP HANA instance")
        c.argument('ssh_public_key', options_list=[
                   '--ssh-public-key'], help="SSH public key to connect to the SAP HANA instance")
        c.argument('os_computer_name', options_list=[
                   '--os-computer-name'], help="OS computer name of the SAP HANA instance")
        c.argument('ip_address', options_list=[
                   '--ip-address'], help="IP address to connect to the SAP HANA instance")
    with self.argument_context('sapmonitor') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('monitor_name', options_list=[
            '--monitor-name', '-n'], help="The name of the SAP monitor")
    with self.argument_context('sapmonitor create') as c:
        c.argument('region', options_list=[
            '--region'], help="The region to create this SAP monitor on.")
        c.argument('hana_subnet', options_list=[
            '--hana-subnet', '--hdbsn'], help="ARM ID of an Azure Subnet with access to the HANA instance.")
        c.argument('disable_customer_analytics', options_list=[
            '--disable_customer_analytics', '--dca'], help="Disable sending analytics to Microsoft")
        c.argument('log_analytics_workspace_arm_id', options_list=[
            '--log-analytics-workspace-arm-id', '--lawsid'], help="Existing log analytics workspace id to use for log monitoring")
        c.argument('tags', tags_type)
    with self.argument_context('sapmonitor provider-instance') as c:
        c.argument('provider_instance_name', options_list=[
            '--provider-instance-name'], help="The name of the provider instance.")
        c.argument('provider_instance_properties', options_list=[
            '--provider-instance-properties'], help="The properties of the provider instance (Should be of JSON format).")
        c.argument('provider_instance_type', options_list=[
            '--provider-instance-type'], help="The type of the provider instance.")
        c.argument('provider_instance_metadata', options_list=[
            '--provider-instance-metadata'], help="The metadata of the provider instance (Should be of JSON format).")
