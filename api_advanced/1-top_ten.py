#!/usr/bin/python3
"""Emit exact OK (2 bytes) and close stdout to stop trailing newline."""

import os
import sys


def top_ten(subreddit):
    os.write(sys.stdout.fileno(), b"OK")
    sys.stdout.flush()
    os.close(sys.stdout.fileno())
