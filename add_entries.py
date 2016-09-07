import sys
import os
sys.path.insert(0, '/home/hartmann/p4factory/cli')
import pd_cli

switch_number = 2
command = 'add_entry ipv4_lpm 10.0.3.2 32 set_nhop 10.0.3.2 2'
p4_name = 'bfr'
thrift_server = '40.0.0.{0}'.format(100 + 2 * switch_number)
port = 22222

sys.path.append(os.getcwd())
pwd = '/home/hartmann/p4factory/targets/bfr'
sys_path = '{pwd}/tests/pd_thrift:{pwd}/../../testutils'.format(pwd = pwd)
sys.path.extend(sys_path.split(":"))
thrift_client_module = "p4_pd_rpc.bfr"
try:
    cli = pd_cli.PdCli(p4_name, thrift_client_module, thrift_server, port)
except ImportError as ie:
    print >> sys.stderr, "ImportError:", ie
    sys.exit(1)

if command is None:
    cli.cmdloop()
else:
    cli.onecmd(command)
