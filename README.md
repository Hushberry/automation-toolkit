# ⚙️ Automation Toolkit (CLI)

A powerful, production-style Python command-line automation tool designed to streamline everyday system tasks such as file organization, backups, system monitoring, and bulk file renaming.

This project demonstrates real-world scripting and automation skills used in IT support, system administration, and DevOps environments.


## 🚀 Features

 📊 ** System Monitoring **

  * CPU usage
  * RAM usage
  * Disk usage

* 🗂️ **File Organization**

  * Automatically sorts files into folders based on extension

* 💾 **Folder Backup**

  * Creates timestamped backups of directories

* ✏️ **Bulk File Renaming**

  * Renames multiple files with a consistent naming pattern

* 🖥️ **CLI Interface**

  * Clean and simple command-line interaction using `argparse`


## 🧰 Tech Stack

* **Python 3**
* **psutil** – system monitoring
* **os / shutil** – file operations
* **argparse** – CLI argument parsing


## 📁 Project Structure

```
automation-toolkit/
│
├── toolkit.py
├── requirements.txt
├── setup.py
├── .gitignore
├── README.md
│
├── screenshots/
│   ├── system-info.png
│   └── file-organizer.png
│
└── automation_toolkit.egg-info/   (IGNORED by git)
---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/automation-toolkit.git
cd automation-toolkit
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the toolkit using:

```bash
python toolkit.py
```

Or make it executable:

```bash
chmod +x toolkit.py
./toolkit.py
```


## 📌 Available Commands

### 📊 Show System Information

```bash
python toolkit.py --info
```

Displays CPU, RAM, and disk usage.

---

### 🗂️ Organize Files by Type

```bash
python toolkit.py --organize ~/Downloads
```

Sorts files into folders like:

* `PDF_FILES`
* `JPG_FILES`
* `TXT_FILES`

---

### 💾 Backup a Folder

```bash
python toolkit.py --backup ~/Documents ~/Backup
```

Creates a timestamped backup:

```
Backup/backup_2026-05-02_14-30-00/
```

---

### ✏️ Bulk Rename Files

```bash
python toolkit.py --rename ~/Pictures image
```

Renames files like:

```
image_1.jpg
image_2.jpg
image_3.jpg
```

---

## 📸 Example Output

```
📊 SYSTEM INFORMATION
------------------------------
CPU Usage: 12%
RAM Usage: 48%
Disk Usage: 65%
------------------------------
```

---

## 🧠 Learning Outcomes

This project demonstrates:

* Building real-world CLI tools using Python
* Automating repetitive system tasks
* Working with the file system (os, shutil)
* Monitoring system resources using `psutil`
* Designing modular and maintainable Python scripts
* Structuring a production-ready project

---

## 🔒 Limitations

* No logging system (yet)
* No GUI interface
* No scheduling (manual execution only)

---

## 🔮 Future Improvements

* ✅ Add logging (file + console output)
* ⏱️ Task scheduler (cron integration)
* ⚙️ Config file support (JSON/YAML)
* 🖥️ GUI version (Tkinter or Web UI)
* 📦 Package as installable CLI tool (`pip install toolkit`)
* ☁️ Cloud backup support (AWS S3 / Google Drive)

---

## 💼 Use Cases

* IT support automation
* File management for developers
* Backup scripting
* Personal productivity workflows
* DevOps scripting utilities

---

## 👨‍💻 Author

**Vincent Chimezirim**
Python Developer | Cybersecurity Enthusiast | Automation Engineer

---

## 📜 License

This project is open-source and available for educational and professional use.

---

## ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🛠️ Contribute improvements

---

## 🚀 Related Projects

* 🌐 Job Scraper Dashboard (Flask + SQLite)
* 🛡️ Cybersecurity Toolkit (coming soon)

---

## 📬 Contact

For collaboration or freelance opportunities:

* Email: [administrator@netfusion.digital](mailto:administrator@netfusion.digital)
* Portfolio: https://netfusion.digital

---

