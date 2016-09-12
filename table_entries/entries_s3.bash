echo "Entries for h3"
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.3.4 32 set_nhop 10.0.3.4 1" -c 100.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 10.0.3.4 set_dmac 10.0.3.4" -c 100.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 1 rewrite_mac 00:aa:00:00:03:04" -c 100.0.0.106:22222
echo "Entries for h6"
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.3.7 32 set_nhop 10.0.3.7 2" -c 100.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 10.0.3.7 set_dmac 10.0.3.7" -c 100.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 2 rewrite_mac 00:aa:00:00:03:07" -c 100.0.0.106:22222
echo "Entries for switch interconnects"
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.2.0 24 set_nhop 20.0.0.3 3" -c 100.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 20.0.0.3 set_dmac 00:dd:00:00:00:03" -c 100.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 3 rewrite_mac 00:dd:00:00:00:04" -c 100.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.1.0 24 set_nhop 20.0.0.6 4" -c 100.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 20.0.0.6 set_dmac 00:dd:00:00:00:06" -c 100.0.0.106:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 4 rewrite_mac 00:dd:00:00:00:05" -c 100.0.0.106:22222
