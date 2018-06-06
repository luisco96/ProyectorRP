#import
import RPi.GPIO as GPIO
import socket

UDP_IP = ""
UDP_PORT = "60501"
#variables
x=11
y=12
xs=0
ys=90
yss=40

#setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(x,GPIO.OUT)
GPIO.setup(y,GPIO.OUT)
pwmx=GPIO.PWM(x,50)
pwmy=GPIO.PWM(y,50)
pwmx.start(5)
pwmy.start(2)

#UDP initialization
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
    data,addr = sock.recvfrom(1024)
    val = int.from_bytes(data)
    if(val == 1):
        data, addr = sock.recvfrom(1024)
        angulo = int.from_bytes(data)
        UP(angulo)
    
    else if (val == 2):
        data, addr = sock.recvfrom(1024)
        angulo = int.from_bytes(data)
        DOWN(angulo)

    else if (val == 3):
        data, addr = sock.recvfrom(1024)
        angulo = int.from_bytes(data)
        RIGHT(angulo)

    else if (val == 4):
        data, addr = sock.recvfrom(1024)
        angulo = int.from_bytes(data)
        UP(angulo)
        
        


#events
def UP(yss):
    global ys
    ys=9.0/180.*(yss+20)+2
    pwmy.ChangeDutyCycle(ys)
def DOWN():
    global ys
    ys=9.0/180.0*(yss-20)+2
    pwmy.ChangeDutyCycle(ys)




