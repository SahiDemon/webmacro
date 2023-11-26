import subprocess
import time
import os

def detect_website():
    try:
        chrome_process = subprocess.Popen(
            ["tasklist", "/fi", "imagename eq chrome.exe", "/fo", "csv"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        chrome_process.communicate()  # Wait for the process to finish

        if chrome_process.returncode == 0:
            active_window_title = subprocess.check_output(
                ["powershell", "(Get-Process -name chrome).MainWindowTitle"],
                stderr=subprocess.PIPE
            ).decode('utf-8').strip()

            if "youtube" in active_window_title.lower() or "myflixer" in active_window_title.lower():
                print("Detected YouTube or MyFlixerz - Running AHK script")
                return True

    except subprocess.CalledProcessError as e:
        print(f"Error executing PowerShell command: {e}")
        return False

    return False

def run_ahk_script():
    ahk_script_path = r"macro.ahk" # your script path
    
    try:
        ahk_process = subprocess.Popen(['AutoHotKey.exe', ahk_script_path])
        print("AutoHotKey script started successfully.")
        return ahk_process
    except Exception as e:
        print(f"Error starting AutoHotKey script: {e}")
        return None

def main():
    ahk_process = None

    while True:
        website_detected = detect_website()

        if website_detected:
            if ahk_process is None:
                ahk_process = run_ahk_script()
        else:
            if ahk_process is not None:
                print("Website not detected. Killing AutoHotKey script.")
                ahk_process.terminate()
                ahk_process = None
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear') 
                

        time.sleep(8)  # Adjust the sleep time as needed

if __name__ == "__main__":
    main()
