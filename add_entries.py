import sys
import os
sys.path.insert(0, '/home/hartmann/p4factory/cli')

import pd_cli
#sys_path = 'tests/pd_thrift:../../testutils'

#sys.path.extend(sys_path.split(':'))

#sys_path = '../targets/bfr/tests/pd_thrift:../testutils'



#sys.path.extend(sys_path.split(':'))


pwd = '/home/hartmann/p4factory/targets/bfr'

sys.path.append(os.getcwd())
sys_path = '{pwd}/tests/pd_thrift:{pwd}/../../testutils'.format(pwd = pwd)

print(sys_path)

sys.path.extend(sys_path.split(":"))
thrift_server = '40.0.0.108'
port = 22224
using_default_thrift_server_port = True
thrift_client_module = "p4_pd_rpc.bfr"
using_default_thrift_client_module = True
command = 'add_entry ipv4_lpm 10.0.3.2 32 set_nhop 10.0.3.2 2'
p4_name = 'bfr'
try:
    cli = pd_cli.PdCli(p4_name, thrift_client_module, thrift_server, port)
except ImportError as ie:
    print >> sys.stderr, "ImportError:", ie
    sys.exit(1)

if command is None:
    cli.cmdloop()
else:
    cli.onecmd(command)
