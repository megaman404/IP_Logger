import tkinter as tk
from datetime import datetime

def handle_enter(event):
    # 1. Grab what the user typed in the entry box
    user_text = text_entry.get()
    
    # 2. Get current time and format it
    now = datetime.now()
    
    # %H handles 00:00 (midnight) to 23:59, and 13:00 for 1 PM
    military_time = now.strftime("%H:%M")       
    
    # 3. Update the labels underneath
    result_label.config(text=f"You entered: {user_text}")
    time_label.config(text=f" Military Time: {military_time}")
    
    # 4. Clear the entry box
    text_entry.delete(0, tk.END)

# --- Setup the Main Window ---
root = tk.Tk()
root.title("Text & Time App")
root.geometry("420x260")

# Instruction label at the top
instruction_label = tk.Label(root, text="Type something and press Enter:", font=("Arial", 11))
instruction_label.pack(pady=15)

# Text entry input box
text_entry = tk.Entry(root, width=25, font=("Arial", 12))
text_entry.pack(pady=5)

# Bind the Enter key (<Return>) so it triggers our function automatically
text_entry.bind("<Return>", handle_enter)

# Result label underneath to display the user's text
result_label = tk.Label(root, text="", font=("Arial", 11, "bold"), fg="blue")
result_label.pack(pady=10)

# Time label underneath that to display normal and 24-hour military time
time_label = tk.Label(root, text="", font=("Arial", 10), fg="gray")
time_label.pack(pady=5)

# --- Run the Application ---
root.mainloop()
