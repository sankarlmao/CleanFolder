#During the initial stages of this project it was named as 'organizer_gui' and 'Directory-Organizer' and the finale name of the project is CleanFolder , soo If you find files named the older way im sorry they will be updated in the future commits 
# CleanFolder , A simple Folder organizer 📂  

A simple yet powerful desktop application with a clean graphical user interface (GUI) to automatically organize files in a directory based on their extension. Tidy up messy folders like "Downloads" with a single click.

---
---

## 📖 About The Project

We all have that one folder on our computer (usually **Downloads**) that becomes a dumping ground for documents, images, installers, and more. Finding anything in that mess can be a nightmare. This project was created to solve that exact problem.

**Directory Organizer Pro** provides an intuitive interface to select any folder and let the script intelligently sort all the files into neatly organized sub-folders (e.g., `PDF Files`, `JPG Files`, `EXE Files`).  
It’s a practical tool built to bring order to digital chaos.

---

## ✨ Key Features

- **Intuitive GUI**: A clean, user-friendly interface built with Tkinter. No command-line knowledge required.  
- **One-Click Organization**: Simply select a folder and click **Start** to automate the entire cleaning process.  
- **Smart Grouping**: Files are automatically moved into categorized folders based on their file type.  
- **Real-Time Logging**: A log panel provides live feedback on which files are being moved and where.  
- **Safe and Reliable**: Only moves files, never deletes. Automatically creates folders as needed.  
- **Cross-Platform**: Built with Python and Tkinter. Works on Windows, macOS, and Linux.  
- **Standalone Executable**: Packaged into a single executable file, so no Python installation is required.  

---

## 🚀 Getting Started

You can either download the **ready-to-use application** or **build it yourself from the source code**.

---

### 📥 Installation (For Users)

1. Navigate to the **[Releases](../../releases)** page of this repository.  
2. Download the latest:
   - `Directory-Organizer.exe` (for Windows)  
   - `Directory-Organizer` (for Linux/macOS)  
3. Place the file anywhere on your computer.  
4. Double-click to run. **No installation needed!**

---

### 💻 Installation (For Developers)

To run this project from source, ensure you have:

- **Python 3.6+** installed  

Steps:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

# Navigate to project directory
cd your-repository-name

# Run the application
python organizer_gui.py

```
For build this install
 ```bash
pip install pyinstaller
pyinstaller --onefile CleanFolder.py
