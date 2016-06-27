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
from mininet.node import Node

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

    def __init__(self, sw_path, thrift_port, **opts):
        # Initialize topology and default options
        # Each BFR listens on a different Thrift port
        # A-F listen on Port thrift_port + {1-6}
        Topo.__init__(self, **opts)

        bfr_names = ['A', 'B', 'C', 'D', 'E', 'F']
        name_to_dpid = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6}
        bfrs = {}
        info( '*** Creating BFRs\n' )
        for name in bfr_names:
            bfrs[name] = self.addSwitch("n%d" % name_to_dpid[name],
                                    sw_path = sw_path,
                                    thrift_port = thrift_port + name_to_dpid[name],
                                    pcap_dump = True)

        info( '*** Creating links\n' )
        links = [['A', 'B'], ['B', 'E'], ['B', 'C'], ['C', 'D'], ['C', 'F']]
        for link in links:
            self.addLink(bfrs[link[0]], bfrs[link[1]])
	print(self.nodeInfo(bfrs['A']))
    print(self.nodes())
	print(self.g.node['n1'])
	info( '*** Assigning IPs\n' )
        #bfrs['A'].setIP('10.0.4.1', intf='s1-eth1')
        #bfrs['B'].setIP('10.0.4.2', intf='s2-eth1')
        #bfrs['B'].setIP('10.0.3.1', intf='s2-eth2')
        #bfrs['B'].setIP('10.0.5.1', intf='s2-eth3')
        #bfrs['C'].setIP('10.0.5.2', intf='s3-eth1')
        #bfrs['C'].setIP('10.0.1.1', intf='s3-eth2')
        #bfrs['C'].setIP('10.0.2.1', intf='s3-eth3')
        #bfrs['D'].setIP('10.0.1.2', intf='s4-eth1')
        #bfrs['E'].setIP('10.0.3.2', intf='s5-eth1')
        #bfrs['F'].setIP('10.0.2.2', intf='s6-eth1')


def main():
    num_hosts = args.num_hosts
    sw_path = args.behavioral_exe
    thrift_port = args.thrift_port

    topo = BFR_Topo(sw_path, thrift_port)
    net = Mininet(topo = topo, switch=P4Router)
    net.start()
    print(net.get('n1'))
    # switch_names = ['A', 'B', 'C', 'D', 'E', 'F']
    # name_to_nbr = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6}
    #
    #
    # links = [['A', 'B'], ['B', 'E'], ['B', 'C'], ['C', 'D'], ['C', 'F']]
    #
    # switches = {}
    # info( '*** Creating switches\n' )
    # for name in switch_names:
    #     switches[name] = net.addSwitch("s%d" % name_to_nbr[name],
    #                             sw_path = sw_path,
    #                             thrift_port = thrift_port,
    #                             pcap_dump = True,
    #                             cls = P4Router)
    #     #switches[name].setIP(ip = '192.1.1.%d' % name_to_nbr[name], intf='s'+str(name_to_nbr[name])+'-eth1')
    # print(switches[name].intfList())
    # #establish links
    # info( '*** Creating links\n' )
    # for link in links:
    #     net.addLink(switches[link[0]], switches[link[1]])
    #
    # sleep(1)
    #
    # print "Ready !"
    #
    # for name in switch_names:
    # print "<<<<<<<<<" + name + ">>>>>>>>>>>>"
    # print "interfaces: " + str(switches[name].intfNames())
    #
    # switches['A'].setIP('10.0.4.1', intf='s1-eth1')
    # switches['B'].setIP('10.0.4.2', intf='s2-eth1')
    # switches['B'].setIP('10.0.3.1', intf='s2-eth2')
    # switches['B'].setIP('10.0.5.1', intf='s2-eth3')
    # switches['C'].setIP('10.0.5.2', intf='s3-eth1')
    # switches['C'].setIP('10.0.1.1', intf='s3-eth2')
    # switches['C'].setIP('10.0.2.1', intf='s3-eth3')
    # switches['D'].setIP('10.0.1.2', intf='s4-eth1')
    # switches['E'].setIP('10.0.3.2', intf='s5-eth1')
    # switches['F'].setIP('10.0.2.2', intf='s6-eth1')
    CLI( net )
    net.stop()


class P4Router(Node):
    """P4 virtual Router"""
    listenerPort = 11111
    thriftPort = 22222

    def __init__( self, name, sw_path = "dc_full",
		  dpid=None,
                  thrift_port = None,
                  pcap_dump = False,
                  verbose = False, **kwargs ):
        Node.__init__( self, name, **kwargs )
        self.dpid = self.defaultDpid(dpid)
	self.sw_path = sw_path
        self.verbose = verbose
        logfile = '/tmp/p4ns.%s.log' % self.name
        self.output = open(logfile, 'w')
        self.thrift_port = thrift_port
        self.pcap_dump = pcap_dump

    def defaultDpid(self, dpid=None):
        "Return correctly formatted dpid from dpid or switch name (s1 -> 1)"
        if dpid:
            # Remove any colons and make sure it's a good hex number
            dpid = dpid.translate( None, ':' )
            assert len( dpid ) <= self.dpidLen and int( dpid, 16 ) >= 0
        else:
            # Use hex of the first number in the switch name
            nums = re.findall( r'\d+', self.name )
            if nums:
                dpid = hex( int( nums[ 0 ] ) )[ 2: ]
            else:
                raise Exception( 'Unable to derive default datapath ID - '
                                 'please either specify a dpid or use a '
                                 'canonical switch name such as s23.' )
        return '0' * ( self.dpidLen - len( dpid ) ) + dpid
    @classmethod
    def setup( cls ):
        pass

    def start( self, controllers ):
        "Start up a new P4 Router"
        print "Starting P4 Router", self.name
        args = [self.sw_path]
        args.extend( ['--name', self.name] )
        args.extend( ['--dpid', self.dpid] )
        for intf in self.intfs.values():
            if not intf.IP():
                args.extend( ['-i', intf.name] )
        args.extend( ['--listener', '127.0.0.1:%d' % self.listenerPort] )
        self.listenerPort += 1
        # FIXME
        if self.thrift_port:
            thrift_port = self.thrift_port
        else:
            thrift_port =  self.thriftPort
            self.thriftPort += 1
        args.extend( ['--pd-server', '127.0.0.1:%d' % thrift_port] )
        if not self.pcap_dump:
            args.append( '--no-cli' )
        args.append( self.opts )

        logfile = '/tmp/p4ns.%s.log' % self.name

        print ' '.join(args)

        self.cmd( ' '.join(args) + ' >' + logfile + ' 2>&1 </dev/null &' )
        #self.cmd( ' '.join(args) + ' > /dev/null 2>&1 < /dev/null &' )

        print "Router has been started"

    def stop( self ):
        "Terminate IVS switch."
        self.output.flush()
        self.cmd( 'kill %' + self.sw_path )
        self.cmd( 'wait' )
        self.deleteIntfs()

    def attach( self, intf ):
        "Connect a data port"
        print "Connecting data port", intf, "to switch", self.name
        self.cmd( 'p4ns-ctl', 'add-port', '--datapath', self.name, intf )

    def detach( self, intf ):
        "Disconnect a data port"
        self.cmd( 'p4ns-ctl', 'del-port', '--datapath', self.name, intf )

    def dpctl( self, *args ):
        "Run dpctl command"
        pass





if __name__ == '__main__':
    setLogLevel( 'debug' )
    main()
