# -*- coding: utf-8 -*-
from modules.core.basetypes import Sensor
from modules.core.core import cbpi

@cbpi.addon.sensor.type("System Temp Sensor")
class SystemTemp(Sensor):

    def init(self):

        if self.api.get_config_parameter("unit","C") == "C":
            self.unit = "°C"
        else:
            self.unit = "°F"

    def execute(self):
        while True:
            try:
                self.update_value(int(self.text))
            except:
                pass
            self.api.sleep(1)

    def fetch_system_temp(self):
        try:
            res = os.popen('vcgencmd measure_temp').readline()
            temp = float(res.replace("temp=","").replace("'C\n",""))
            if self.unit == "°C":
                return round(temp, 2)
            else:
                return round(9.0 / 5.0 * temp + 32, 2)
        except:
            pass
