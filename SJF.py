import threading


class Process:
    def __init__(self, process_number, burst_time):
        # Each process has a unique number and a burst time (CPU time required)
        self.process_number = process_number
        self.burst_time = burst_time

        # Waiting time: how long the process waits before starting execution
        # Turnaround time: total time from submission to completion
        self.waiting_time = 0
        self.turn_around_time = 0


class Scheduler:
    def __init__(self):
        # List to store all processes added by the user
        self.processes = []

        # Lock ensures that only one thread modifies the list at a time
        self.lock = threading.Lock()

    def add_process(self, p):
        # Add a process to the list safely using a lock
        with self.lock:
            self.processes.append(p)

    def calculate_times(self):
        # Calculate waiting time and turnaround time for each process
        with self.lock:
            # Sort processes based on burst time (Shortest Job First scheduling)
            self.processes.sort(key=lambda p: p.burst_time)

            elapsed = 0  # Keeps track of total CPU time passed so far

            for p in self.processes:
                # Waiting time = total CPU time of all previous processes
                p.waiting_time = elapsed

                # Turnaround time = waiting time + burst time
                p.turn_around_time = p.waiting_time + p.burst_time

                # Update elapsed CPU time for the next process
                elapsed += p.burst_time

    def print_results(self):
        # Print a neatly formatted table showing each process and its times
        with self.lock:
            print("\n" + "=" * 50)
            print(" " * 16 + "PROCESS SCHEDULING RESULTS")
            print("=" * 50 + "\n")

            # Table headers
            header = f"{'Process':<10}{'Burst Time':<15}{'Waiting Time':<15}{'Turnaround':<15}"
            print(header)
            print("-" * len(header))

            total_wt = 0  # Total waiting time, used to calculate average
            total_tat = 0  # Total turnaround time, used to calculate average

            for p in self.processes:
                # Print each process in table row
                print(f"{p.process_number:<10}{p.burst_time:<15}{p.waiting_time:<15}{p.turn_around_time:<15}")

            total_wt += p.waiting_time
            total_tat += p.turn_around_time

        # Calculate averages
        avg_wt = total_wt / len(self.processes)
        avg_tat = total_tat / len(self.processes)

        # Print averages in a clear format
        print("\n" + "-" * 50)
        print(f"{'Average Waiting Time:':<25}{avg_wt:.2f}")
        print(f"{'Average Turnaround Time:':<25}{avg_tat:.2f}")
        print("=" * 50)


class SchedulingThread(threading.Thread):
    def __init__(self, scheduler):
        # A separate thread to perform calculation of times
        super().__init__()
        self.scheduler = scheduler

    def run(self):
        # When the thread starts, it calculates waiting and turnaround times
        self.scheduler.calculate_times()


if __name__ == "__main__":
    scheduler = Scheduler()

    # Ask user for the number of processes to schedule
    num = int(input("Enter the number of processes: "))

    # Ask user for burst time for each process
    for i in range(1, num + 1):
        burst = int(input(f"Enter burst time for process {i}: "))
        scheduler.add_process(Process(i, burst))

    # Start a thread to calculate waiting and turnaround times
    t = SchedulingThread(scheduler)
    t.start()
    t.join()  # Wait for thread to finish

    # Print the final scheduling results in a professional table
    scheduler.print_results()
