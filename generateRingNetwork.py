import json
import collections
num_switches = 3
hosts_per_switch = 2

network = { 'name': 'RingNetwork',
            'switches': []}

#generate Switches with a number of hosts connected to them
for i in range(1,num_switches + 1):
    s = {   'name'  : 's{0}'.format(i),
            'number': i,
            'ip': '10.0.{0}.1'.format(i),
            'mac' : '00:00:00:00:{0:02d}:1'.format(i),
            'hosts' : []
            }

    for j in range(1, num_switches * hosts_per_switch + 1, num_switches):
        host_num = j + i - 1
        print(host_num)
        h = {   'name':'h{0}'.format(host_num),
                'number': j,
                'ip': '10.0.{0}.{1}'.format(i, host_num + 1),
                'mac' : '00:00:00:00:{0:02d}:{1:02d}'.format(i, host_num + 1),
                'switch_ip': 0,
                'switch_mac' : 0
                }
        s['hosts'].append(h)

    network['switches'].append(s)

switch_links = []
#generate inter-switch links
for i in range(0,num_switches):
    switch_links.append({ 'node1': network['switches'][i]['name'],
                                'node2': network['switches'][(i+1) % num_switches]['name']})

network['switch_links'] = switch_links

#print(json.dumps(inter_switch_links, sort_keys=True, indent=4, separators=(',', ': ')))
#print(json.dumps(s, sort_keys=True, indent=4, separators=(',', ': ')))
#print(links)

with open('{0}.json'.format(network['name']), 'w') as network_file:
    json.dump(network, network_file, sort_keys=True, indent=4, separators=(',', ': '))
