class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            pass
        else:
            self.stack = self.stack[:-1]

    def top(self):
        """
        :rtype: int
        """
        l = len(self.stack)
        if l ==0:
            return 0
        else:
            return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        l = len(self.stack)
        if l ==0:
            return 0
        else:
            m = self.stack[0]
            for i in range(l):
                if m > self.stack[i]:
                    m = self.stack[i]
            return m

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# val = 3
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
a1=minStack.getMin()
a2=minStack.pop()
a3=minStack.top()
a4=minStack.getMin()

print("{}, {}, {}, {}".format(a1,a2,a3,a4))