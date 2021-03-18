# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.util import empty_on_404
from ._client_factory import (cf_hanainstance_groups, cf_sapmonitor_groups, cf_providerinstance_groups)
from azure.cli.core.commands import CliCommandType

def load_command_table(self, _):
    custom_tmpl = 'azext_hanaonazure.custom#{}'
    custom_type = CliCommandType(operations_tmpl=custom_tmpl)

    with self.command_group('hanainstance', client_factory=cf_hanainstance_groups) as g:
        g.custom_command('create', 'create_hanainstance')
        g.custom_command('list', 'list_hanainstance')
        g.custom_show_command('show', 'show_hanainstance')
        g.custom_command('restart', 'restart_hanainstance')
        g.custom_command('start', 'start_hanainstance')
        g.custom_command('shutdown', 'shutdown_hanainstance')
        g.generic_update_command('update', getter_name='show_hanainstance', setter_name='update_hanainstance',
                                 command_type=custom_type, supports_no_wait=True)
        g.custom_command('delete', 'delete_hanainstance')

    with self.command_group('sapmonitor', client_factory=cf_sapmonitor_groups) as g:
        g.custom_command('list', 'list_sapmonitor')
        g.custom_show_command('show', 'show_sapmonitor')
        g.custom_command('create', 'create_sapmonitor')
        g.generic_update_command('update', getter_name='show_sapmonitor', setter_name='update_sapmonitor',
                                 command_type=custom_type, supports_no_wait=True)
        g.custom_command('delete', 'delete_sapmonitor')

    with self.command_group('sapmonitor provider-instance', client_factory=cf_providerinstance_groups) as g:
        g.custom_command('list', 'list_providerinstance')
        g.custom_command('show', 'show_providerinstance', exception_handler=empty_on_404)
        g.custom_command('create', 'create_providerinstance')
        g.custom_command('delete', 'delete_providerinstance')
