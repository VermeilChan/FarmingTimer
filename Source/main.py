import time
import tkinter as tk

timer_running = False
paused = False
start_time = 0
current_time = 0

def start_timer():
    global timer_running, start_time
    if not timer_running:
        start_time = time.time()
        timer_running = True
        update_timer()

def pause_resume_timer():
    global paused, start_time, current_time
    if timer_running:
        paused = not paused
        if not paused:
            start_time = time.time() - (current_time - start_time)
            update_timer()
        else:
            current_time = time.time()

def stop_timer():
    global timer_running, paused
    if timer_running:
        timer_running = False
        paused = False
        timer_label.config(text="00:00:00")

def update_timer():
    global timer_running, paused, start_time, current_time
    if timer_running and not paused:
        current_time = time.time()
        elapsed_time = int(current_time - start_time)
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        timer_label.after(1000, update_timer)

root = tk.Tk()
root.title("Farming Timer")
root.configure(bg="#1e1e1e")
root.geometry("250x110")
root.resizable(False, False)

timer_label = tk.Label(root, text="00:00:00", font=("Roboto", 24), bg="#1e1e1e", fg="white")
timer_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", command=start_timer, bg="#444444", fg="white", bd=0)
pause_button = tk.Button(button_frame, text="Pause/Resume", command=pause_resume_timer, bg="#444444", fg="white", bd=0)
stop_button = tk.Button(button_frame, text="Stop", command=stop_timer, bg="#444444", fg="white", bd=0)

start_button.grid(row=0, column=0, padx=5)
pause_button.grid(row=0, column=1, padx=5)
stop_button.grid(row=0, column=2, padx=5)

root.mainloop()
