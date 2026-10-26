from pathlib import Path
from subprocess import Popen

def launch_hidden():
    # 1. Get the folder where this script lives
    current_folder = Path(__file__).parent.absolute()
    target_script = current_folder / "IP_Logger.py"

    # Windows-specific flag
    HIDE_CMD = 134217728

    # 3. Launch main.py silently using pythonw.exe
    Popen(
        ["pythonw.exe", target_script],
        creationflags = HIDE_CMD,
        cwd=current_folder  # Keeps your multi-file paths working perfectly
    )

if __name__ == "__main__":
    launch_hidden()
