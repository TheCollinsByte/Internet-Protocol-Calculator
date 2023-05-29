import ipaddress

def ip_caculator(ip_address, subnet_mask):
    network = ipaddress.ip_network(ip_address + '/' + subnet_mask)

    network_id = network.network_address
    broadcast_address = network.broadcast_address

    host_addresses = []

    for host in network.hosts():
        host_addresses.append(host)

    return network_id, broadcast_address, host_addresses


if __name__ == '__main__':
    ip_address = input('Enter the IP Address: ')
    subnet_mask = input('Enter the subnet_mask: ')

    network_id, broadcast_address, host_addresses = ip_caculator(ip_address, subnet_mask)

    print('Network ID:', network_id)
    print('Broadcast address:', broadcast_address)

    print('Host address:')
    for host in host_addresses:
        print(host)

