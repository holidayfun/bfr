import sys

sys.path.insert(0, '/home/hartmann/p4factory/cli')

import pd_cli
sys_path = 'tests/pd_thrift:../../testutils'

sys.path.extend(sys_path.split(':'))

cli = pd_cli.PdCli(p4_name='bfr', thrift_module='p4_pd_rcp.bfr', thrift_server='40.0.0.104', port = 22224)


ip = '40.0.0.1'
port = 22224
