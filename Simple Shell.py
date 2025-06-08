"""
Simple Shell in Python

Supports basic commands: ls, pwd, cd, exit.

"""

import os
import shlex
import subprocess

def simple_shell():
    while True:
        cwd = os.getcwd()
        cmd_input = input(f"{cwd} $ ")
        if cmd_input.strip() == '':
            continue
        args = shlex.split(cmd_input)
        cmd = args[0]

        if cmd == 'exit':
            print("Bye!")
            break
        elif cmd == 'cd':
            try:
                os.chdir(args[1])
            except Exception as e:
                print(e)
        else:
            try:
                subprocess.run(args)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    simple_shell()
