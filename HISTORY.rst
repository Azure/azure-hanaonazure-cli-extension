.. :changelog:

Release History
===============

0.6.5 (2020-10-15)
++++++++++++++++++

- Removed usage of old API version (v2017-11-03-preview) for SapMonitor resources

0.6.4 (2020-06-17)
++++++++++++++++++

- Create provider instance using Key Vault will no longer pass hanaDbCredentialsMsiId to the API request

0.6.3 (2020-06-02)
++++++++++++++++++

- Added tags field to SAP Monitor create

0.6.2 (2020-05-18)
++++++++++++++++++

- Updated SDK
- Create SapHana provider instance with Key Vault will reuse MSI instead of creating a new one
- "Attempting old api version" message will be sent to logger debug rather than printing

0.6.1 (2020-04-16)
++++++++++++++++++

- Added metadata field to provider instance

0.6.0 (2020-04-15)
++++++++++++++++++

- Added Multi-Instance Multi-Provider Feature

0.5.9 (2020-02-14)
++++++++++++++++++

- Removed invalid SKUs: S224oxm, S224oxxm, S224o
- Added SD-Flex SKUs

0.5.8 (2019-11-26)
++++++++++++++++++

- Added --log-analytics-workspace-arm-id to allow using existing log analytics workspace for SAP Monitor

0.5.7 (2019-11-22)
++++++++++++++++++

- Added disable_customer_analytics parameter to opt out of sending analytics information to Microsoft

0.5.6 (2019-11-12)
++++++++++++++++++

- Add Cascade Lake SKUs

0.5.5 (2019-09-04)
++++++++++++++++++

- Added Update method for SapMonitor, which will allow adding tags

0.5.4 (2019-08-08)
++++++++++++++++++

- GET method for SapMonitor also returns LogAnalyticsWorkspace info

0.5.3 (2019-08-01)
++++++++++++++++++

- Removing enable monitor on hana instance

0.5.2 (2019-07-24)
++++++++++++++++++

- sapmonitor create will also accept keyvault url as credentials

0.5.1 (2019-07-05)
++++++++++++++++++

- Added start and shutdown commands

0.5.0 (2019-06-26)
++++++++++++++++++

- Added SAP Monitor list, show, create and delete

0.4.1 (2019-06-17)
++++++++++++++++++

- Fixing a typo that prevented the hana-db-name from being read

0.4.0 (2019-06-17)
++++++++++++++++++

- Add APIs to create and delete a HanaInstance
- Edit API version format to add parameters necessary for creating a HanaInstance

0.3.9 (2019-06-14)
++++++++++++++++++

- Remove use of min_profile to comply with CLI core version 2.0.67

0.3.8 (2019-06-12)
++++++++++++++++++

- Set the maximum CLI core version to avoid breaking change in CLI core version 2.0.67

0.3.7 (2019-05-23)
++++++++++++++++++

- Fixing the short command options for monitoring

0.3.6 (2019-05-22)
++++++++++++++++++

- Add new SKU S224o, S224m, S224om, S224oxm, S224oxxm

0.3.5 (2019-05-21)
++++++++++++++++++

- Add monitoring capabilities to hana instance

0.3.4 (2019-02-26)
++++++++++++++++++

- Add hwRevision field to Hana Instance model

0.3.3 (2019-01-30)
++++++++++++++++++

- Restart command is now asynchronous

0.3.2 (2019-01-29)
++++++++++++++++++

**Features**

- Add proximity_placement_group

0.3.0 (2019-01-03)
++++++++++++++++++

**Features**

- Added operation HanaInstancesOperations.update

0.1.6 (2018-09-11)
++++++++++++++++++

* Style guidelines and new version.

0.1.5 (2018-09-06)
++++++++++++++++++

* Added restart command.

0.1.1 (2018-05-18)
++++++++++++++++++

* Release of CLI extension version 0.1.1.

0.0.1 (2018-01-17)
++++++++++++++++++

* Initial release.
