import sys
import os


switch_number = 2
command = 'add_entry ipv4_lpm 10.0.3.2 32 set_nhop 10.0.3.2 2'
p4_name = 'bfr'
thrift_server = '40.0.0.{0}'.format(100 + 2 * switch_number)
thrift_client_module = "p4_pd_rpc.bfr"
thrift_port = 22222
create_entry_file = True

if create_entry_file:
    os.remove('entries_s{0}.bash'.format(switch_number))
    entry_file = open('entries_s{0}.bash'.format(switch_number), 'a')
else:
    sys.path.insert(0, '/home/hartmann/p4factory/cli')
    import pd_cli
    sys.path.append(os.getcwd())
    pwd = '/home/hartmann/p4factory/targets/bfr'
    sys_path = '{pwd}/tests/pd_thrift:{pwd}/../../testutils'.format(pwd = pwd)
    sys.path.extend(sys_path.split(":"))
    try:
        cli = pd_cli.PdCli(p4_name, thrift_client_module, thrift_server, thrift_port)
    except ImportError as ie:
        print >> sys.stderr, "ImportError:", ie
        sys.exit(1)

def handle_cmd(cmd):
    if create_entry_file:
        entry_file.write('python ../../cli/pd_cli.py -p {0} -i {1} -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "{2}" -c {3}:{4}\n'
                            .format(p4_name, thrift_client_module, cmd, thrift_server, thrift_port))
    else:
        cli.onecmd(cmd)

#adding IP lpm rules
entries = [ {'ip': '', 'prefix_len': 24, 'next_hop': ''},
            {'ip': '', 'prefix_len': 24, 'next_hop': ''},
            {'ip': '', 'prefix_len': 24, 'next_hop': ''},
            {'ip': '', 'prefix_len': 24, 'next_hop': ''}]
for entry in entries:
    handle_cmd("add_entry ipv4_lpm {entry[ip]} {entry[prefix_len]} set_nhop {entry[next_hop]}".format(entry=entry))

#adding Send Frame rules
entries = [ {'port': 1, 'rewrite_mac': '00:00:00:00:00:00'},
            {'port': 1, 'rewrite_mac': '00:00:00:00:00:00'},
            {'port': 1, 'rewrite_mac': '00:00:00:00:00:00'},
            {'port': 1, 'rewrite_mac': '00:00:00:00:00:00'}]
for entry in entries:
    handle_cmd("add_entry send_frame {entry[port]} rewrite_mac {entry[rewrite_mac]}".format(entry=entry))

#adding Forward rules
entries = [ {'ip': '', 'dmac': ''},
            {'ip': '', 'dmac': ''},
            {'ip': '', 'dmac': ''},
            {'ip': '', 'dmac': ''},
            {'ip': '', 'dmac': ''}]
for entry in entries:
    handle_cmd("add_entry forward {entry[ip]} set_dmac {entry[dmac]}".format(entry=entry))
