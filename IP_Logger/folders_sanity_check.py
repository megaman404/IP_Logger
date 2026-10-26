from pathlib import Path

def check_folders() -> None:
    """ Checks for Graphs and Reports folders, otherwise create them """
    try:
        current_directory = Path(__file__).absolute()
        check_graphs_folder = current_directory / "Graphs"
        check_reports_folder = current_directory / "Reports"

        if check_graphs_folder.is_dir() and check_reports_folder.is_dir():
            print("Folders exist")
            return
        raise FileNotFoundError()
        
    except FileNotFoundError:
        print("Folders were created")
        folder_path = Path("Graphs")
        folder_path.mkdir(exist_ok = True)

        folder_path = Path("Reports")
        folder_path.mkdir(exist_ok = True)

if __name__ == "__main__":
    check_folders()
