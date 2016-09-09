python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.1.2 32 set_nhop 10.0.1.2 3" -c 40.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.2.2 32 set_nhop 10.0.2.2 2" -c 40.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.5.1 32 set_nhop 10.0.5.1 1" -c 40.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.0.0 16 set_nhop 10.0.5.1 1" -c 40.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 1 rewrite_mac 00:00:00:00:03:01" -c 40.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 2 rewrite_mac 00:00:00:00:03:02" -c 40.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 3 rewrite_mac 00:00:00:00:03:03" -c 40.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 10.0.1.2 set_dmac 00:00:00:00:04:01" -c 40.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 10.0.2.2 set_dmac 00:00:00:00:06:01" -c 40.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 10.0.5.1 set_dmac 00:00:00:00:02:03" -c 40.0.0.106:22222
