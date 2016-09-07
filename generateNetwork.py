from SwitchData import SwitchData
import json

s1 = SwitchData('s1')
s1.addPort('s1-eth1', '00:00:00:00:01:01', '10.0.4.1')

s2 = SwitchData('s2')
s2.addPort('s2-eth1', '00:00:00:00:02:01', '10.0.4.2')
s2.addPort('s2-eth2', '00:00:00:00:02:02', '10.0.3.1')
s2.addPort('s2-eth3', '00:00:00:00:02:03', '10.0.5.1')

s3 = SwitchData('s3')
s3.addPort('s3-eth1', '00:00:00:00:03:01', '10.0.5.2')
s3.addPort('s3-eth2', '00:00:00:00:03:02', '10.0.1.1')
s3.addPort('s3-eth3', '00:00:00:00:03:03', '10.0.2.1')

s4 = SwitchData('s4')
s4.addPort('s4-eth1', '00:00:00:00:04:01', '10.0.1.2')

s5 = SwitchData('s5')
s5.addPort('s5-eth1', '00:00:00:00:05:01', '10.0.3.2')

s6 = SwitchData('s6')
s6.addPort('s6-eth1', '00:00:00:00:06:01', '10.0.2.2')



switches = {}
for s in s1,s2,s3,s4,s5,s6:
    switches.update(s._to_serializable())
d = json.dumps(switches, sort_keys=True, indent=4, separators=(',', ': '))
sw = json.loads(d)
print(sw)

with open('network.json', 'w') as network_file:
    json.dump(switches, network_file, sort_keys=True, indent=4, separators=(',', ': '))

network = json.load(open('network.json', 'r'))

print(network)
