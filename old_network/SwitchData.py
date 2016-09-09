import json
class SwitchData:
    @staticmethod
    def _from_dict(dict):
        s = SwitchData(dict.keys()[0])
        for key, value in dict[s.name].items():
            s.addPort(key, value['mac'], value['ip'])
        return s
    @staticmethod
    def from_json(json_string):
        return SwitchData._from_dict(json.loads(json_string))

    def __init__(self, name):
        self.name = name
        self.ports = {}
        pass
    def addPort(self, name, mac, ip):
        self.ports[name] = {'mac': mac, 'ip': ip}
    def __str__(self):
        return "{0}: {1}".format(self.name, self.ports)
    def _to_serializable(self):
        return {self.name : self.ports}
    def to_json(self):
        return json.dumps(self._to_serializable())

if __name__ == "__main__":
    s = SwitchData('s1')
    s.addPort('s1-eth1', '00:00:00:00:00:00', '10.0.4.1')
    s.addPort('s1-eth2', '00:00:00:00:00:00', '10.0.4.1')

    print(SwitchData.from_json(s.to_json()))
