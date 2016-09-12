echo "Entries for h2"
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry ipv4_lpm 10.0.2.3 32 set_nhop 10.0.2.3 1" -c 100.0.0.104:22222
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry forward 10.0.2.3 set_dmac 00:00:00:00:02:03" -c 100.0.0.104:22222
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry send_frame 1 rewrite_mac 00:aa:00:00:02:03" -c 100.0.0.104:22222
echo "Entries for h5"
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry ipv4_lpm 10.0.2.6 32 set_nhop 10.0.2.6 2" -c 100.0.0.104:22222
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry forward 10.0.2.6 set_dmac 00:00:00:00:02:06" -c 100.0.0.104:22222
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry send_frame 2 rewrite_mac 00:aa:00:00:02:06" -c 100.0.0.104:22222
echo "Entries for switch interconnects"
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry ipv4_lpm 10.0.1.0 24 set_nhop 20.0.0.1 3" -c 100.0.0.104:22222
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry forward 20.0.0.1 set_dmac 00:dd:00:00:00:01" -c 100.0.0.104:22222
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry send_frame 3 rewrite_mac 00:dd:00:00:00:02" -c 100.0.0.104:22222
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry ipv4_lpm 10.0.3.0 24 set_nhop 20.0.0.4 4" -c 100.0.0.104:22222
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry forward 20.0.0.4 set_dmac 00:dd:00:00:00:04" -c 100.0.0.104:22222
python ../../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/../tests/pd_thrift:$PWD/../../../testutils -m "add_entry send_frame 4 rewrite_mac 00:dd:00:00:00:03" -c 100.0.0.104:22222
