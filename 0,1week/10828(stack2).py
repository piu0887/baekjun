import sys
from typing import Any
sys.stdin = open("test.txt", "r")
N = int(sys.stdin.readline())
commands: list[list[Any]] = [sys.stdin.readline().split()
                             for _ in range(N)]
for i in range(len(commands)):
    if len(commands[i]) == 2:
        commands[i][1] = int(commands[i][1])
class CommandProcesser:
    def __init__(self, commands) -> None:
        self.commands = commands
        self.stack = []
    def run(self):
        for command in self.commands:
            self.dispatch(command)
    def dispatch(self, command):
        match command[0]:
            case "push":
                self.push(command[1])
            case "pop":
                print(self.pop())
            case "size":
                print(self.size())
            case "empty":
                print(self.empty())
            case "top":
                print(self.top())
            case _:
                pass
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        try:
            return self.stack.pop()
        except:
            return -1
    def size(self):
        return len(self.stack)
    def empty(self):
        match len(self.stack):
            case 0:
                return 1
            case _:
                return 0
    def top(self):
        try:
            return self.stack[-1]
        except:
            return -1
command_processor = CommandProcesser(commands)
command_processor.run()