#!/usr/bin/python

# Copyright 2013-present Barefoot Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.cli import CLI

from p4_mininet import P4Switch, P4Host

import argparse
from time import sleep

parser = argparse.ArgumentParser(description='Mininet demo')
parser.add_argument('--behavioral-exe', help='Path to behavioral executable',
                    type=str, action="store", required=True)
parser.add_argument('--thrift-port', help='Thrift server port for table updates',
                    type=int, action="store", default=22222)
parser.add_argument('--num-hosts', help='Number of hosts to connect to switch',
                    type=int, action="store", default=2)

args = parser.parse_args()

class BFR_Topo(Topo):
    """
    Example topology for a BIER Domain
     ( A ) ------------ (  B  ) ------------ ( C ) ------------ ( D )
    4 (0:1000)              \                  \            1 (0:0001)
                             \                  \
                             ( E )              ( F )
                           3 (0:0100)         2 (0:0010)
    """

    def __init__(self, sw_path, thrift_port, n, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)


def main():
    num_hosts = args.num_hosts
    sw_path = args.behavioral_exe
    thrift_port = args.thrift_port
    #print "Topo created"
    net = Mininet(host = P4Host,
                  switch = P4Switch,
                  controller = None )

    switch_names = ['A', 'B', 'C', 'D', 'E', 'F']
    name_to_nbr = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6}


    links = [['A', 'B'], ['B', 'E'], ['B', 'C'], ['C', 'D'], ['C', 'F']]

    switches = {}
    info( '*** Creating switches\n' )
    for name in switch_names:
        switches[name] = net.addSwitch("s%d" % name_to_nbr[name],
                                sw_path = sw_path,
                                thrift_port = thrift_port,
                                pcap_dump = True)
        #switches[name].setIP(ip = '192.1.1.%d' % name_to_nbr[name], intf='s'+str(name_to_nbr[name])+'-eth1')
	print(switches[name].intfList())
    #establish links
    info( '*** Creating links\n' )
    for link in links:
        net.addLink(switches[link[0]], switches[link[1]])

    net.start()

    sleep(1)

    print "Ready !"
    
    for name in switch_names:
	print "<<<<<<<<<" + name + ">>>>>>>>>>>>"
	print "interfaces: " + str(switches[name].intfNames())

    switches['A'].setIP('10.0.4.1', intf='s1-eth1')    
    switches['B'].setIP('10.0.4.2', intf='s2-eth1')    
    switches['B'].setIP('10.0.3.1', intf='s2-eth2')    
    switches['B'].setIP('10.0.5.1', intf='s2-eth3')    
    switches['C'].setIP('10.0.5.2', intf='s3-eth1')    
    switches['C'].setIP('10.0.1.1', intf='s3-eth2')    
    switches['C'].setIP('10.0.2.1', intf='s3-eth3')    
    switches['D'].setIP('10.0.1.2', intf='s4-eth1')    
    switches['E'].setIP('10.0.3.2', intf='s5-eth1') 
    switches['F'].setIP('10.0.2.2', intf='s6-eth1')    
    CLI( net )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'debug' )
    main()
