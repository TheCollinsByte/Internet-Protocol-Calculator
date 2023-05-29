import unittest

def test_calculate_network_address():
    ip_address = '192.168.1.0'
    network_mask = '24'

    expected_network_address = '192.168.1.0'

    actual_network_address = calculate_network_address(ip_address, network_mask)

    assert actual_network_address == expected_network_address
