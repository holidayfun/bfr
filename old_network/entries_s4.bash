python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.1.1 32 set_nhop 10.0.1.1 1" -c 40.0.0.108:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.0.0 16 set_nhop 10.0.1.1 1" -c 40.0.0.108:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 1 rewrite_mac 00:00:00:00:04:01" -c 40.0.0.108:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 10.0.1.1 set_dmac 00:00:00:00:03:03" -c 40.0.0.108:22222
