class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # convert n to binary
        remainder = 0
        quotient = n
        bn = []
        pos = 0
        while pos <32 or quotient != 0:
            if quotient!=0:
                remainder = quotient % 2
                quotient = int(quotient/2)
                bn.append(remainder)
            elif pos<32:
                bn.append(0)
            pos +=1
        reverse_n = bn[-1::-1]
        sum = 0
        level = 0
        for i in range(len(reverse_n)):
            s = int(reverse_n[i])
            sum += s*(2**level)
            level+=1
        return sum

        # reverse n to reverse_n
        # convert reverse_n to integer


s = Solution()
b = 43261596
print(s.reverseBits(b))
