import tkinter as tk
import subprocess
import sys

def run_game(difficulty):
    try:
        subprocess.run([sys.executable, 'main.py', difficulty], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running the game: {e}")

def create_window():
    root = tk.Tk()
    root.title("Minesweeper")
    root.geometry("800x800")
    root.config(bg="#282828")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    label = tk.Label(root, text="Minesweeper", font=("Arial", 40), fg="#FFFFFF", bg="#282828")
    label.grid(row=0, column=0, pady=60)

    easy_button = tk.Button(root, text="Easy", width=20, height=2, font=("Arial", 20), fg="white", bg="#4CAF50",
                            activebackground="#45a049", command=lambda: run_game("easy"))
    easy_button.grid(row=1, column=0, pady=15)

    medium_button = tk.Button(root, text="Medium", width=20, height=2, font=("Arial", 20), fg="white", bg="#FF9800",
                              activebackground="#e68900", command=lambda: run_game("medium"))
    medium_button.grid(row=2, column=0, pady=15)

    hard_button = tk.Button(root, text="Hard", width=20, height=2, font=("Arial", 20), fg="white", bg="#F44336",
                            activebackground="#e53935", command=lambda: run_game("hard"))
    hard_button.grid(row=3, column=0, pady=15)

    root.mainloop()

if __name__ == "__main__":
    create_window()
