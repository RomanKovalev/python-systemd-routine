"""
Script to collect the number of failed logins in the last hour.
Use Python 2 and python-systemd (https://github.com/systemd/python-systemd)

Author Roman Kovalev (https://github.com/RomanKovalev)
"""

from systemd import journal
import time

def get_failed_logins_count():
    j = journal.Reader()                        # Create object to access systemd journal entries
    j.add_match(SYSLOG_FACILITY=10)             # Set filter SYSLOG_FACILITY=10
    j.add_match(PRIORITY=5)                     # Set filter PRIORITY=5
    j.seek_realtime(time.time() - 60**2)        # Seek journal records for the last hour
    count_list = [entry['_PID'] for entry in j] # Add every journal object record field "_PID" to  count_list
    return len(set(count_list))                 #  Choose only unique PID in counter and return quantity of it


def main():
    get_failed_logins_count()

if __name__=='__main__':
    main()

