import evdev
import sys

class ps3ev:
    DEVICE_NAME="Sony PLAYSTATION"
    BTN_SELECT=288
    BTN_THUMBL=BTN_SELECT+1
    BTN_THUMBR=BTN_SELECT+2
    BTN_START=BTN_SELECT+3
    BTN_UP=BTN_SELECT+4
    BTN_RIGHT=BTN_SELECT+5
    BTN_DOWN=BTN_SELECT+6
    BTN_LEFT=BTN_SELECT+7
    BTN_TL=BTN_SELECT+8
    BTN_TR=BTN_SELECT+9
    BTN_TL2=BTN_SELECT+10
    BTN_TR2=BTN_SELECT+11
    BTN_X=BTN_SELECT+12
    BTN_A=BTN_SELECT+13
    BTN_B=BTN_SELECT+14
    BTN_Y=BTN_SELECT+15
    BTN_MODE=BTN_SELECT+16

    VAL_PRESSED=1
    VAL_RELEASE=0

    @staticmethod
    def printEvCode(code):
        if code==ps3ev.BTN_START:
            print "BTN_START"
        elif code==ps3ev.BTN_THUMBL:
            print "BTN_THUMBL"
        elif code==ps3ev.BTN_THUMBR:
            print "BTN_THUMBR"
        elif code==ps3ev.BTN_RIGHT:
            print "BTN_RIGHT"
        elif code==ps3ev.BTN_LEFT:
            print "BTN_LEFT"
        elif code==ps3ev.BTN_DOWN:
            print "BTN_DOWN"
        elif code==ps3ev.BTN_UP:
            print "BTN_UP"
        elif code==ps3ev.BTN_X:
            print "BTN_X"
        elif code==ps3ev.BTN_A:
            print "BTN_A"
        elif code==ps3ev.BTN_B:
            print "BTN_B"
        elif code==ps3ev.BTN_Y:
            print "BTN_Y"
        elif code==ps3ev.BTN_MODE:
            print "BTN_MODE"
        else:
            print "no code"

    @staticmethod
    def finddevice():
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        for device in devices:
            if device.name.startswith(ps3ev.DEVICE_NAME):
                return device
        return None


if __name__ == '__main__':
    device = ps3ev.finddevice()
    
    if device == None:
        print("PS3 controler not plugged")
        sys.exit()
    
    print "wait event from:", device.name
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_KEY and event.value == ps3ev.VAL_PRESSED:
            print(event)
            ps3ev.printEvCode(event.code)

