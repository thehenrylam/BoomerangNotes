import time
import daemon
import webbrowser
import datetime
import pause

class Alarm:

    PATH_TO_ERROR = '/app/template/error.html'

    def __init__(self):
        self.trigger_datetime = None

        self.working_dir = ""

        self.path_to_reminder = ""

    def __repr__(self):
        output = '<Alarm for {} with {} sec delay>'.format(self.working_dir, self.sec_to_trigger)
        return output

    def start(self):
        with daemon.DaemonContext():
            self._begin_alarm_daemon(
                    self.trigger_datetime,
                    self.working_dir + self.path_to_reminder,
                    self.working_dir + Alarm.PATH_TO_ERROR)
        
    def _begin_alarm_daemon(self, 
            trigger_datetime, 
            full_path_to_reminder,
            full_path_to_error):

        pause.until(trigger_datetime)

        try:
            webbrowser.open_new(full_path_to_reminder)
        except:
            webbrowser.open_new(full_path_to_error)

        exit()


