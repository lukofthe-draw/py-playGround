import time
from tkinter import *

class Stopwatch:
    def __init__(self, master):
        # Set up the GUI
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        self.label = Label(self.frame, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()
        self.stop_button = Button(self.frame, text="Stop", command=self.stop)
        self.stop_button.pack()
        self.reset_button = Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.pack()

        # Initialize the stopwatch variables
        self.start_time = time.time()  # Start the timer when the program is run
        self.elapsed_time = 0
        self.running = True
        self.update_label()  # Update the label to display the current time

    def stop(self):
        # Stop the stopwatch
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False

    def reset(self):
        # Reset the stopwatch
        self.start_time = time.time()
        self.elapsed_time = 0
        self.running = True

    def update_label(self):
        # Update the label to display the current time
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        time_str = self.convert_time(self.elapsed_time)
        self.label.configure(text=time_str)
        self.label.after(100, self.update_label)  # Schedule the update_label function to be called again in 100 milliseconds

    def convert_time(self, elapsed_time):
        # Convert the elapsed time to a formatted string
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Set up the GUI and start the stopwatch
root = Tk()
stopwatch = Stopwatch(root)
root.mainloop()
