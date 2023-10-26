import sys
from typing import Any
from collections import deque
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
        self.queue = deque()
    def run(self):
        for command in self.commands:
            result = self.dispatch(command)
            if result is not None:
                print(result)
    def dispatch(self, command):
        match command[0]:
            case "push":
                self.push(command[1])
            case "pop":
                return self.pop()
            case "size":
                return self.size()
            case "empty":
                return self.empty()
            case "front":
                return self.front()
            case "back":
                return self.back()
            case _:
                pass
    def push(self, x):
        self.queue.append(x)
    def pop(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.popleft()
    def size(self):
        return len(self.queue)
    def empty(self):
        match len(self.queue):
            case 0:
                return 1
            case _:
                return 0
    def front(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[0]
    def back(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]
command_processor = CommandProcesser(commands)
command_processor.run()