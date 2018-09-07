# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.util import empty_on_404
from ._client_factory import cf_hanainstance_groups


def load_command_table(self, _):
    with self.command_group('hanainstance', client_factory=cf_hanainstance_groups) as g:
        g.custom_command('list', 'list_hanainstance')
        g.custom_command('show', 'show_hanainstance', exception_handler=empty_on_404)
        g.custom_command('restart', 'restart_hanainstance')
