from Queue import Queue

class Printer:
    def __init__(self):
        self.queue = Queue()

    def add_print_job(self, job):
        self.queue.enqueue(job)

    def print_job(self):
        if self.queue.is_empty():
            print("No jobs to print.")
            return None
        return self.queue.dequeue()

    def view_next_job(self):
        if self.queue.is_empty():
            print("No jobs in the queue.")
            return None
        return self.queue.peek()

    def is_empty(self):
        return self.queue.is_empty()

    def size(self):
        return self.queue.size()

# Example usage
printer_queue = Printer()
printer_queue.add_print_job("Job 1")
printer_queue.add_print_job("Job 2")
printer_queue.add_print_job("Job 3")

print("Next job:", printer_queue.view_next_job())  # "Job 1"
printer_queue.print_job() 
print("Next job:", printer_queue.view_next_job())  # "Job 2"

print("Queue size:", printer_queue.size())  # 2

printer_queue.print_job()
printer_queue.print_job()

print("Is queue empty?", printer_queue.is_empty())  # True
