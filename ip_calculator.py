import ipaddress        # This line imports the ipaddress module, which provides functions for working with IP addresses.


def ip_caculator(ip_address, subnet_mask):
    """This function calculates the Network ID, broadcast address, and list of host addresses for a given IP address and subnet mask."""

    # Create a `ipaddress.ip_network` object from the IP address and subnet mask
    network = ipaddress.ip_network(ip_address + '/' + subnet_mask)

    # Get the network ID from the `ip_network` object
    network_id = network.network_address

    # Get the broadcast address from the `ip_network` object
    broadcast_address = network.broadcast_address

    # Create an empty list to store the host addresses.
    host_addresses = []

    # Iterate over all the hosts in the network and add them to the `host_addresses` list.
    for host in network.hosts():
        host_addresses.append(host)

    # Return the network ID, broadcast address and host addresses
    return network_id, broadcast_address, host_addresses


if __name__ == '__main__':
    # Prompt the User to enter IP address and subnet mask
    ip_address = input('Enter the IP Address: ')
    subnet_mask = input('Enter the subnet_mask: ')

    # Call the `ip_calculator` function and store the results in the `network_id`, `broadcast_address`, and `host_addresses` variables.
    network_id, broadcast_address, host_addresses = ip_caculator(ip_address, subnet_mask)

    # Print the `network_id`, `Broadcast_address` and `host_addresses`
    print('Network ID:', network_id)
    print('Broadcast address:', broadcast_address)

    print('Host address:')
    for host in host_addresses:
        print(host)

