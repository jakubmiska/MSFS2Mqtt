# Do NOT remove or alter comments
import sys
import json
import time

# CONFIG:SIMCONNECT_PATH
Ext_Path = r"C:\MSFSPythonSimConnectMobiFlightExtension\src"
sys.path.append(Ext_Path)

from simconnect_mobiflight import SimConnectMobiFlight
from mobiflight_variable_requests import MobiFlightVariableRequests
import paho.mqtt.client as mqtt

# -----------------------
# MQTT
# -----------------------

# CONFIG:MQTT_BROKER
MQTT_BROKER = "127.0.0.1"

# CONFIG:MQTT_PORT
MQTT_PORT = "1883"

mqtt_client = mqtt.Client()

mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
mqtt_client.loop_start()

# -----------------------
# HOME ASSISTANT DISCOVERY
# -----------------------

# NEW TOPIC DEFINITIONS AFTER THIS LINE



# NEW DISCOVERY DEFINITIONS AFTER THIS LINE



# NEW DISCOVERY PROCEDURES AFTER THIS LINE



print("Published Home Assistant discovery")

# -----------------------
# SIMCONNECT + MOBIFLIGHT
# -----------------------

sm = SimConnectMobiFlight()
vr = MobiFlightVariableRequests(sm)
vr.clear_sim_variables()

print("Connected to MSFS via MobiFlight WASM")

# -----------------------
# L:Vars
# -----------------------



# NEW LVARS AFTER THIS LINE



last_state = {
# NEW LASTSTATES AFTER THIS LINE
    
    "placeholder": None
}

while True:
    try:
# NEW ENTRIES AFTER THIS LINE
              


# END OF ENTRIES

# NEW PROCEDURES AFTER THIS LINE

       

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(0.5)
