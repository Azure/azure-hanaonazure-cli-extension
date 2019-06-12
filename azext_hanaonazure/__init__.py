# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

import azext_hanaonazure._help  # pylint: disable=unused-import


class HanaInstanceCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_type = CliCommandType(operations_tmpl='azext_hanaonazure.custom#{}')
        super(HanaInstanceCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                         custom_command_type=custom_type)

    def load_command_table(self, args):
        from azext_hanaonazure.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_hanaonazure._params import load_arguments
        load_arguments(self, command)

COMMAND_LOADER_CLS = HanaInstanceCommandsLoader