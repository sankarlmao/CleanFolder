import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

# --- CORE ORGANIZING LOGIC (from our previous script) ---
def organize_folder(target_directory, log_widget, status_widget):
    """The function that contains the logic to organize files."""
    try:
        # Update status
        status_widget.config(text="Status: Organizing...", fg="orange")
        log_widget.insert(tk.END, f"Scanning '{target_directory}'...\n")
        
        all_items = os.listdir(target_directory)
        files_moved = 0

        for item_name in all_items:
            item_path = os.path.join(target_directory, item_name)

            if os.path.isfile(item_path):
                # We don't want to move the script itself if it's in the folder
                if item_name == os.path.basename(__file__):
                    continue

                file_root, file_extension = os.path.splitext(item_name)
                
                if file_extension:
                    folder_name = file_extension[1:].upper() + " Files"
                    destination_folder_path = os.path.join(target_directory, folder_name)
                    
                    os.makedirs(destination_folder_path, exist_ok=True)

                    destination_path = os.path.join(destination_folder_path, item_name)
                    
                    shutil.move(item_path, destination_path)
                    files_moved += 1
                    
                    # Log the action to the text widget
                    log_widget.insert(tk.END, f"Moved: {item_name} -> {folder_name}\n")
                    log_widget.see(tk.END) # Auto-scroll to the bottom

        if files_moved == 0:
            log_widget.insert(tk.END, "No files needed to be organized.\n")
        else:
            log_widget.insert(tk.END, f"\nOrganization complete! Moved {files_moved} files. ✨\n")

        status_widget.config(text="Status: Complete!", fg="green")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_widget.config(text="Status: Error!", fg="red")
        log_widget.insert(tk.END, f"ERROR: {e}\n")


# --- GUI FUNCTIONS ---
def select_folder():
    """Opens a dialog to select a folder and updates the label."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        path_label.config(text=folder_path)
        log_box.delete(1.0, tk.END) # Clear log box
        status_label.config(text="Status: Ready", fg="black")


def start_organization():
    """Starts the organization process in a new thread to keep the GUI responsive."""
    target_directory = path_label.cget("text")
    if not target_directory or not os.path.isdir(target_directory):
        messagebox.showwarning("Warning", "Please select a valid folder first.")
        return
    
    # Clear the log box before starting
    log_box.delete(1.0, tk.END)

    # Run the organization in a separate thread to prevent the GUI from freezing
    # The 'daemon=True' ensures the thread will close when the main window is closed
    organize_thread = threading.Thread(
        target=organize_folder, 
        args=(target_directory, log_box, status_label),
        daemon=True
    )
    organize_thread.start()


# --- GUI SETUP ---
# Main window
root = tk.Tk()
root.title("Directory Organizer")
root.geometry("600x450")
root.minsize(500, 350)
root.config(bg="#f0f0f0")

# Main frame
main_frame = tk.Frame(root, padx=15, pady=15, bg="#f0f0f0")
main_frame.pack(expand=True, fill=tk.BOTH)

# --- Top Section: Folder Selection ---
top_frame = tk.Frame(main_frame, bg="#f0f0f0")
top_frame.pack(fill=tk.X, pady=(0, 10))

select_button = tk.Button(
    top_frame, 
    text="Select Folder", 
    command=select_folder, 
    font=("Helvetica", 10, "bold"),
    bg="#007BFF",
    fg="white",
    padx=10,
    pady=5,
    relief=tk.FLAT
)
select_button.pack(side=tk.LEFT, padx=(0, 10))

path_label = tk.Label(
    top_frame, 
    text="No folder selected", 
    bg="#FFFFFF", 
    fg="#333", 
    anchor="w", 
    padx=10,
    relief=tk.SUNKEN,
    borderwidth=1
)
path_label.pack(side=tk.LEFT, expand=True, fill=tk.X)

# --- Middle Section: Log Box ---
log_frame = tk.Frame(main_frame)
log_frame.pack(expand=True, fill=tk.BOTH, pady=(0, 10))

log_label = tk.Label(log_frame, text="Log:", font=("Helvetica", 10, "bold"), bg="#f0f0f0")
log_label.pack(anchor="w")

log_box = tk.Text(log_frame, height=15, bg="#FFFFFF", relief=tk.SUNKEN, borderwidth=1, state=tk.NORMAL)
log_box.pack(expand=True, fill=tk.BOTH)

# --- Bottom Section: Action Button & Status ---
bottom_frame = tk.Frame(main_frame, bg="#f0f0f0")
bottom_frame.pack(fill=tk.X)

start_button = tk.Button(
    bottom_frame, 
    text="Start Organizing", 
    command=start_organization,
    font=("Helvetica", 12, "bold"),
    bg="#28a745",
    fg="white",
    pady=8,
    relief=tk.FLAT
)
start_button.pack(fill=tk.X)

status_label = tk.Label(
    main_frame, 
    text="Status: Ready", 
    bd=1, 
    relief=tk.SUNKEN, 
    anchor=tk.W, 
    bg="#f0f0f0"
)
status_label.pack(side=tk.BOTTOM, fill=tk.X, pady=(5,0))

# Start the GUI event loop
root.mainloop()
