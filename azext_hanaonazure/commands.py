# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.util import empty_on_404
from ._client_factory import cf_hanainstance_groups
from azure.cli.core.commands import CliCommandType

def load_command_table(self, _):
    custom_tmpl = 'azext_hanaonazure.custom#{}'
    custom_type = CliCommandType(operations_tmpl=custom_tmpl)

    with self.command_group('hanainstance', client_factory=cf_hanainstance_groups) as g:
        g.custom_command('list', 'list_hanainstance')
        g.custom_command('show', 'show_hanainstance',
                         exception_handler=empty_on_404)
        g.custom_command('restart', 'restart_hanainstance')
        g.generic_update_command('update', getter_name='show_hanainstance', setter_name='update_hanainstance',
                                 command_type=custom_type, supports_no_wait=True)

    with self.command_group('hanainstance monitor', client_factory=cf_hanainstance_groups) as g:
        g.custom_command('enable', 'enable_monitoring_hanainstance')