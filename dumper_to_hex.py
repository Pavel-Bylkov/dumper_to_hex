#!/usr/bin/python3.10

import sys
import getopt
import ntpath


def _path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def dump(filename, to=None):
    try:
        print("Start dump for", from_, "to", end=" ")
        with open(filename, 'rb') as file:
            res = "".join([str(hex(b)).upper()[2:].rjust(2, '0') for b in file.read()])
            if to is None:
                to = _path_leaf(filename) + ".txt"
            print(to)
            with open(to, 'w') as f:
                f.write(res)
    except Exception as e:
        print("Error", e)


def load(filename, to=None):
    try:
        print("Start load for", from_, "to", end=" ")
        with open(filename, 'r') as file:
            res = b""
            chunk = file.read(2)
            while chunk:
                res += (int(chunk, 16)).to_bytes(1, byteorder=sys.byteorder)
                chunk = file.read(2)
            if to is None:
                name = _path_leaf(filename)
                to = name[:-4] + name[-4:].replace(".txt", "")
            print(to)
            with open(to, 'wb') as f:
                f.write(res)
    except Exception as e:
        print("Error", e)


if __name__ == "__main__":
    from_ = ""
    to = None
    argv = sys.argv[1:]
    action = "dump"
    options, args = getopt.getopt(argv, "dls:o:",
                                  ["dump", "load", "src=",
                                   "out="])
    for name, value in options:
        if not from_ and name in ['-s', '--src']:
            from_ = value
        elif to is None and name in ['-o', '--out']:
            to = value
        elif name in ['-d', '--dump']:
            action = "dump"
        elif name in ['-l', '--load']:
            action = "load"
    if from_ == "" and len(args):
        from_ = args[0]

    if from_ != "":
        if action == "dump":
            dump(from_, to)
        elif action == "load":
            load(from_, to)
        print("Convert completed for", from_)
    else:
        print("Help for Dumper to HEX\n")
        print('\t-d --dump Default action - create txt file with HEX code')
        print('\t-l --load Read txt file with HEX code and create ')
        print('\t-s --src Source file or path')
        print('\t-o --out Output file or path')
        print()
        print('Example: ')
        print('python dumper_to_hex.py app.exe')
        print('result - app.exe.txt')
        print('python dumper_to_hex.py -d -s app.exe')
        print('result - app.exe.txt')
        print('python dumper_to_hex.py -d -s app.exe -o out.txt')
        print('result - out.txt')
        print('python dumper_to_hex.py -l -s app.exe.txt -o out.exe')
        print('result - out.exe')
        print('python dumper_to_hex.py -l -s app.exe.txt')
        print('result - app.exe')
