import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import namedtuple

Process = namedtuple('Process', ['name', 'burst_time', 'priority', 'arrival_time'])

class SchedulerApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Priority (Non-Preemptive) Scheduler")
        
        self.processes = []
        self.num_processes = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.master, text="Number of processes:").grid(row=0, column=0)
        self.num_processes_entry = tk.Entry(self.master)
        self.num_processes_entry.grid(row=0, column=1)
        
        tk.Button(self.master, text="Enter", command=self.get_num_processes).grid(row=0, column=2)
        
        self.process_frame = tk.Frame(self.master)
        
        self.gantt_chart_label = tk.Label(self.master, text="Gantt Chart:")
        self.gantt_chart_label.grid(row=1, column=0, columnspan=3)
        self.gantt_chart_text = tk.Text(self.master, height=5, width=50)
        self.gantt_chart_text.grid(row=2, column=0, columnspan=3)
        
        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=1)
        
    def get_num_processes(self):
        try:
            self.num_processes = int(self.num_processes_entry.get())
            if self.num_processes <= 0:
                raise ValueError
            self.create_process_entries()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of processes.")
    
    def create_process_entries(self):
        self.process_frame.destroy()
        self.process_frame = tk.Frame(self.master)
        self.process_frame.grid(row=1, column=0, columnspan=3)
        
        tk.Label(self.process_frame, text="Arrival Time").grid(row=0, column=1)
        tk.Label(self.process_frame, text="Burst Time").grid(row=0, column=2)
        tk.Label(self.process_frame, text="Priority").grid(row=0, column=3)
        
        self.process_entries = []
        for i in range(self.num_processes):
            tk.Label(self.process_frame, text=f"Process {i+1}").grid(row=i+1, column=0)
            arrival_entry = tk.Entry(self.process_frame)
            arrival_entry.grid(row=i+1, column=1)
            burst_entry = tk.Entry(self.process_frame)
            burst_entry.grid(row=i+1, column=2)
            priority_entry = tk.Entry(self.process_frame)
            priority_entry.grid(row=i+1, column=3)
            self.process_entries.append((arrival_entry, burst_entry, priority_entry))
        
    def calculate(self):
        self.processes = []
        for entry in self.process_entries:
            try:
                arrival_time = int(entry[0].get())
                burst_time = int(entry[1].get())
                priority = int(entry[2].get())
                if arrival_time < 0 or burst_time < 0 or priority < 0:
                    raise ValueError
                process_name = f"Process {len(self.processes)+1}"
                self.processes.append(Process(process_name, burst_time, priority, arrival_time))
            except ValueError:
                messagebox.showerror("Error", "Please enter valid positive integers for arrival time, burst time, and priority.")
                return
        
        self.processes.sort(key=lambda x: (x.name, x.priority))
        
        fig, ax = plt.subplots()
        ax.set_title('Gantt Chart')
        ax.set_xlabel('Time')
        ax.set_ylabel('Process')
        
        current_time = 0
        waiting_times = []
        turnaround_times = []
        response_times = []
        
        for i, process in enumerate(self.processes):
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            ax.barh(i, process.burst_time, left=current_time, label=f'{process.name}\nTurnaround Time: {process.burst_time}\nWaiting Time: {current_time - process.arrival_time}\nResponse Time: {current_time - process.arrival_time}')
            waiting_time = current_time - process.arrival_time
            response_time = current_time - process.arrival_time
            turnaround_time = waiting_time + process.burst_time
            waiting_times.append(waiting_time)
            response_times.append(response_time)
            turnaround_times.append(turnaround_time)
            current_time += process.burst_time
        
        avg_waiting_time = sum(waiting_times) / self.num_processes
        avg_turnaround_time = sum(turnaround_times) / self.num_processes
        avg_response_time = sum(response_times) / self.num_processes
        
        ax.legend()
        plt.show()
        
        messagebox.showinfo("Results", f"Average Waiting Time: {avg_waiting_time:.2f}\n"
                                        f"Average Turnaround Time: {avg_turnaround_time:.2f}\n"
                                        f"Average Response Time: {avg_response_time:.2f}")
        

def main():
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
