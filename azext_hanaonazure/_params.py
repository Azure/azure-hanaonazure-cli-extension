# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import resource_group_name_type


def load_arguments(self, _):
    with self.argument_context('hanainstance') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('instance_name', options_list=['--instance-name', '-n'], help="The name of the SAP HANA instance", id_part='name')
        c.argument('hana_vnet', options_list=['--hana-vnet', '-hv'], help="ARM ID of an Azure Vnet with access to the HANA instance.")
        c.argument('hana_hostname', options_list=['--hana-hostname'], help="Hostname of the HANA Instance blade.")
        c.argument('hana_instance_num', options_list=['--hana-instance-num'], help="A number between 00 and 99, stored as a string to maintain leading zero.")
        c.argument('db_container', options_list=['--db-container'], help="Either single or multiple depending on the use of MDC(Multiple Database Containers). Possible values include: 'single','multiple'")
        c.argument('hana_database', options_list=['--hana-database', '-hdb'], help="Name of the database itself.  It only needs to be specified if using MDC")
        c.argument('hana_db_username', options_list=['--hana-db-username'], help="Username for the HANA database to login to for monitoring")
        c.argument('hana_db_password', options_list=['--hana-db-password', '-hdbpw'], help="Password for the HANA database to login for monitoring")
