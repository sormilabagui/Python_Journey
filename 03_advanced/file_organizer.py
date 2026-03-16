# file_organizer.py
# Organizes files in a folder by file type


# NOTE:
# This script organizes files by type.
# Use a test folder before running on important directories.
import os
import shutil

folder_path = "sample_folder"   # change to your test folder

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"]
}

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):

        for folder, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):

                target_folder = os.path.join(folder_path, folder)

                os.makedirs(target_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(target_folder, filename))

                print(f"Moved {filename} → {folder}")
                break