#!/usr/bin/python3
'''
Reads stdin line by line and computes metrics
'''


from sys import stdin

status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0


def log_parsing():
    print("File size: {}".format(total_size))
    for status in sorted(status_code.keys()):
        if status_code[status]:
            print("{}: {}".format(status, status_code[status]))


if __name__ == "__main__":
    counter = 0
    try:
        for line in stdin:
            try:
                line_item = line.split()
                total_size += int(line_item[-1])
                if line_item[-2] in status_code:
                    status_code[line_item[-2]] += 1
            except:
                pass
            if counter == 9:
                log_parsing()
                counter = -1
            counter += 1
    except KeyboardInterrupt:
        log_parsing()
        raise
    log_parsing()
