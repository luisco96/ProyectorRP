#Import
import RPi.GPIO as GPIO
import socket

#GPIO Variables
x=11
y=12

#UPD Variables
UDP_IP = "192.168.1.68"
UDP_PORT = 60500

#GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(x,GPIO.OUT)
GPIO.setup(y,GPIO.OUT)
pwmx=GPIO.PWM(x,50)
pwmy=GPIO.PWM(y,50)
pwmx.start(5.9)
pwmy.start(5.9)

#UDP initialization
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

def X(ax):
	a = (180-ax)/20.68
	pwmx.ChangeDutyCycle(a)

def Y(ay):
	a = (180-ay)/20.68
	pwmy.ChangeDutyCycle(a)

#Reveive Data
while True:
    data,addr = sock.recvfrom(1024)
    val = float(data)
    if(val == 1):
	data, addr = sock.recvfrom(1024)
        angulo = float(data)
        X(angulo)

    elif (val == 2):
        data, addr = sock.recvfrom(1024)
        angulo = float(data)
        Y(angulo)





