#!/usr/bin/python


from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.node import Node, Switch, Host, RemoteController
from p4_mininet import P4Switch, P4Host
import argparse
from time import sleep
import json


network = json.load(open('RingNetwork.json', 'r'))


def main(args):
    sw_path = args.behavioral_exe
    thrift_port = args.thrift_port
    topo = NetworkTopo(sw_path, thrift_port)


    net = OwnMininet(topo = topo, host= P4Host, switch=P4Router, controller=None)
    #adding host routes to controller to be able to connect to redis DB
    net_switches =[net.get(switch['name']) for switch in network['switches']]
    c0 = net.addController('c0', controller=InbandController)
    net.configureControlNetwork()
    for s in net_switches:
        s.setHostRoute('192.168.122.42', s.connectionsTo(c0)[0][0])

    net.start()
    
    for switch in network['switches']:
        net_switch = net.get(switch['name'])
        for host in switch['hosts']:
            net_host = net.get(host['name'])
            net_host.setARP(host['switch_addr'], host['switch_mac'])
            net_host.setDefaultRoute("dev eth0 via %s" % host['switch_addr'])

            link_to_switch = net_host.connectionsTo(net_switch)[0]
            net_switch.setMAC(host['switch_mac'], intf=link_to_switch[1])
            net_switch.setIP(host['switch_addr'], intf=link_to_switch[1])

    CLI(net)
    net.stop()

class InbandController(RemoteController):
    def checkListening(self):
	"Overridden to do nothing."
	return

class NetworkTopo(Topo):
    """generate the network topology"""
    def __init__(self, sw_path, thrift_port, **opts):
        Topo.__init__(self, **opts)

        for switch in network['switches']:
            s = self.addSwitch(switch['name'], sw_path=sw_path, thrift_port=thrift_port, pcap_dump = True, inNamespace = True)
            for host in switch['hosts']:
                h = self.addHost(host['name'], ip=host['ip'], mac=host['mac'])
                self.addLink(s, h)


        for link in network['switch_links']:
            self.addLink(link['node1']['name'], link['node2']['name'])

class OwnMininet(Mininet):
    def configureControlNetwork(self):
	info("configuring control network.")
	n = 0
	for controller in self.controllers:
	    for switch in self.switches:
	            sw_to_ctrl = self.addLink(switch,controller)
		    controller.setIP( '100.0.0.%s' % (100 + 2 * n + 1), intf=sw_to_ctrl.intf2)
		    switch.setIP(     '100.0.0.%s' % (100 + 2 * n + 2), intf=sw_to_ctrl.intf1)

		    controller.setMAC('00:00:00:0c:00:%02d' % (n + 1), intf=sw_to_ctrl.intf2)
		    switch.setMAC('00:00:00:0c:%02d:01' % (n + 1), intf=sw_to_ctrl.intf1)
        	    controller.setHostRoute('100.0.0.%s' % (100 + 2 * n + 2), sw_to_ctrl.intf2)
	            n += 1

class P4Router(P4Switch):
    """P4 virtual Router"""
    listenerPort = 11111
    dpidLen = 16
    #we pretend to not be a switch, so mininet assumes we are a host
    def defaultIntf(self):
        return Node.defaultIntf(self)

    def __init__( self, name, sw_path = "dc_full", dpid=None, opts='', thrift_port = 22222, pcap_dump = False, verbose = False, **kwargs ):
        P4Switch.__init__(self, name, **kwargs)
        self.dpid = self.defaultDpid(dpid)
        self.opts = opts
        self.sw_path = sw_path
        self.verbose = verbose
        self.logfile = '/tmp/p4ns.%s.log' % self.name
        self.output = open(self.logfile, 'w')
        self.thrift_port = thrift_port
        self.pcap_dump = pcap_dump

    def start( self, controllers ):
        "Start up a new P4 Router"
        args = [self.sw_path]
        args.extend( ['--name', self.name] )
        args.extend( ['--dpid', self.dpid] )
        for intf in self.intfs.values():
            if not intf.IP():
                args.extend( ['-i', intf.name] )
        args.extend( ['--listener', '192.168.122.42:%d' % self.listenerPort] )
        self.listenerPort += 1
        args.extend(['--pd-server', '40.0.0.{0}:{1}'.format(100 + 2 * int(self.dpid), self.thrift_port)] )
        args.extend( ['--p4nsdb', '192.168.122.42:6379'] )

        if not self.pcap_dump:
            args.append( '--no-cli' )
        args.append( self.opts )
        self.cmd(' '.join(args) + ' >' + self.logfile + ' 2>&1 </dev/null &' , verbose=True)

if __name__ == "__main__":
    setLogLevel('debug')
    parser = argparse.ArgumentParser(description='Mininet demo')
    parser.add_argument('--behavioral-exe', help='Path to behavioral executable', type=str, action="store", required=True)
    parser.add_argument('--thrift-port', help='Thrift server port for table updates', type=int, action="store", default=22222)
    args = parser.parse_args()

    main(args)
