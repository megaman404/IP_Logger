import tkinter as tk
from datetime import datetime
import IP_Logger_Gui
from pathlib import Path


class IPLogger:
    """ <class IPLogger> handles the backend for creating graphs and reports using tkinter and txt files """ 
    def __init__(self):
        self.user_input = ""
        self.current_directory = Path(__file__).parent.absolute()

    def handle_enter(self, user_input: tkinter.Entry) -> None:
        """ onEnter <class IPLogger> takes tkinter entry as a string to append to txt file"""
        
        reports = self.current_directory / "Reports" / "file.txt"
        print(reports)
        reports.touch()
        with reports.open("a", encoding="utf-8") as f:
            f.write(user_input + "\n")
    
