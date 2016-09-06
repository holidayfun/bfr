#startet eine interaktive CLI Instanz
read -p "IP, auf die verbunden werden soll: " ip
read -p "Thrift Port, auf den verbunden werden soll: " port

python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -c $ip:$port "$@"
