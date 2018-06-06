from tkinter import *
from tkinter import ttk
import socket

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title("Control")
        self.root.geometry('200x500')
        #self.pack()
        self.servo1 = IntVar()
        self.servo2 = IntVar()
        self.UDP_IP = "10.4.63.123"
        self.UDP_PORT = 60500
    

        self.etiq1 = ttk.Label(self.root, text = "Control de Servos")
        self.etiq2 = ttk.Label(self.root, text = "Arriba Abajo")
        self.etiq3 = ttk.Label(self.root, text = "Derecha Izquierda")
        self.etiq4 = ttk.Label(self.root, text = "Value = ")
        self.etiq5 = ttk.Label(self.root, text = "Value = ")
        self.aa = ttk.Scale(self.root, variable = self.servo1, from_ = 0, to = 180,
                            orient = VERTICAL, command = self.Value1)
        self.di = ttk.Scale(self.root, variable = self.servo2, from_ = 0, to = 180,
                            command = self.Value2)

        self.etiq1.pack(side ="top", fill = BOTH, expand = True, padx = 10, pady = 0)
        self.etiq2.pack(side ="top", fill = BOTH, expand = True, padx = 10, pady = 5)
        self.aa.pack(side = "top", fill =BOTH, expand = True, padx = 10, pady = 10)
        self.etiq4.pack(side ="top", fill = BOTH, expand = True, padx = 10, pady = 12)
        self.etiq3.pack(side ="top", fill = BOTH, expand = True, padx = 10, pady = 15)
        self.di.pack(side = "top", fill =BOTH, expand = True, padx = 10, pady = 20)
        self.etiq5.pack(side ="top", fill = BOTH, expand = True, padx = 10, pady = 22)

        self.quit = ttk.Button(self.root, text="QUIT",
                              command=self.root.destroy)
        self.quit.pack(side="bottom")
        self.root.mainloop()

    def Value1(self,val):
        selection = "Value = " +(val)
        self.etiq4.config(text = selection)
        angulo = str.encode(val)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(angulo, (self.UDP_IP, self.UDP_PORT))

    def Value2 (self,val):
        selection = "Value = " + str(val)
        self.etiq5.config(text = selection)

        
    #def say_hi(self):
     #   print("hi there, everyone!")

    #def slider(self):
         
def main():
    mi_app = Application()
    return 0

if __name__ == '__main__':

    main()
