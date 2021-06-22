import itertools
import sys
import time


class RotatingProgress(object):
    def __init__(self):
        self.default = "\|/-"
        self.spinner = self.default

    def rotating_progress(self, message):
        print(message, end="")
        self.spinner = itertools.cycle(self.default)

    def run(self):
        sys.stdout.write(next(self.spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")
