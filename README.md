# Priority (Non-Preemptive) Scheduler

This is an application for scheduling processes using the **Priority (Non-Preemptive)** scheduling algorithm. It allows users to input process data, such as burst time, priority, and arrival time. The app then calculates the waiting time, turnaround time, and response time for each process and displays a **Gantt Chart** showing the timeline of these processes.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python)
- Matplotlib library (for plotting charts)

## Installation

1. Make sure you have Python 3.x installed.
2. To install Matplotlib, run the following command:
   ```bash
   pip install matplotlib
# How to Run
1. Run the file using Python:
     ```bash
       python main.py
2. Once the program runs, a window will appear asking you to input the number of processes and their data (arrival time, burst time, and priority).
3. After entering the data, click "Calculate" to compute the waiting time, turnaround time, and response time.
4. A new window will open displaying the Gantt Chart and the calculation results.

# How to Use
- **Enter the number of processes**: Input the number of processes you want to calculate.
- **Enter process data**: For each process, enter its arrival time, burst time, and priority.
- **Calculate results**: After entering the data, click the "Calculate" button to calculate the waiting time, turnaround time, and response time.
- **View results**: After the calculation, a pop-up window will display:
    - Average Waiting Time
    - Average Turnaround Time
    - Average Response Time
    - A Gantt Chart showing the timeline for each process.
 
# Example
- Number of processes: 3
- Processes:
  - Process 1: Arrival Time = 0, Burst Time = 5, Priority = 2
  - Process 2: Arrival Time = 1, Burst Time = 3, Priority = 1
  - Process 3: Arrival Time = 2, Burst Time = 4, Priority = 3
    
The program will calculate the waiting time, turnaround time, and response time based on the priority and arrival times, then display the results and the Gantt Chart.

# Notes
- The program uses a non-preemptive algorithm where processes are executed based on priority.
- In case of equal priorities, processes are sorted by their arrival time.



