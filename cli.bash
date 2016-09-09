#startet eine interaktive CLI Instanz
#read -p "IP, auf die verbunden werden soll: " ip
#read -p "Thrift Port, auf den verbunden werden soll: " port
typeset -i sw_number
typeset -i t
read -p "Switch, auf den verbunden werden soll: " sw_number

t=100+2*$sw_number
ip="100.0.0.$t"
port=22222

echo "Verbinde zu $ip:$port"

python ../../cli/pd_cli.py -p bfr -i p4_pd_rpc.bfr -s $PWD/tests/pd_thrift:$PWD/../../testutils -c $ip:$port "$@"
