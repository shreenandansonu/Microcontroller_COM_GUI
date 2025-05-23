import tkinter as tk
from tkinter import messagebox
from serial_com import SerialCtrl

c1 = "#FFFFFF"
c2 = "#C9ADA7"
c3 = "#9A8C98"
c4 = "#4A4E69"
c5 = "#22223B"


class RootGUI:
    def __init__(self,):

        self.root = tk.Tk()
        self.root.title("Serial Connection")
        self.root.geometry('360x230')
        self.root.config(bg=c1)
        self.root.iconbitmap("serial.ico")


class ComGui:
    def __init__(self, root,serial):
        self.serial=serial
        self.root = root
        self.frame = tk.LabelFrame(
            root, text="COM Manager", padx=5, pady=5, bg=c1)
        self.label_com = tk.Label(
            self.frame, text="COM Port(s)", bg=c1, width=10, anchor='w', padx=5, pady=5)
        self.label_baud = tk.Label (
            self.frame, text="Baud Rate", bg=c1, width=10, anchor='w')
        self.padx=20
        self.pady=5

        self.ComOptionMenu()
        self.BaudOptionMenu()

        self.butn_refresh=tk.Button(self.frame,text="Refresh",width=10,command=self.com_refresh)
        self.butn_connect=tk.Button(self.frame,text="Connect",width=10,state="disabled",command=self.serial_connect)


        self.publish()

    def ComOptionMenu(self):
        self.serial.getCOMlist()
        self.clicked_com = tk.StringVar()
        self.clicked_com.set(self.serial.com_list[0])
        self.drop_com = tk.OptionMenu(self.frame, self.clicked_com, *self.serial.com_list,command=self.connect_cntrl)
        self.drop_com.config(width=10)

    def BaudOptionMenu(self):
        bauds = ["-",
                "300","600","1200","2400","4800","9600","14400","19200","28800","38400","56000","57600","115200","128000","256000"]
        self.clicked_baud=tk.StringVar()
        self.clicked_baud.set(bauds[0])
        self.drop_baud=tk.OptionMenu(self.frame,self.clicked_baud,*bauds,command=self.connect_cntrl)
        self.drop_baud.config(width=10)

    def publish(self):
        self.frame.grid(column=0, row=0, columnspan=1,
                        rowspan=1, padx=5, pady=5)
        self.label_com.grid(column=0, row=1, columnspan=1, rowspan=1)
        self.label_baud.grid(column=0, row=2, columnspan=1, rowspan=1)
 
        self.drop_com.grid(column=1, row=1, columnspan=1, rowspan=1,padx=self.padx,pady=self.pady)
        self.drop_baud.grid(column=1,row=2,columnspan=1,rowspan=1)

        self.butn_refresh.grid(column=2, row=1, columnspan=1, rowspan=1,padx=self.padx,pady=self.pady)
        self.butn_connect.grid(column=2, row=2, columnspan=1)

    def com_refresh(self):
        # self.serial.getCOMlist()
        # print(self.serial.com_list)
        self.drop_com.destroy()
        self.ComOptionMenu()
        self.drop_com.grid(column=1, row=1, columnspan=1, rowspan=1,padx=self.padx,pady=self.pady)
        logic=""
        self.connect_cntrl(logic)


    def serial_connect(self):
        if self.butn_connect["text"] == "Connect":
            self.serial.SerialOpen(self)
            if self.serial.ser.status:
                self.butn_connect["text"]="Disconnect"
                self.butn_refresh["state"]="disabled"
                self.drop_baud["state"]="disabled"
                self.drop_com["state"]="disabled"
                infomessage=f"Successful UART connection using {self.clicked_com.get()}"
                messagebox.showinfo("Connection Established",infomessage)
                self.conn=ConnGUI(self.root,self.serial)
            else:
                errormessage=f"Failure to establish UART connection using {self.clicked_com.get()}"
                messagebox.showerror("Error Connecting",errormessage)
        else:
            self.serial.SerialClose()

            self.butn_connect["text"]="Connect"
            self.butn_refresh["state"]="active"
            self.drop_baud["state"]="active"
            self.drop_com["state"]="active"               
            print("Disconnected")
            self.butn_connect.config(text="Connect")
            infomessage=f"UART conncection using {self.clicked_com.get()} is now closed"
            messagebox.showinfo("Connection Closed",infomessage)

    def connect_cntrl(self,other):
        print("Connect")
        if "-" in self.clicked_com.get() or "-" in self.clicked_baud.get():
            self.butn_connect.config(state="disabled")
        else:
            self.butn_connect.config(state="active")

class ConnGUI():
    def __init__(self,root,serial):
        self.root=root
        self.serial=serial
        self.frame=tk.LabelFrame(root,text="Connection Manager",padx=5,pady=5,bg="white",width=60)
        self.sync_label=tk.Label(self.frame,text="Sync Status",bg='white',width=15,anchor='w')
        self.sync_status=tk.Label(self.frame,text="...sync...",bg='white',fg='orange',width=5)

        self.ConnGUIOpen()

    def ConnGUIOpen(self):
        self.root.geometry('800x120')
        self.frame.grid(row=0,column=4,rowspan=3,columnspan=5,padx=5,pady=5)
        self.sync_label.grid(row=1,column=1)
        self.sync_status.grid(row=1,column=2)






if __name__ == "__main__":
    RootGUI()
    ComGui()
    ConnGUI()
