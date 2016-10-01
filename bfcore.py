#!/usr/bin/env python3
import sys
from sys import argv
from sys import exit

bm = {}


class Stack():
    def __init__(self):
        self.st = []

    def checkempty(self):
        return self.st == []

    def peek(self):
        return self.st[0]

    def size(self):
        return len(self.st)

    def push(self, item):
        self.st.insert(0, item)

    def pop(self):
        return self.st.pop(0)


def check_mem_range(ptr, memory_size):
    if ptr >= memory_size or ptr < 0:
        exit('Segfault!')


def read_program(sourcefile):
    code = []
    with open(sourcefile, 'rb') as sf:
        while True:
            char = sf.read(1)
            if not char or char == b'\n':
                break
            code.append(char)
    return code


def brackets(program):
    st = Stack()
    for i in range(0, len(program) - 2):
        if program[i] == b'[':
            st.push(i)
        elif program[i] == b']':
            if st.checkempty():
                exit('Invalid brackteing, check syntax!')
            bm[i] = st.peek()
            bm[st.peek()] = i
            st.pop()


def main():
    memory_size = 256
    memory = [0] * memory_size
    ptr = 0
    program = []
    if len(argv) < 2:
        exit('BF interpreter. \nUsage: {} sourcefile'.format(argv[0]))
    program = read_program(argv[1])
    #print(program)
    brackets(program)
    i = 0
    while i in range(0, len(program) - 1):
        #print(i)
        char = program[i]
        if char == b'>':
            ptr += 1
            i += 1
            check_mem_range(ptr, memory_size)
        elif char == b'<':
            ptr -= 1
            i += 1
            check_mem_range(ptr, memory_size)
        elif char == b'+':
            memory[ptr] += 1
            i += 1
        elif char == b'-':
            memory[ptr] -= 1
            i += 1
        elif char == b'.':
            print(chr(memory[ptr]), end="")
            i += 1
        elif char == b',':
            memory[ptr] = int(sys.stdin.read(1))
            i += 1
        elif char == b'[':
            if memory[ptr] == 0:
                i = bm[i] + 1
            else:
                i += 1
        elif ']':
            i = bm[i]
        else:
            i += 1


if __name__ == '__main__':
    main()
