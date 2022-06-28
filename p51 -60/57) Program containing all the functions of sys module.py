import sys
import threading
from sys import settrace
print(sys.getrefcount(1556778))

print(sys.getsizeof('hello'))

interval = sys.getswitchinterval()
print(interval)

max_val = sys.maxsize
print(max_val)

print("Using the stdout stream")
sys.stdout.write("Another way to do it!\n")

save_stderr = sys.stderr
fh = open("errors.txt", "w")
sys.stderr = fh

print(sys.stderr, "printing to error.txt")

# return to normal:
sys.stderr = save_stderr

fh.close()

# settrace()


def my_tracer(frame, event, arg=None):

    code = frame.f_code

    func_name = code.co_name

    line_no = frame.f_lineno

    print(f"A {event} encountered in \
    {func_name}() at line number {line_no} ")

    return my_tracer


def fun():
    return "GFG"


def check():
    return fun()


settrace(my_tracer)

check()

limit = sys.getrecursionlimit()

print('Before changing, limit of stack =', limit)

New_limit = 500

sys.setrecursionlimit(New_limit)

limit = sys.getrecursionlimit()

# Print the current limit
print('After changing, limit of stack =', limit)


def deferral():
    pass


def run(self):
    if sys.getprofile() is not None:
        raise RuntimeError('Another profiler already registered')
    with deferral() as defer:
        self._times_entered.clear()
        self.overhead = 0.0
        sys.setprofile(self._profile)
        defer(sys.setprofile, None)
        threading.setprofile(self._profile)
        defer(threading.setprofile, None)
        self.timer.start(self)
        defer(self.timer.stop)
        yield
