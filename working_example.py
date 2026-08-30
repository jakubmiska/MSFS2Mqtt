import sys
import json
import time

# CONFIG:SIMCONNECT_PATH
sys.path.append(
    r"C:\MSFSPythonSimConnectMobiFlightExtension\src"
)

from simconnect_mobiflight import SimConnectMobiFlight
from mobiflight_variable_requests import MobiFlightVariableRequests
import paho.mqtt.client as mqtt

# -----------------------
# MQTT
# -----------------------

# CONFIG:MQTT_BROKER
MQTT_BROKER = "192.168.1.150"

# CONFIG:MQTT_PORT
MQTT_PORT = "1883"

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
mqtt_client.loop_start()

# -----------------------
# HOME ASSISTANT DISCOVERY
# -----------------------

WARNING_CONFIG_TOPIC = (
    "homeassistant/binary_sensor/pmdg_master_warning/config"
)
WARNING_STATE_TOPIC = (
    "homeassistant/binary_sensor/pmdg_master_warning/state"
)

CAUTION_CONFIG_TOPIC = (
    "homeassistant/binary_sensor/pmdg_master_caution/config"
)
CAUTION_STATE_TOPIC = (
    "homeassistant/binary_sensor/pmdg_master_caution/state"
)

SPEEDBRAKE_CONFIG_TOPIC = (
    "homeassistant/binary_sensor/pmdg_speedbrake/config"
)
SPEEDBRAKE_STATE_TOPIC = (
    "homeassistant/binary_sensor/pmdg_speedbrake/state"
)

LGEARSAFE_CONFIG_TOPIC = (
    "homeassistant/binary_sensor/pmdg_lgearsafe/config"
)
LGEARSAFE_STATE_TOPIC = (
    "homeassistant/binary_sensor/pmdg_lgearsafe/state"
)

RGEARSAFE_CONFIG_TOPIC = (
    "homeassistant/binary_sensor/pmdg_rgearsafe/config"
)
RGEARSAFE_STATE_TOPIC = (
    "homeassistant/binary_sensor/pmdg_rgearsafe/state"
)

NGEARSAFE_CONFIG_TOPIC = (
    "homeassistant/binary_sensor/pmdg_ngearsafe/config"
)
NGEARSAFE_STATE_TOPIC = (
    "homeassistant/binary_sensor/pmdg_ngearsafe/state"
)

LGEARUNSAFE_CONFIG_TOPIC = (
    "homeassistant/binary_sensor/pmdg_lgearunsafe/config"
)
LGEARUNSAFE_STATE_TOPIC = (
    "homeassistant/binary_sensor/pmdg_lgearunsafe/state"
)

RGEARUNSAFE_CONFIG_TOPIC = (
    "homeassistant/binary_sensor/pmdg_rgearunsafe/config"
)
RGEARUNSAFE_STATE_TOPIC = (
    "homeassistant/binary_sensor/pmdg_rgearunsafe/state"
)

NGEARUNSAFE_CONFIG_TOPIC = (
    "homeassistant/binary_sensor/pmdg_ngearunsafe/config"
)
NGEARUNSAFE_STATE_TOPIC = (
    "homeassistant/binary_sensor/pmdg_ngearunsafe/state"
)

# NEW TOPIC DEFINITIONS AFTER THIS LINE



warning_discovery = {
    "name": "PMDG Master Warning",
    "unique_id": "pmdg_master_warning",
    "state_topic": WARNING_STATE_TOPIC,
    "payload_on": "ON",
    "payload_off": "OFF",
    "device": {
        "identifiers": ["pmdg_737_600"],
        "name": "PMDG 737-600",
        "manufacturer": "PMDG",
        "model": "737-600 NG"
    }
}

caution_discovery = {
    "name": "PMDG Master Caution",
    "unique_id": "pmdg_master_caution",
    "state_topic": CAUTION_STATE_TOPIC,
    "payload_on": "ON",
    "payload_off": "OFF",
    "device": {
        "identifiers": ["pmdg_737_600"],
        "name": "PMDG 737-600",
        "manufacturer": "PMDG",
        "model": "737-600 NG"
    }
}

speedbrake_discovery = {
    "name": "PMDG Speedbrake",
    "unique_id": "pmdg_speedbrake",
    "state_topic": SPEEDBRAKE_STATE_TOPIC,
    "payload_on": "ON",
    "payload_off": "OFF",
    "device": {
        "identifiers": ["pmdg_737_600"],
        "name": "PMDG 737-600",
        "manufacturer": "PMDG",
        "model": "737-600 NG"
    }
}

lgearsafe_discovery = {
    "name": "PMDG Left Gear Safe",
    "unique_id": "pmdg_lgearsafe",
    "state_topic": LGEARSAFE_STATE_TOPIC,
    "payload_on": "ON",
    "payload_off": "OFF",
    "device": {
        "identifiers": ["pmdg_737_600"],
        "name": "PMDG 737-600",
        "manufacturer": "PMDG",
        "model": "737-600 NG"
    }
}

rgearsafe_discovery = {
    "name": "PMDG Right Gear Safe",
    "unique_id": "pmdg_rgearsafe",
    "state_topic": RGEARSAFE_STATE_TOPIC,
    "payload_on": "ON",
    "payload_off": "OFF",
    "device": {
        "identifiers": ["pmdg_737_600"],
        "name": "PMDG 737-600",
        "manufacturer": "PMDG",
        "model": "737-600 NG"
    }
}

ngearsafe_discovery = {
    "name": "PMDG Nose Gear Safe",
    "unique_id": "pmdg_ngearsafe",
    "state_topic": NGEARSAFE_STATE_TOPIC,
    "payload_on": "ON",
    "payload_off": "OFF",
    "device": {
        "identifiers": ["pmdg_737_600"],
        "name": "PMDG 737-600",
        "manufacturer": "PMDG",
        "model": "737-600 NG"
    }
}

lgearunsafe_discovery = {
    "name": "PMDG Left Gear Unsafe",
    "unique_id": "pmdg_lgearunsafe",
    "state_topic": LGEARUNSAFE_STATE_TOPIC,
    "payload_on": "ON",
    "payload_off": "OFF",
    "device": {
        "identifiers": ["pmdg_737_600"],
        "name": "PMDG 737-600",
        "manufacturer": "PMDG",
        "model": "737-600 NG"
    }
}

rgearunsafe_discovery = {
    "name": "PMDG Right Gear Unsafe",
    "unique_id": "pmdg_rgearunsafe",
    "state_topic": RGEARUNSAFE_STATE_TOPIC,
    "payload_on": "ON",
    "payload_off": "OFF",
    "device": {
        "identifiers": ["pmdg_737_600"],
        "name": "PMDG 737-600",
        "manufacturer": "PMDG",
        "model": "737-600 NG"
    }
}

ngearunsafe_discovery = {
    "name": "PMDG Nose Gear Unsafe",
    "unique_id": "pmdg_ngearunsafe",
    "state_topic": NGEARUNSAFE_STATE_TOPIC,
    "payload_on": "ON",
    "payload_off": "OFF",
    "device": {
        "identifiers": ["pmdg_737_600"],
        "name": "PMDG 737-600",
        "manufacturer": "PMDG",
        "model": "737-600 NG"
    }
}

# NEW DISCOVERY DEFINITIONS AFTER THIS LINE



mqtt_client.publish(
    WARNING_CONFIG_TOPIC,
    json.dumps(warning_discovery),
    retain=True
)

mqtt_client.publish(
    CAUTION_CONFIG_TOPIC,
    json.dumps(caution_discovery),
    retain=True
)

mqtt_client.publish(
    SPEEDBRAKE_CONFIG_TOPIC,
    json.dumps(speedbrake_discovery),
    retain=True
)

mqtt_client.publish(
    LGEARSAFE_CONFIG_TOPIC,
    json.dumps(lgearsafe_discovery),
    retain=True
)

mqtt_client.publish(
    RGEARSAFE_CONFIG_TOPIC,
    json.dumps(rgearsafe_discovery),
    retain=True
)

mqtt_client.publish(
    NGEARSAFE_CONFIG_TOPIC,
    json.dumps(ngearsafe_discovery),
    retain=True
)

mqtt_client.publish(
    LGEARUNSAFE_CONFIG_TOPIC,
    json.dumps(lgearunsafe_discovery),
    retain=True
)

mqtt_client.publish(
    RGEARUNSAFE_CONFIG_TOPIC,
    json.dumps(rgearunsafe_discovery),
    retain=True
)

mqtt_client.publish(
    NGEARUNSAFE_CONFIG_TOPIC,
    json.dumps(ngearunsafe_discovery),
    retain=True
)

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
# PMDG L:Vars
# -----------------------

WARNING_LVAR = "(L:switch_3471_73X)"
CAUTION_LVAR = "(L:switch_3481_73X)"
SPEEDBRAKE_LVAR = "(L:switch_343_73X)"
LGEARSAFE_LVAR = "(L:switch_453_73X)"
RGEARSAFE_LVAR = "(L:switch_454_73X)"
NGEARSAFE_LVAR = "(L:switch_450_73X)"
LGEARUNSAFE_LVAR = "(L:switch_451_73X)"
RGEARUNSAFE_LVAR = "(L:switch_452_73X)"
NGEARUNSAFE_LVAR = "(L:switch_449_73X)"

# NEW LVARS AFTER THIS LINE



last_state = {
# NEW LASTSTATES AFTER THIS LINE
    "warning": None,
    "caution": None,
    "speedbrake": None,
    "lgearsafe": None,
    "rgearsafe": None,
    "ngearsafe": None,
    "lgearunsafe": None,
    "rgearunsafe": None,
    "ngearunsafe": None


}

while True:
    try:
# NEW ENTRIES AFTER THIS LINE
        warning = int(float(vr.get(WARNING_LVAR)))
        caution = int(float(vr.get(CAUTION_LVAR)))
        speedbrake = int(float(vr.get(SPEEDBRAKE_LVAR)))
        lgearsafe = int(float(vr.get(LGEARSAFE_LVAR)))
        rgearsafe = int(float(vr.get(RGEARSAFE_LVAR)))
        ngearsafe = int(float(vr.get(NGEARSAFE_LVAR)))
        lgearunsafe = int(float(vr.get(LGEARUNSAFE_LVAR)))
        rgearunsafe = int(float(vr.get(RGEARUNSAFE_LVAR)))
        ngearunsafe = int(float(vr.get(NGEARUNSAFE_LVAR)))

# END OF ENTRIES



        if warning != last_state["warning"]:
            mqtt_client.publish(
                WARNING_STATE_TOPIC,
                "ON" if warning else "OFF",
                retain=True
            )

            print(f"WARNING: {warning}")

            last_state["warning"] = warning

        if caution != last_state["caution"]:
            mqtt_client.publish(
                CAUTION_STATE_TOPIC,
                "ON" if caution else "OFF",
                retain=True
            )

            print(f"CAUTION: {caution}")

            last_state["caution"] = caution

        if speedbrake != last_state["speedbrake"]:
            mqtt_client.publish(
                SPEEDBRAKE_STATE_TOPIC,
                "ON" if speedbrake else "OFF",
                retain=True
            )

            print(f"SPEEDBRAKE: {speedbrake}")

            last_state["speedbrake"] = speedbrake

        if lgearsafe != last_state["lgearsafe"]:
            mqtt_client.publish(
                LGEARSAFE_STATE_TOPIC,
                "ON" if lgearsafe else "OFF",
                retain=True
            )

            print(f"LGEARSAFE: {lgearsafe}")

            last_state["lgearsafe"] = lgearsafe

        if rgearsafe != last_state["rgearsafe"]:
            mqtt_client.publish(
                RGEARSAFE_STATE_TOPIC,
                "ON" if rgearsafe else "OFF",
                retain=True
            )

            print(f"RGEARSAFE: {rgearsafe}")

            last_state["rgearsafe"] = rgearsafe

        if ngearsafe != last_state["ngearsafe"]:
            mqtt_client.publish(
                NGEARSAFE_STATE_TOPIC,
                "ON" if ngearsafe else "OFF",
                retain=True
            )

            print(f"NGEARSAFE: {ngearsafe}")

            last_state["ngearsafe"] = ngearsafe

        if lgearunsafe != last_state["lgearunsafe"]:
            mqtt_client.publish(
                LGEARUNSAFE_STATE_TOPIC,
                "ON" if lgearunsafe else "OFF",
                retain=True
            )

            print(f"LGEARUNSAFE: {lgearunsafe}")

            last_state["lgearunsafe"] = lgearunsafe

        if rgearunsafe != last_state["rgearunsafe"]:
            mqtt_client.publish(
                RGEARUNSAFE_STATE_TOPIC,
                "ON" if rgearunsafe else "OFF",
                retain=True
            )

            print(f"RGEARUNSAFE: {rgearunsafe}")

            last_state["rgearunsafe"] = rgearunsafe

        if ngearunsafe != last_state["ngearunsafe"]:
            mqtt_client.publish(
                NGEARUNSAFE_STATE_TOPIC,
                "ON" if ngearunsafe else "OFF",
                retain=True
            )

            print(f"NGEARUNSAFE: {ngearunsafe}")

            last_state["ngearunsafe"] = ngearunsafe

# NEW PROCEDURES AFTER THIS LINE



    except Exception as e:
        print(f"Error: {e}")

    time.sleep(0.5)
