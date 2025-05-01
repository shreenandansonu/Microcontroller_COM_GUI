from GUI_Master import RootGUI, ComGui
from serial_com import SerialCtrl 

myserial=SerialCtrl()
mastergui=RootGUI()
com_master=ComGui(mastergui.root,myserial)

mastergui.root.mainloop() 