from pathlib import Path

def check_folders() -> None:
    """ Checks for Graphs and Reports folders, otherwise create them """
    try:
        check_graphs_folder = Path("./Graphs").is_dir()
        check_reports_folder = Path("./Reports").is_dir()
        if check_graphs_folder and check_reports_folder:
            print("Folders exist")
            return
        raise FileNotFoundError()
        
    except FileNotFoundError:
        print("Folders were created")
        folder_path = Path("Graphs")
        folder_path.mkdir(exist_ok=True)

        folder_path = Path("Reports")
        folder_path.mkdir(exist_ok=True)

if __name__ == "__main__":
    check_folders()
