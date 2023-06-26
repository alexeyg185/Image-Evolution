from GlobalDefintions import *
import sys
import logging
import time
import psutil



# -------------------------------------------------------------------------------------------------
# Logger BEG
# Encapsulates logging handling
# -------------------------------------------------------------------------------------------------
def create_logger(debug_mode = True):

    if debug_mode is True:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logger = logging.getLogger()
    logger.setLevel(level)
    # Create the logging to stdout
    strm_hndlr = logging.StreamHandler(sys.stdout)
    format = LOG_FORMAT
    formatter = logging.Formatter(format)
    strm_hndlr.setFormatter(formatter)
    # Add handler to logger object
    logger.addHandler(strm_hndlr)
    return logger

Log = create_logger(DBG_ON)
# -------------------------------------------------------------------------------------------------
# Logger END
# -------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------
# ProgramProgress BEG
# App context specific statistics wrapper
# Time is calculated in 1 second resolution
# -------------------------------------------------------------------------------------------------
class ProgramProgress(object):
    __start_time = None


    def __init__(self, start_time = None):
        Log.debug('CTR>ProgramProgress')
        self.set_start_time(start_time)
        self.im_generated = 0
        self.im_drawn = 0
        self.im_ignored = 0


    def get_now_time(self):
        return time.time()

    def get_start_time(self):
        return self.__start_time

    def set_start_time(self, time = None):
        if time is None:
            self.__start_time = self.get_now_time()
        else:
            self.__start_time = time


    def get_elapsed_time(self):
        start = self.get_start_time()
        now = self.get_now_time()
        elapsed = now - start
        return elapsed

    def inc_im_generated(self):
        self.im_generated += 1
    def inc_im_drawn(self):
        self.im_drawn += 1
    def inc_im_ignored(self):
        self.im_ignored += 1


    def get_time_str(self):
        time = format(self.get_elapsed_time(), '.3g')
        return ('Elapsed time: ' + time + ' sec')

    def percentage(self, part, whole):
        if(whole > 0):
            return 100 * float(part) / float(whole)
        else:
            return 0

    def get_image_status(self):
        try:
            percent = self.percentage(self.im_ignored, self.im_generated)
            msg = ('Generated Images: Total=' +
                   str(self.im_generated) +
                   ', Drawn=' + str(self.im_drawn) + ' ' +
                   ', Ignored=' + str(self.im_ignored) + ' (' +
                    str(percent) + '%)')
        except Exception as e:
            Log.exception(str(e))
        return msg


    def cpu_str(self):
        cpu = psutil.cpu_percent()
        return ('CPU: ' + str(cpu) + '%')


    def memory_str(self):
        percent = psutil.virtual_memory()
        return ('Memory: ' + str(percent) + '%')

    def get_all_stats(self):
        return self.get_time_str() + " " + self.memory_str() + " " + self.cpu_str()

    def get_stats_4GUI(self):
        return self.get_time_str() + ' ' + self.get_image_status()


Progress = ProgramProgress()
# -------------------------------------------------------------------------------------------------
# ProgramProgress END
# -------------------------------------------------------------------------------------------------





