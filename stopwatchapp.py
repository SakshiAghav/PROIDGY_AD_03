import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        # Create a label to display time
        self.time_label = tk.Label(root, text=self.format_time(), font=("Arial", 40), fg="black")
        self.time_label.pack(pady=20)

        # Create Start, Pause, and Reset buttons
        self.start_button = tk.Button(root, text="Start", font=("Arial", 20), command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.pause_button = tk.Button(root, text="Pause", font=("Arial", 20), command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=20)

        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 20), command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=20)

    def format_time(self):
        return f"{self.minutes:02}:{self.seconds:02}:{self.milliseconds:02}"

    def update_time(self):
        if self.running:
            self.milliseconds += 1
            if self.milliseconds == 100:
                self.milliseconds = 0
                self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1

            # Update the displayed time
            self.time_label.config(text=self.format_time())
            # Call the update_time method after 10 milliseconds
            self.root.after(10, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.time_label.config(text=self.format_time())

if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()
