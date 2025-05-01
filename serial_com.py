import serial.tools.list_ports

class SerialCtrl():
    def __init__(self):
        self.com_list=[]

    def getCOMlist(self):
        ports=serial.tools.list_ports.comports()
        self.com_list=[coms[0] for coms in ports]
        self.com_list.insert(0,"-")

    def SerialOpen(self):
        try:
            self.
        except:

    
if __name__=="__main__":
    SerialCtrl()