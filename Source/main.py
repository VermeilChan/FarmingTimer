import time
import tkinter as tk

class FarmingTimer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Farming Timer")
        self.configure(bg="#1e1e1e")
        self.geometry("200x110")
        self.timer_label = tk.Label(self, text="00:00:00", font=("Roboto", 24), bg="#1e1e1e", fg="white")
        self.timer_label.pack(pady=10)
        button_frame = tk.Frame(self, bg="#1e1e1e")
        button_frame.pack(pady=10)
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_timer, bg="#444444", fg="white", bd=0)
        self.pause_button = tk.Button(button_frame, text="Pause/Resume", command=self.pause_resume_timer, bg="#444444", fg="white", bd=0)
        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_timer, bg="#444444", fg="white", bd=0)
        self.start_button.grid(row=0, column=0, padx=5)
        self.pause_button.grid(row=0, column=1, padx=5)
        self.stop_button.grid(row=0, column=2, padx=5)
        self.timer_running = False
        self.paused = False
        self.start_time = 0

    def start_timer(self):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True
            self.update_timer()

    def pause_resume_timer(self):
        if self.timer_running:
            self.paused = not self.paused
            if not self.paused:
                self.start_time = time.time() - (self.current_time - self.start_time)
                self.update_timer()
            else:
                self.current_time = time.time()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.paused = False
            self.timer_label.config(text="00:00:00")

    def update_timer(self):
        if self.timer_running and not self.paused:
            current_time = time.time()
            elapsed_time = int(current_time - self.start_time)
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.after(1000, self.update_timer)

if __name__ == "__main__":
    app = FarmingTimer()
    app.mainloop()
