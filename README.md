# About
This is a project aiming to gather data from Microsoft Flight Simulator and pass it locally via MQTT to use with Home Assistant automations (for example - turn ambient light in room red when aircraft's alarm goes off, etc.). I created it since I was unable to find any existing simple and ready-to-use solution.

In essence it is a simple python script meant to run alongside MSFS. The additional app is only designed to help manage scripts (change basic MQTT config and add new entries) and is not required for the script itself to work.

The script is designed to work with MSFS2020, I didn't test it with MSFS2024, as I don't own the newer sim, therefore I can't confirm whether it works with it or not.

The script also relies on 3rd party python libraries and software that can be found online, I do not claim any rights to them. In case of those causing any problems, please reach to their respective owners/developers.

Please also keep in mind that I'm not a programmer/professional developer and I created this with a major help from AI just to combine my 2 hobbys, which are flight-simming and smart-home. I decided to share it in case anyone else finds this kind of utility helpful. Therefore:
* I do not take any responsibility for any outcome of downloading, modifying, using, sharing, etc.,
* no updates, bugfixes or any other maintenance efforts are to be expected. However, if you want to, feel free to modify and adjust anything to your needs and preferences.

# Usage
## Requirements
* MobiFlight
* MSFSPythonSimConnectMobiFlightExtension
* simconnect_mobiflight
* mobiflight_variable_requests
* paho.mqtt.client

(the above can be found on GitHub).
Plus, of course, MSFS, Home Assistant with MQTT integration and local MQTT broker running.

Simply download the template script from this repository and save it in a convenient location. Feel free to rename it after downloading.

## Config
You can either manually edit the script or use the optional app.

### App
Be sure to select the path to your script at the top of the window before any further action. 

Simply type your MQTT broker IP and port (only the numbers, eg. 127.0.0.1 - without protocols like http://) in appropriate fields and choose path to MSFSPythonSimConnectMobiFlightExtension\src catalogue, then hit Apply.

### Note
The app doesn't read config lines from your script, so upon selecting the path, the default values visible in app's fields won't change. That is normal and doesn't mean your script wasn't found or saved properly.

### Script
While editing the script itself please do not remove or modify comments.

Find the following lines:
* Ext_Path = r"C:\MSFSPythonSimConnectMobiFlightExtension\src"
* MQTT_BROKER = "127.0.0.1"
* MQTT_PORT = "1883"
change the values inside "" marks as needed and save.

## Adding new entries
### App
While path to your script still selected in the top bar, fill all the fields on "Add entry" tab and after that hit ADD button.
* UniqeID - ID for MQTT topics and HA sensors,
* EntryName - this is the name of the sensor that should be created inside of Home Assistant's MQTT integration - which you will then be able to use in automations,
* Data - MSFS variable to track (tested with LVars, other types probably also possible), 
* Home assistant device - details of the device that should be created inside of Home Assistant's MQTT integration. You can add multiple entities to the same device.

### Note
For now the app only supports creating binary sensors in HA, you can create other types of entities manually.

### Example
For PMDG 737-600 master warning indicator:
* UniqueID: pmdg_master_warning
* Name: PMDG Master Warning
* Data: L:switch_3471_73X
* Identifier: pmdg_737_600
* Name: PMDG 737-600
* Manufacturer: PMDG
* Model: 737-600 NG
That should, after launching the script, create a binary sensor inside HA, which changes as the master warning indicator goes off or is turned off. You can then use the sensor in automations.

## Editing and removing entries
The app only supports adding new entries. To edit or remove any existing ones you have to manually edit the script.

Each entry consists of several lines located in specific sections of the script. To remove an entry, simply delete all of the respective parts, as shown in the next section.

## Script example
The example entry, PMDG master warning, consists of the following parts:

### Home Assistant Discovery section
```
WARNING_CONFIG_TOPIC = (
    "homeassistant/binary_sensor/pmdg_master_warning/config"
)
WARNING_STATE_TOPIC = (
    "homeassistant/binary_sensor/pmdg_master_warning/state"
)
```

After all topics for other entries:

```
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
```

And after all of those lines for other entries:

```
mqtt_client.publish(
    WARNING_CONFIG_TOPIC,
    json.dumps(warning_discovery),
    retain=True
)
```

### LVARs section
```
WARNING_LVAR = "(L:switch_3471_73X)"
```

After all VARs for other entries, inside laststate = {
```
"warning": None,
```

After all last_states for other entries, inside while - try loop:
```
warning = int(float(vr.get(WARNING_LVAR)))
```

And then, after all of that:
```
if warning != last_state["warning"]:
            mqtt_client.publish(
                WARNING_STATE_TOPIC,
                "ON" if warning else "OFF",
                retain=True
            )

            print(f"WARNING: {warning}")

            last_state["warning"] = warning
```

So to remove an entry, you have to remove all of the above parts.

## Running
Once ready, launch MSFS, then the script. That's all.