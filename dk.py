import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT,initial = GPIO.LOW)

try:
  file=open("dkread.txt","r")
  file.close()
  file=open("dk.txt","r")
  file.close()
except:
  file=open("dkread.txt","w")
  file.close()
  file=open("dk.txt","w")
  file.close()

while True:

  time.sleep(1)
  file=open("/sys/bus/w1/devices/w1_bus_master1/w1_master_slaves","r")
  dkpas=file.readline()
  file.close()

  if str(dkpas) == 'not found.\n':
    time.sleep(1)
    continue
  else:
    file=open("/sys/bus/w1/devices/w1_bus_master1/w1_master_remove","a")
    file.write(str(dkpas))

  try:
    dkpas=dkpas[5:17]
  except:
    continue

  file=open("dkread.txt","r")
  dbkey=file.readlines()
  file.close()
  dkpas=str(dkpas)

  if dkpas in dbkey:
    pass
  else:
    file=open("dkread.txt","a")
    key=dkpas
    file.write(key)
    file.close()
    print "key added"

  file=open("dk.txt","r")
  akey=file.readlines()

  if dkpas in akey:
    print "acess granted for key: "+str(dkpas)
    GPIO.output(27,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(27,GPIO.LOW)

  else:
    print "acess dened for key: "+str(dkpas)
  
#end
  
