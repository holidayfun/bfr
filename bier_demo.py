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

        switch_names = ['A', 'B', 'C', 'D', 'E', 'F']

        links = [['A', 'B'], ['B', 'E'], ['B', 'C'], ['C', 'D'], ['C', 'F']]

        switches = {}

        for name in switch_names:
            switches[name] = self.addSwitch(name,
                                    sw_path = sw_path,
                                    thrift_port = thrift_port,
                                    pcap_dump = True)

        #establish links
        for link in links:
            self.addLink(switches[link[0]], switches[link[1]])



class SingleSwitchTopo(Topo):
    "Single switch connected to n (< 256) hosts."
    def __init__(self, sw_path, thrift_port, n, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        switch = self.addSwitch('s1',
                                sw_path = sw_path,
                                thrift_port = thrift_port,
                                pcap_dump = True)

        for h in xrange(n):
            host = self.addHost('h%d' % (h + 1),
                                ip = "10.0.%d.10/24" % h,
                                mac = '00:04:00:00:00:%02x' %h)

            self.addLink(host, switch)

def main():
    num_hosts = args.num_hosts

    topo = BFR_Topo(args.behavioral_exe,
                            args.thrift_port,
                            num_hosts
    )
    #print "Topo created"
    net = Mininet(topo = topo,
                  host = P4Host,
                  switch = P4Switch,
                  controller = None )
    #print "net created!"
    net.start()
    #print "net started"

    # sw_mac = ["00:aa:bb:00:00:%02x" % n for n in xrange(num_hosts)]
    #
    # sw_addr = ["10.0.%d.1" % n for n in xrange(num_hosts)]
    # 
    # for n in xrange(num_hosts):
    #     h = net.get('h%d' % (n + 1))
    #     h.setARP(sw_addr[n], sw_mac[n])
    #     h.setDefaultRoute("dev eth0 via %s" % sw_addr[n])
    #
    # for n in xrange(num_hosts):
    #     h = net.get('h%d' % (n + 1))
    #     h.describe()

    sleep(1)

    print "Ready !"

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'debug' )
    main()
