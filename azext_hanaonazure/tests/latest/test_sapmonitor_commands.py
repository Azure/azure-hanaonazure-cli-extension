import unittest

from azure.cli.testsdk import ScenarioTest

class SapMonitorScenarioTests(ScenarioTest):
    def test_create_sapmonitor(self):
        self.kwargs.update({
            'region': 'japanwest',
            'resource_group': 'sapmonitor-lab',
            'monitor_name': "donaliuTesting",
            'hana_subnet': '/subscriptions/c4106f40-4f28-442e-b67f-a24d892bf7ad/resourceGroups/sapmonitor-lab/providers/Microsoft.Network/virtualNetworks/SML-vnet/subnets/hdb-subnet',
            'hana_hostname': "10.0.0.6",
            'hana_db_sql_port': "30015",
            'hana_db_name': "SYSTEMDB",
            'hana_db_username': "admin",
            'hana_db_password': "password1"
        })
        sapmonitor = self.cmd('az sapmonitor create \
                                    --region {region} \
                                    --resource-group {resource_group} \
                                    --monitor-name {monitor_name} \
                                    --hana-subnet "{hana_subnet}" \
                                    --hana-hostname {hana_hostname} \
                                    --hana-db-sql-port {hana_db_sql_port} \
                                    --hana-db-name {hana_db_name} \
                                    --hana-db-username {hana_db_username} \
                                    --hana-db-password {hana_db_password}') .get_output_in_json()
        assert sapmonitor["provisioningState"] == "Succeeded"


if __name__ == '__main__':
    unittest.main()
