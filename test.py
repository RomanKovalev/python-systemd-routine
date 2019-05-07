"""
Add failed one login record in journal with bash: type "su" command and input wrong root password.
There is opportunity to make journal records through systemd.journal.sendv() with parameters,
but i choose first way as more organic

Author Roman Kovalev (https://github.com/RomanKovalev)
"""

import unittest
import subprocess
import re

from journal import get_failed_logins_count


class TestJournal(unittest.TestCase):
    def test_counter(self):                         # Function to get failed logins through testing function
        bashCommand = [                             # Prepare command for bash
            'journalctl',
            'SYSLOG_FACILITY=10',
            '--priority=5',
            '--since',
            "1 hour ago",
            '--no-pager'
            ]
        process = subprocess.Popen(                 # Run bash command and capture output
            bashCommand,
            stdout=subprocess.PIPE
        )
        output, error = process.communicate()       # Send command to stdin and receive output string
        result = re.findall(r'\[\d*\]', output)     # Find all [*] parts
        result = len(set(result))                   # Choose only unique strings, count unique ones
        count = get_failed_logins_count()           # Get number of failed logins through testing function
        self.assertEqual(result, count)             # Compare it

if __name__ == '__main__':
    unittest.main()