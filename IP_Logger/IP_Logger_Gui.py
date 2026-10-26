import tkinter as tk
from datetime import datetime
import IP_Logger_Logic
import re

class IPLogger_gui:
    """ <class IPLogger_gui> displays tkinter window/widgets and calls <class IPLogger_Logger> for backend processes """
    def __init__(self, root: tkinter, logic: IP_Logger_Logic.IPLogger) -> None:
        print("i was initied")
        # init Window
        self.root = root
        self.root.title("IP Logger App")
        self.root.geometry("400x200")
        self.root.minsize(400, 200)
        self.root.maxsize(400,200)
        self.logic = logic

        # init Instructions
        self.instruction_label = tk.Label(root, text = "Type Radio IP and press Enter:", font = ("Arial", 11))
        self.instruction_label.pack()

        # init Entry Box
        self.text_entry = tk.Entry(root, width = 25, font = ("Arial", 12))

        self.text_entry.pack(pady = 5)
        self.text_entry.bind("<Return>", self.gui_handle_enter)

        # init Feedback Dialog
        self.result_label = tk.Label(root, text = "", font = ("Arial", 11, "bold"))
        self.result_label.pack(pady = 10)

        # init Military Dialog
        self.time_label = tk.Label(root, text = "", font = ("Arial", 10), fg = "gray")
        self.time_label.pack(pady = 5)

    def gui_handle_enter(self, event: tkinter.Event) -> None:
        """ onEnter bind, display red for invalid inputs, display green for valid inputs, and display time """
        user_text = self.text_entry.get().strip().replace(" ", "")
        
        now = datetime.now()
        military_time = now.strftime("%H:%M")      
        self.time_label.config(text = f"Military Time: {military_time}")

        # regex rules
        format_rule = r"^\d+(?:\.\d+){3}$"
        invalid_chars = re.findall(r"[^0-9.]", user_text)

        # check correct syntax
        if not user_text:
            self.result_label.config(text = "Please Enter a Valid IP", fg = "red")
            self.text_entry.delete(0, tk.END)
        elif invalid_chars:
            self.result_label.config(text = f"Only numbers and periods are valid  \nUser_Input: {user_text}", fg = "red")
            self.text_entry.delete(0, tk.END)
        elif not re.match(format_rule, user_text):
            self.result_label.config(text = f"Incorrect format, please input: X.X.X.X \nUser_Input: {user_text}", fg = "red")
            self.text_entry.delete(0, tk.END)            
        else:
            self.result_label.config(text = f"You entered: {user_text}", fg = "green")
            self.text_entry.delete(0, tk.END)

            # start IP_Logger logic
            self.logic.handle_enter(user_text)
        
