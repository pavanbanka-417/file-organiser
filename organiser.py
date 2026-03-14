import os
import shutil
folder = input("Enter the folder name: ")

file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4"],
    "PDFs": [".pdf"],
    "Audio": [".mp3"],
    "Archives": [".zip", ".rar"],
    "Documents": [".docx", ".doc"],
    "Code": [".py"]
}

files = os.listdir(folder)
for file in files:
  file_path = os.path.join(folder, file)
  if os.path.isfile(file_path):
     for folder_name,extensions in file_types.items():
        if any(file.lower().endswith(ext) for ext in extensions):
            destination = os.path.join(folder, folder_name)
            if not os.path.exists(destination):
                os.makedirs(destination)
            shutil.move(file_path, os.path.join(destination, file))
            print(file,"moved to",folder_name)
            break
