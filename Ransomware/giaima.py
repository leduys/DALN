import os
import base64
import  sys

import psutil
sys.path.append("./DES")
import DES
import string, os, shutil
from ctypes import windll
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

def is_encrypted(file_path):
    try:
        # Mở tệp và kiểm tra nội dung
        with open(file_path, 'rb') as f:
            content = f.read()
            if b'\x00' in content and file_path.endswith(".txt"):
                return True
            base64.b64decode(content)
            return False
    except:
        return True

def get_files(drives):
    hidden_folder_files = []
    for drive in drives:
        src_dir = drive + ':\\'
        for root, dirs, files in os.walk(src_dir):
            if '.hidden_folder' in dirs:
                hidden_folder_path = os.path.join(root, '.hidden_folder')
                for _, _, hidden_files in os.walk(hidden_folder_path):
                    for hidden_file in hidden_files:
                        hidden_file_path = os.path.join(hidden_folder_path, hidden_file)
                        if is_encrypted(hidden_file_path):
                            hidden_folder_files.append(hidden_file_path)
    return hidden_folder_files

def decrypt_and_move(pathfiles):
    hidden_directory = ".hidden"
    # Tên file chứa key đã mã hóa
    key_file = ".hidden\key2.bin"
    with open(key_file, 'rb') as file:
            stored_hashed_key = file.read()
    print(stored_hashed_key)
    for encrypted_file in pathfiles:
        try:
            DES.decrypt(encrypted_file)
            parent_directory = os.path.dirname(os.path.dirname(encrypted_file))
            shutil.move(encrypted_file, parent_directory)
            hidden_directory = os.path.join(parent_directory, ".hidden_folder")
            if os.path.exists(hidden_directory):
                shutil.rmtree(hidden_directory)
        except Exception as e:
            pass

drives = get_drives()
pathfiles = get_files(drives)
decrypt_and_move(pathfiles)


def kill_terminal_processes():
    # Lấy danh sách các tiến trình đang chạy
    all_processes = psutil.process_iter()

    # Duyệt qua từng tiến trình
    for process in all_processes:
        try:
            # Kiểm tra xem tiến trình có phải là terminal không
            if process.name() == "cmd.exe" or process.name() == "powershell.exe":
                # Tắt tiến trình terminal
                process.terminate()  # hoặc sử dụng process.kill() nếu cần thiết
               
        except psutil.NoSuchProcess:
            pass
        except psutil.AccessDenied:
            pass

def kill_virut():
    import glob

    python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

    for script in python_scripts: 
        if script != "dahinh.py":  # Loại trừ file dahinh.py
            # Đọc nội dung của file
            with open(script, 'r', encoding='utf-8', errors='ignore') as f:
                script_code = f.readlines()

            # Tìm vị trí của `### THE VIRUS STARTS HERE ###` và `### THE VIRUS ENDS HERE ###`
            start_index = -1
            end_index = -1
            for i, line in enumerate(script_code):
                if line.strip() == "### THE VIRUS STARTS HERE ###":
                    start_index = i
                elif line.strip() == "### THE VIRUS ENDS HERE ###":
                    end_index = i

            # Nếu tìm thấy cả hai vị trí, xóa cả hai dòng và nội dung nằm giữa chúng
            if start_index != -1 and end_index != -1:
                del script_code[start_index:end_index+1]

                # Ghi lại nội dung của file
                with open(script, 'w', encoding='utf-8') as f:
                    f.writelines(script_code)



kill_virut()

kill_terminal_processes()

