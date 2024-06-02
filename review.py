# Review 1
# def add_to_list(value, my_list=[]): -- The calling function will use the same list instance for all subsequent calls if the caller does not provide the my_list parameter.
def add_to_list(value, my_list = None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

# Review 2
def format_greeting(name, age):
    # return "Hello, my name is {name} and I am {age} years old." -- need to apply f-string or other string formatting function
    return f"Hello, my name is {name} and I am {age} years old."


# Review 3
class Counter:
    # count = 0 -- An instance variable "self.count" should be initialized in the "__ init__" method
    
    def __init__(self, count = 0):
        self.__count = count 

    def increment(self):  
        self.__count += 1

    def get_count(self):
        return self.__count

# Review 4
import threading

class SafeCounter:
    ## In a multi-threaded environment, multiple threads may simultaneously access and modify the count attribute, leading to data competition and inconsistent results.
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()  # add a threading lock

    def increment(self):
        with self.lock:  # Using the "with" statement to automatically manage lock acquisition and release
            self.count += 1

def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Review 5
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            # counts[item] =+ 1 -- count will not increase if using "=+ 1"
            counts[item] += 1
        else:
            counts[item] = 1
    return counts