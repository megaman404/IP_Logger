import tkinter as tk
import IP_Logger_Gui
from pathlib import Path
import IP_Logger as myApp
from datetime import datetime as dt


class IPLogger:
    """ <class IPLogger> handles the backend for creating graphs and reports using tkinter and txt files """ 
    def __init__(self):
        self.user_input = ""
        self.current_directory = Path(__file__).parent.absolute()
        self.report_dictionary = dict(
        {"0000-0100": [],"0100-0200": [],"0200-0300": [],"0300-0400": [],"0400-0500": [],"0500-0600": [],
         "0600-0700": [],"0700-0800": [],"0800-0900": [],"0900-1000": [],"1000-1100": [],"1100-2000": [],
         "1200-1300": [],"1300-1400": [],"1400-1500": [],"1500-1600": [],"1600-1700": [],"1700-1800": [],
         "1800-1900": [],"1900-2000": [],"2000-2100": [],"2100-2200": [],"2200-2300": [],"2300-2400": []})

    def handle_enter(self, user_input: tkinter.Entry) -> None:
        """ onEnter <class IPLogger.handle_enter> takes tkinter entry as a string to append to txt file"""
        
        for k,v in self.report_dictionary.items():
            print("hello", k[-4:])
            if int(myApp.get_military_time()) < int(k[-4:]):
                self.report_dictionary[k].append(user_input)
                break
        for k,v in self.report_dictionary.items():
            print(k,v)
        
    def export_report(self) -> None:
        """ <class IPLogger.export_report> handles backend to export dictionary into file """
        print("exporting report file")
        file_name = myApp.get_report_name()
        print(file_name)
        reports = self.current_directory / "Reports" / f"{file_name}"
        reports.touch()

        with reports.open(mode='w') as f:
            for k,v in self.report_dictionary.items():
                f.write(f"{k}\n")
                for i in v:
                    f.write(f"{i}\n")
                f.write("\n")
                
    def save_file(self) -> None:
        """ <IPLogger.save_file> saves report and graph files and puts it into a history folder """
        print("Saving files....")
        saves_path = Path("saves")
        saves_path.mkdir(exist_ok = True)

        '''
        # Approach 2: Using Pathlib (Modern Python alternative)
        src_path = Path("report.txt")
        tgt_path = Path("archive") / src_path.name

        # replace() automatically overwrites an existing file
        src_path.replace(tgt_path)'''
        
