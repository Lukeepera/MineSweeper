import tkinter as tk
import subprocess
import sys


class ModernMinesweeper:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Modern Minesweeper")
        self.root.geometry("1024x768")
        self.root.minsize(800, 600)

        self.colors = {
            'bg': '#1E1E1E',
            'text': '#FFFFFF',
            'easy': '#4CAF50',
            'medium': '#FF9800',
            'hard': '#F44336',
            'hover_easy': '#45a049',
            'hover_medium': '#e68900',
            'hover_hard': '#e53935',
            'title_glow': '#3498db'
        }

        self.animation_speed = 20
        self.root.configure(bg=self.colors['bg'])
        self.setup_ui()

    def run_game(self, difficulty):
        try:
            subprocess.run([sys.executable, 'main.py', difficulty], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running the game: {e}")

    def animate_scale(self, widget, start_size, end_size, steps=10):
        current_step = 0
        size_diff = end_size - start_size

        def update_size():
            nonlocal current_step
            if current_step < steps:
                progress = current_step / steps
                current_size = start_size + (size_diff * progress)
                widget.configure(font=('Segoe UI', int(current_size), 'bold'))
                current_step += 1
                self.root.after(self.animation_speed, update_size)

        update_size()

    def create_styled_button(self, parent, text, color, hover_color, command):
        btn = tk.Button(
            parent,
            text=text,
            font=('Segoe UI', 16, 'bold'),
            width=20,
            height=2,
            bg=color,
            fg=self.colors['text'],
            activebackground=hover_color,
            activeforeground=self.colors['text'],
            relief='raised',
            bd=0,
            command=command,
            cursor='hand2'
        )

        def on_enter(e):
            btn.configure(bg=hover_color)
            self.animate_scale(btn, 16, 18)
            # Add highlight
            btn.configure(highlightbackground='white', highlightthickness=2)

        def on_leave(e):
            btn.configure(bg=color)
            self.animate_scale(btn, 18, 16)
            # Remove highlight
            btn.configure(highlightthickness=0)

        btn.bind('<Enter>', on_enter)
        btn.bind('<Leave>', on_leave)

        return btn

    def setup_ui(self):
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        title = tk.Label(
            self.root,
            text="MINESWEEPER",
            font=('Segoe UI', 52, 'bold'),
            fg=self.colors['title_glow'],
            bg=self.colors['bg']
        )
        title.grid(row=0, column=0, pady=(40, 0))

        subtitle = tk.Label(
            self.root,
            text="⚡ Select Your Challenge ⚡",
            font=('Segoe UI', 18),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        subtitle.grid(row=1, column=0, pady=(0, 40))

        buttons_frame = tk.Frame(self.root, bg=self.colors['bg'])
        buttons_frame.grid(row=2, column=0, rowspan=3, sticky='nsew')
        buttons_frame.grid_rowconfigure((0, 1, 2), weight=1)
        buttons_frame.grid_columnconfigure(0, weight=1)

        easy_btn = self.create_styled_button(
            buttons_frame,
            "😊 Easy",
            self.colors['easy'],
            self.colors['hover_easy'],
            lambda: self.run_game("easy")
        )
        easy_btn.grid(row=0, column=0, pady=15)

        medium_btn = self.create_styled_button(
            buttons_frame,
            "😎 Medium",
            self.colors['medium'],
            self.colors['hover_medium'],
            lambda: self.run_game("medium")
        )
        medium_btn.grid(row=1, column=0, pady=15)

        hard_btn = self.create_styled_button(
            buttons_frame,
            "🔥 Hard",
            self.colors['hard'],
            self.colors['hover_hard'],
            lambda: self.run_game("hard")
        )
        hard_btn.grid(row=2, column=0, pady=15)

        footer_frame = tk.Frame(self.root, bg=self.colors['bg'])
        footer_frame.grid(row=5, column=0, sticky='ew', pady=20)
        footer_frame.grid_columnconfigure(0, weight=1)

        version_label = tk.Label(
            footer_frame,
            text="v1.0.0 | Made with 💖",
            font=('Segoe UI', 10),
            fg='#666666',
            bg=self.colors['bg']
        )
        version_label.grid(row=0, column=0)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ModernMinesweeper()
    app.run()
