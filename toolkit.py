#!/usr/bin/env python3
import os
import shutil
import argparse
import psutil
from datetime import datetime

def system_info():
    print("\n📊 SYSTEM INFORMATION")
    print("-" * 30)
    print(f"CPU Usage : {psutil.cpu_percent()}%")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
    print("-" * 30)

def organize_folder(path):
    if not os.path.exists(path):
        print("x Path does not exist")
        return
    
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        ext = file.split('.')[-1]
        folder = os.path.join(path, ext.upper() + "_FILES")
        os.makedirs(folder, exist_ok=True)
        shutil.move(file_path, os.path.join(folder, file))

    print (f" Files organized in {path}")

def backup_folder(source, destination):
    if not os.path.exists(source):
        print("x Source folder not found")
        return
    
    if not os.path.exists(destination):
        os.makedirs(destination)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = os.path.join(destination, f"backup_{timestamp}")

    shutil.copytree(source, backup_name)
    print (f" Backup created at {backup_name}")


def bulk_rename(folder, base_name):
    if not os.path.exists(folder):
        print("x Folder not found")
        return
    
    for file in files:
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            ext = file.split('.')[-1]
            new_name = f"{base_name}_{count}.{ext}"
            new_path = os.path.join(folder, new_name)

            os.rename(file_path, new_path)
            count += 1

    print(f" Renamed {count -1} files")


def main():
    parser = argparse.ArgumentParser(description="Python Automation Toolkit")
    parser.add_argument("--info", action="store_true", help="Show system info")
    parser.add_argument("--organize", help="Organize files in folder")
    parser.add_argument("--backup", nargs=2, help="Backup folder: source destination")
    parser.add_argument("--rename", nargs=2, help="Rename files: folder base_name")
    args = parser.parse_args()

    if args.info:
        system_info()

    elif args.organize:
        organize_folder(args.organize)

    elif args.backup:
        backup_folder(args.backup[0], args.backup[1])

    elif args.rename:
        bulk_rename(args.rename[0], args.rename[1])

    else:
        print("""⚙️ Python Automation Toolkit

            Commands:
            --info
           --organize <folder>
           --backup <source> <destination>
           --rename <folder> <base_name>
            """)
        
if __name__ == "__main__":
    main()
        