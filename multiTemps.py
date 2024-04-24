import os
import glob
import time
os.system('sudo modprobe w1-gpio')
os.system('sudo modprobe w1-therm')
try:
    while(True):
        list=os.listdir("/sys/bus/w1/devices/")
        list.remove("w1_bus_master1")
        file_count = len(list)
        i=0
        while i<file_count:
            if(i==0):    print('Número de Sensores: ' + str(file_count) + "\n")
            print('Sensor número: ' + str(i+1))
            ruta=glob.glob('/sys/bus/w1/devices/' + '28*')[i]
            if (os.path.exists(ruta) == True):
                fSensor=open(ruta + '/w1_slave')
                linSensor = fSensor.readlines()
                fSensor.close()
                if len(linSensor)==0:
                    print ("Sensor " + str(i+1) + " desconectado...")
                    i=file_count
                    time.sleep(110)
                    break
                else:
                    posTemp=linSensor[1].find('t=')
                    if posTemp != -1:  
                        strTemp=linSensor[1][posTemp+2:]
                        temp=float(strTemp) / 1000.0
                        print (list[i])
                        print (str(temp) + "ºC")
                        i=i+1
                        print("\n")
        time.sleep(5)
except IndexError:
    print("Error de lectura")
    os.system('sudo reboot')