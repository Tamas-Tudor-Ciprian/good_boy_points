"""
the purpose of this file is providing a time delta mechanism that ensures
that movement is not dependent on framerate and providing an acumulator mechanism for the timing
of animation and events
"""
import time


class timer:
    """this should have a function that takes another and only calls it when a certain delta has passed but doing so
    everytime the interval has passed creating smooth timing for events"""

    def __init__(self, accumulator_size=None):
        self.__time_anchor = time.time()
        self.__time_accumulator = 0
        self.__acumulator_size = accumulator_size
        self.reset = False

    def delta_timer(self, function_to_call=None):
        current_time = time.time()
        time_delta = current_time - self.__time_anchor
        self.__time_anchor = current_time

        if self.__acumulator_size != None:
            self.__time_accumulator += time_delta
            if self.__time_accumulator >= self.__acumulator_size:
                self.__time_accumulator = 0
                self.reset = True
                if function_to_call != None:
                    function_to_call()

        return time_delta

    def get_timing(self):
        to_return = self.reset
        self.reset = False
        return to_return

    def set_new_accumulator_size(self, accumulator_size):
        self.__acumulator_size = accumulator_size
