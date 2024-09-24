"""
the purpose of this file is providing a time delta mechanism that ensures
that movement is not dependent on framerate and providing an acumulator mechanism for the timing
of animation and events
"""
import time


class timer:
    def __init__(self,accumulator_size = None):
        self.__time_anchor = time.time()
        self.__time_accumulator = 0
        self.__acumulator_size = accumulator_size


    def delta_timer(self):
        current_time = time.time()
        time_delta = current_time - self.__time_anchor
        self.__time_anchor = current_time

        if self.__acumulator_size != None:
            self.__time_accumulator += time_delta
            if self.__time_accumulator >= self.__acumulator_size:
                self.__time_accumulator = 0

        return time_delta



    def get_timing(self):
        return self.__time_accumulator == 0


    def set_new_accumulator_size(self,accumulator_size):
        self.__acumulator_size = accumulator_size




