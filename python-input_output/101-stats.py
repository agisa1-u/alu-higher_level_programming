#!/usr/bin/python3
"""Script that reads stdin line by line and computes log metrics."""
import sys

STATUS_CODES = ("200", "301", "400", "401", "403", "404", "405", "500")


def print_stats(total_size, status_counts):
    """Print the total file size and the number of lines by status code.

    Args:
        total_size: the sum of all the file sizes read so far.
        status_counts: dictionary of status code -> number of lines.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    count = 0
    status_counts = {code: 0 for code in STATUS_CODES}

    try:
        for line in sys.stdin:
            count += 1
            try:
                parts = line.split()
                size = int(parts[-1])
                status = parts[-2]
                total_size += size
                if status in status_counts:
                    status_counts[status] += 1
            except (IndexError, ValueError):
                pass
            if count % 10 == 0:
                print_stats(total_size, status_counts)
        if count == 0 or count % 10 != 0:
            print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
