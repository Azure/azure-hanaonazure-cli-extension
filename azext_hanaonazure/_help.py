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

helps['hanainstance create'] = """
    type: command
    short-summary: Create a new SAP HANA Instance.
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

helps['hanainstance start'] = """
    type: command
    short-summary: Start a SAP HANA Instance.
"""

helps['hanainstance shutdown'] = """
    type: command
    short-summary: Shutdown a SAP HANA Instance.
"""

helps['hanainstance update'] = """
    type: command
    short-summary: Update the Tags field of a SAP HANA Instance.
"""

helps['hanainstance delete'] = """
    type: command
    short-summary: Delete a SAP HANA Instance.
"""

helps['sapmonitor'] = """
    type: group
    short-summary: (PREVIEW) Manage Azure SAP Monitor.
"""

helps['sapmonitor list'] = """
    type: command
    short-summary: List SAP Monitors.
"""

helps['sapmonitor show'] = """
    type: command
    short-summary: Get the details of a SAP Monitor.
"""

helps['sapmonitor create'] = """
    type: command
    short-summary: Create a SAP Monitor.
"""

helps['sapmonitor delete'] = """
    type: command
    short-summary: Delete a SAP Monitor.
"""
helps['sapmonitor update'] = """
    type: command
    short-summary: Updates the tags field of a SAP Monitor.
"""