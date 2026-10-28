import tkinter as tk
from pathlib import Path
import IP_Logger_Gui
import IP_Logger_Logic
import folders_sanity_check as folder_check
from datetime import datetime as dt

def get_military_time() -> str:
    todays_time = dt.now()
    todays_date = dt.today()
    return todays_time.strftime("%H%M")

def get_report_name() -> str:
    todays_date = dt.today()
    return f"END-OF-SHIFT-REPORT-TIMESHEET_{todays_date.year}-{todays_date.month}-{todays_date.day}.txt"

def file_existence() -> None:
    pass

if __name__ == "__main__":
    print("Hello, Welcome to IP_Logger version 1.0")
    folder_check.check_folders()
    
    # init backend logic
    IPLogger = IP_Logger_Logic.IPLogger()
    
    # init frontend gui
    root = tk.Tk()
    myGui = IP_Logger_Gui.IPLogger_gui(root, IPLogger)
    IPLogger.myGui = myGui
    
    # tkinter on standby
    root.mainloop()
    

    
