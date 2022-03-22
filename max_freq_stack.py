# https://leetcode.com/problems/maximum-frequency-stack/


class FreqStack:

    def __init__(self):
        self.d_stack = {}
        self.d_freq = {}
        self.max_lvl = 0

    def push(self, val: int) -> None:
        lvl = self.d_freq.get(val, 0)
        self.d_stack.setdefault(lvl+1, [])
        self.d_stack[lvl+1].append(val)
        self.d_freq[val] = lvl + 1
        self.max_lvl = max(self.max_lvl, lvl + 1)

    def pop(self) -> int:
        popped = self.d_stack[self.max_lvl].pop()
        self.d_freq[popped] -= 1
        if not len(self.d_stack[self.max_lvl]):
            self.max_lvl -= 1

        return popped


if __name__ == '__main__':
    fs = FreqStack()
    # fs.push(5)
    # fs.push(7)
    # fs.push(5)
    # fs.push(7)
    # fs.push(4)
    # fs.push(5)
    # print(fs.pop())
    # print(fs.pop())
    # print(fs.pop())
    # print(fs.pop())
    fs.push(1)
    fs.push(2)
    fs.push(3)
    fs.push(4)
    fs.push(5)
    fs.push(6)
    fs.push(7)
    print(fs.pop())
    print(fs.pop())
    fs.push(1)
    fs.push(2)
    fs.push(3)
    fs.push(4)
    fs.push(5)
    fs.push(6)
    fs.push(7)
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
