import unittest

from azure.cli.testsdk import ScenarioTest

class HanaInstanceScenarioTests(ScenarioTest):
    def test_create_hanainstance(self):
        TEST_SSH_KEY_PUB = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCbIg1guRHbI0lV11wWDt1r2cUdcNd27CJsg+SfgC7miZeubtwUhbsPdhMQsfDyhOWHq1+ZL0M+nJZV63d/1dhmhtgyOqejUwrPlzKhydsbrsdUor+JmNJDdW01v7BXHyuymT8G4s09jCasNOwiufbP/qp72ruu0bIA1nySsvlf9pCQAuFkAnVnf/rFhUlOkhtRpwcq8SUNY2zRHR/EKb/4NWY1JzR4sa3q2fWIJdrrX0DvLoa5g9bIEd4Df79ba7v+yiUBOS0zT2ll+z4g9izHK3EO5d8hL4jYxcjKs+wcslSYRWrascfscLgMlMGh0CdKeNTDjHpGPncaf3Z+FwwwjWeuiNBxv7bJo13/8B/098KlVDl4GZqsoBCEjPyJfV6hO0y/LkRGkk7oHWKgeWAfKtfLItRp00eZ4fcJNK9kCaSMmEugoZWcI7NGbZXzqFWqbpRI7NcDP9+WIQ+i9U5vqWsqd/zng4kbuAJ6UuKqIzB0upYrLShfQE3SAck8oaLhJqqq56VfDuASNpJKidV+zq27HfSBmbXnkR/5AK337dc3MXKJypoK/QPMLKUAP5XLPbs+NddJQV7EZXd29DLgp+fRIg3edpKdO7ZErWhv7d+3Kws+e1Y+ypmR2WIVSwVyBEUfgv2C8Ts9gnTF4pNcEY/S2aBicz5Ew2+jdyGNQQ== test@example.com\n"  # pylint: disable=line-too-long
        self.kwargs.update({
            'resource_group': 'rg',
            'name': "Test02",
            'ip': "10.19.17.52",
            'location': "japaneast",
            'partner': "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg/providers/Microsoft.HanaOnAzure/hanaInstances/Test01",
            'pub-key': TEST_SSH_KEY_PUB,
        })
        hanaInstance = self.cmd('az hanainstance create -n {name} \
                                                        --ip-address {ip} \
                                                        -l {location} \
                                                        --os-computer-name {name} \
                                                        --partner-node-id "{partner}" \
                                                        -g {resource_group} \
                                                        --ssh-public-key "{pub-key}"').get_output_in_json()
        assert hanaInstance["provisioningState"] == "Succeeded"

if __name__ == '__main__':
    unittest.main()
