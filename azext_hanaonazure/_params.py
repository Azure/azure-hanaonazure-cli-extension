# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import resource_group_name_type


def load_arguments(self, _):
    with self.argument_context('hanainstance') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('instance_name', options_list=[
                   '--instance-name', '-n'], help="The name of the SAP HANA instance", id_part='name')
    with self.argument_context('hanainstance monitor') as c:
        c.argument('hana_vnet', options_list=[
                   '--hana-vnet', '-hv'], help="ARM ID of an Azure Vnet with access to the HANA instance.")
        c.argument('hana_hostname', options_list=[
                   '--hana-hostname'], help="Hostname of the HANA Instance blade.")
        c.argument('hana_instance_num', options_list=[
                   '--hana-instance-num'], help="A number between 00 and 99")
        c.argument('use_mdc', options_list=[
                   '--use-mdc'], help="A boolean to determine the use of Multiple Database Containers")
        c.argument('hana_database', options_list=[
                   '--hana-database', '-hdb'], help="Name of the database itself.  It only needs to be specified if using MDC")
        c.argument('hana_db_username', options_list=[
                   '--hana-db-username'], help="Username for the HANA database to login to for monitoring")
        c.argument('hana_db_password', options_list=[
                   '--hana-db-password', '-hdbpw'], help="Password for the HANA database to login for monitoring")
