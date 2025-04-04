from enum import Enum

class SecurityDevice:
    def __init__(self, active):
        #print("init for SecurityDevice")
        self.active = active
    
    def reset(self):
       #print("Resetting...")
        self.active = True
    

class Sensor(SecurityDevice): #The class sensor is inheriting the properties of SecurityDevice.
    def __init__(self, silent, distance):
        self.silent = silent
        self.distance = distance

# security_device = SecurityDevice(True)
# print(security_device)

# sensor = Sensor(False, 30)
# print(sensor)
# sensor.reset()
# print(sensor.active)

# print(type(sensor))

# #isinstance for example mean is sensor a Sensor.
# print(isinstance(sensor, Sensor)) #sensor or SecurityDevice

# print(issubclass(Sensor, SecurityDevice))

class Position:
    def __init__(self, pan, tilt, zoom):
        self.pan = pan
        self.tilt = tilt
        self.zoom = zoom

    def __str__(self):
        return f"Pan: {str(self.pan)}. Tilt: {str(self.tilt)}. Zoom: {str(self.zoom)}."
    
    def __eq__(self, other):
        return self.pan == other.pan and self.tilt == other.tilt and self.zoom == other.zoom
    
    __hash__ = None

class Camera:
    def __init__(self, serial_number, position, camera_type):
        self.serial_number = serial_number
        self.position = position
        self.camera_type = camera_type
    
    def __str__(self):
        return f"Serial number: {self.serial_number}. Camera type: {self.camera_type}. " + self.position.__str__()
    
    def __eq__(self, other):
        return self.serial_number == other.serial_number and self.position == other.position and self.camera_type == other.camera_type
    
    __hash__ = None

    class cameraType(Enum):
        ptz = 0
        eptz = 1
        stationary = 2