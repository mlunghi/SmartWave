from Adafruit_IO import Client
import time
aio = Client('KUNJD', 'ec48fa5e5a184569a2a7d56e5d26dc52')

count = 0

while True:
    data = aio.receive('microwave')

    count = 0

    item = str(data.value)

    if item.find("rice") >= 0 or item.find("Basmati") >= 0:
                print('Data value: White Rice' + '\nCooking Time = 12 minutes')
                count = 1
    elif item.find("Cookie") >= 0 or item.find("ball") >= 0 or item.find("Baking") >= 0:
                print('Data value: Cookies' + '\nCooking Time = 15 seconds')
                count = 1
    elif item.find("Dessert") >= 0 or item.find("Frozen") >= 0:
        print('Data value: Sandwich' + '\nCooking Time = 2 minutes')
    else:
        print("Food not identified")
            


    time.sleep(2)