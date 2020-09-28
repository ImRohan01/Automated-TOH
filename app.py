from ppadb.client import Client
import time


def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
    global device
    if n == 1: 
        print ("Move disk 1 from rod",from_rod,"to rod",to_rod)
        device.shell('input touchscreen swipe ' + from_rod + to_rod + '1000')
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print ("Move disk",n,"from rod",from_rod,"to rod",to_rod )
    device.shell('input touchscreen swipe ' + from_rod + to_rod + '1000')
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 


if __name__ == "__main__":
    adb = Client(host='127.0.0.1', port=5037)
    devices = adb.devices()

    if len(devices) == 0:
        print('no device attached')
        quit()

    device = devices[0]
    TowerOfHanoi(6,"180 2100 ", "900 2100 ", "540 2100 ")
