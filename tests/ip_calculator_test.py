import unittest 

from ip_caculator import ip_caculator

class TestIpCalculator(unittest.TestCase):

    def test_valid_input(self):
        """Test that the function returns the correct results for valid input."""

        # Valid Input
        ip_address = '192.168.1.1'
        subnet_mask = '255.255.255.0'


        # Expected results
        network_id = '192.168.1.0'
        broadcast_address = '192.168.1.255'
        host_addresses = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6', '192.168.1.7', '192.168.1.8', '192.168.1.9', '192.168.1.10']

        
        # Actual results
        network_id_actual, broadcast_address_actual, host_addresses_actual = ip_caculator(ip_address, subnet_mask)


        # Assert that the actual results match the expected results.
        self.assertEqual(network_id_actual, network_id)
        self.assertEqual(broadcast_address_actual, broadcast_address)
        self.assertEqual(host_addresses_actual, host_addresses)

    def test_invalid_input(self):
        """Test that the function raises an exception for invalid input."""

        # Invalid Input
        ip_address = '192.168.1.256'
        subnet_mask = '255.255.255.0'

        with self.assertRaises(ValueError):
            ip_caculator(ip_address, subnet_mask)
