echo "Entries for h1"
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.1.2 32 set_nhop 10.0.1.2 1" -c 100.0.0.102:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 10.0.1.2 set_dmac 10.0.1.2" -c 100.0.0.102:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 1 rewrite_mac 00:aa:00:00:01:02" -c 100.0.0.102:22222
echo "Entries for h4"
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.1.5 32 set_nhop 10.0.1.5 2" -c 100.0.0.102:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 10.0.1.5 set_dmac 10.0.1.5" -c 100.0.0.102:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 2 rewrite_mac 00:aa:00:00:01:05" -c 100.0.0.102:22222
echo "Entries for switch interconnects"
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.2.0 24 set_nhop 20.0.0.2 3" -c 100.0.0.102:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 20.0.0.2 set_dmac 00:dd:00:00:00:02" -c 100.0.0.102:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 3 rewrite_mac 00:dd:00:00:00:01" -c 100.0.0.102:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry ipv4_lpm 10.0.3.0 24 set_nhop 20.0.0.5 4" -c 100.0.0.102:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry forward 20.0.0.5 set_dmac 00:dd:00:00:00:05" -c 100.0.0.102:22222
python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -m "add_entry send_frame 4 rewrite_mac 00:dd:00:00:00:06" -c 100.0.0.102:22222
