#!/usr/bin/python3
'''Reads stdin line by line and computes metrics'''


from sys import stdin

if __name__ == "__main__":
    total_size = 0
    status_code = {}
    possible_status_code = [
        "200", "301", "400", "401", "403", "404", "405", "500"]
    for possible_status in possible_status_code:
        status_code[possible_status] = 0
    counter = 0
    try:
        for x in stdin:
            try:
                args = x.split(" ")
                if len(args) != 9:
                    pass
                if args[-2] in possible_status_codes:
                    status_code[args[-2]] += 1
                if args[-1][-1] == '\n':
                    args[-1][:-1]
                total_size += int(args[-1])
            except:
                pass
            counter += 1
            if counter % 10 == 0:
                print("File size: {}".format(total_size))
                for posible_status in sorted(status_codes.keys()):
                    if status_codes[possible_status] != 0:
                        print("{}: {}".format(
                            possible_status, status_codes[possible_status]))
        print("File size: {}".format(total_size))
        for possible_status in sorted(status_codes.keys()):
            if status_codes[possible_status] != 0:
                print("{}: {}".format(possible_status,
                                      status_codes[possible_status]))
    except KeyboardInterrupt as err:
        print("File size: {}".format(total_size))
        for possible_status in sorted(status_codes.keys()):
            if status_codes[possible_status] != 0:
                print("{}: {}".format(possible_status,
                                      status_codes[possible_status]))
        raise
