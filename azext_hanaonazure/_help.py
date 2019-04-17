# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.help_files import helps


helps['hanainstance'] = """
    type: group
    short-summary: (PREVIEW) Manage Azure SAP HANA Instance.
    """
helps['hanainstance show'] = """
    type: command
    short-summary: Get the details of a SAP HANA Instance.
    """

helps['hanainstance list'] = """
    type: command
    short-summary: List SAP HANA Instances.
"""

helps['hanainstance restart'] = """
    type: command
    short-summary: Restart a SAP HANA Instance.
"""

helps['hanainstance update'] = """
    type: command
    short-summary: Update the Tags field of a SAP HANA Instance.
"""

helps['hanainstance monitor'] = """
    type: command
    short-summary: Add monitoring for a SAP HANA Instance.
"""
