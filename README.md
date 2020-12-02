# azure-hanaonazure-cli-extension

# Install

To install this extension just use the CLI extension add command:

```
az extension add --name sap-hana
```

# Usage
## HANA instance
To create a new HANA instance:

```
az hanainstance create \
    --location $LOCATION \
    --resource-group $RESOURCE_GROUP \
    --instance-name $HANA_INSTANCE_NAME \
    --partner-node-id $PARTNER_NODE \
    --ssh-public-key $SSH_PUBLIC_KEY \
    --os-computer-name $COMPUTER_NAME \
    --ip-address $IP_ADDRESS
```

To list all HANA instances for the subscription:

```
az hanainstance list
```

To show details about a specific HANA instance:

```
az hanainstance show --resource-group $RESOURCE_GROUP --instance-name $HANA_INSTANCE_NAME
```

To add a key-value pair to the Tags field of a specific HANA instance:

```
az hanainstance update --resource-group $RESOURCE_GROUP --instance-name $HANA_INSTANCE_NAME --set tags.newKey=value
```

To update a key-value pair in the Tags field of a specific HANA instance:

```
az hanainstance update --resource-group $RESOURCE_GROUP --instance-name $HANA_INSTANCE_NAME --set tags.key=updatedValue
```

To delete a key-value pair from the Tags field of a specific HANA instance:

```
az hanainstance update --resource-group $RESOURCE_GROUP --instance-name $HANA_INSTANCE_NAME --remove tags.key
```

To delete all key-value pairs in the Tags field of a specific HANA instance:

```
az hanainstance update --resource-group $RESOURCE_GROUP --instance-name $HANA_INSTANCE_NAME --set tags={}
```

To delete a HANA instance:

```
az hanainstance delete --resource-group $RESOURCE_GROUP --instance-name $HANA_INSTANCE_NAME
```

To start a specific HANA instance:

```
az hanainstance start --resource-group $RESOURCE_GROUP --instance-name $HANA_INSTANCE_NAME
```

To restart a specific HANA instance:

```
az hanainstance restart --resource-group $RESOURCE_GROUP --instance-name $HANA_INSTANCE_NAME
```

To shutdown a specific HANA instance:

```
az hanainstance shutdown --resource-group $RESOURCE_GROUP --instance-name $HANA_INSTANCE_NAME
```

## SapMonitor
To create a new SapMonitor:
```
az sapmonitor create \
    --resource-group $RESOURCE_GROUP \
    --monitor-name $SAP_MONITOR_NAME \
    --hana-subnet $HANA_SUBNET_ID \
    --region $REGION
```
Here is an example of a subnet ID:
```
/subscriptions/<subscription_id>/resourceGroups/<resource_group>/providers/Microsoft.Network/virtualNetworks/<vnet_name>/subnets/<subnet_name>
```

To list all SapMonitor for a subscription:
```
az sapmonitor list
```

To show details about a specific SapMonitor:
```
az sapmonitor show --resource-group $RESOURCE_GROUP --monitor-name $SAP_MONITOR_NAME
```

To add a key-value pair to the Tags field of a specific SapMonitor:
```
az sapmonitor update --resource-group $RESOURCE_GROUP --monitor-name $SAP_MONITOR_NAME --set tags.newKey=value
```

To delete all key-value pairs in the Tags field of a specific SapMonitor:
```
az sapmonitor update --resource-group $RESOURCE_GROUP --monitor-name $SAP_MONITOR_NAME --set tags={}
```

To delete a SapMonitor:
```
az sapmonitor delete --resource-group $RESOURCE_GROUP --monitor-name $SAP_MONITOR_NAME
```

## Provider Instance
To create a new provider instance on a SapMonitor:
```
az sapmonitor provider-instance create \
    --resource-group $RESOURCE_GROUP \
    --monitor-name $SAP_MONITOR_NAME \ 
    --provider-instance-name $PROVIDER_INSTANCE_NAME \
    --provider-instance-type $PROVIDER_INSTANCE_TYPE \
    --provider-instance-properties $PROVIDER_INSTANCE_PROPERTIES \
    --provider-instance-metadata $PROVIDER_INSTANCE_METADATA
```
Here are examples of provider instance types and their properties

| Provider Type                    | Provider Properties                                                                                                              | Required Metadata                                     |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------| ----------------------------------------------------- |
| SapHana                          | {"hanaHostname":"10.0.0.6","hanaDbName":"SYSTEMDB","hanaDbSqlPort":30013,"hanaDbUsername":"SYSTEM"," hanaDbPassword":"password"} | None                                                  |
| PrometheusHaCluster              | {"prometheusUrl":"http://10.0.0.20:9664/metrics"}                                                                                | {"sid":"HA1","hostname":"hdb1-0","clustername":"HA1"} |
| PrometheusOS                     | {"prometheusUrl":"http://10.0.0.21:9664/metrics"}                                                                                | None                                                  |
| MsSqlServer                      | {"sqlHostname":"10.0.0.6","sqlPort":1433,"sqlUsername":"sqladmin","sqlPassword":"password"}                                      | None                                                  |

To list all provider instances for a SapMonitor:
```
az sapmonitor provider-instance list --resource-group $RESOURCE_GROUP --monitor-name $SAP_MONITOR_NAME
```

To show details about a specific provider instances for a SapMonitor:
```
az sapmonitor provider-instance show --resource-group $RESOURCE_GROUP --monitor-name $SAP_MONITOR_NAME --provider-instance-name $PROVIDER_INSTANCE_NAME
```

To delete a provider instances for a SapMonitor:
```
az sapmonitor provider-instance delete --resource-group $RESOURCE_GROUP --monitor-name $SAP_MONITOR_NAME --provider-instance-name $PROVIDER_INSTANCE_NAME
```

# Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
