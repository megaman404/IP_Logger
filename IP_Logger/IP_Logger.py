import tkinter as tk
from pathlib import Path
import IP_Logger_Gui
import IP_Logger_Logic
import folders_sanity_check as folder_check

if __name__ == "__main__":
    print("Hello, Welcome to IP_Logger version 1.0")
    folder_check.check_folders()

    # init backend logic
    IPLogger = IP_Logger_Logic.IPLogger()
    
    # init frontend gui
    root = tk.Tk()
    myGui = IP_Logger_Gui.IPLogger_gui(root, IPLogger)

    # tkinter on standby
    root.mainloop()
    

    
