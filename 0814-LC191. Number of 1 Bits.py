class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # convert n to binary
        # m1
        remainder = 0
        quotient = n
        pos = 0
        count = 0
        while quotient != 0:
            remainder = quotient % 2
            quotient = int(quotient / 2)
            if remainder == 1:
                count += 1
            pos += 1
        """
         public static int hammingWeight(int n) {
             int ones = 0;
                 while(n!=0) {
                     ones = ones + (n & 1);
                     n = n>>>1;
                 }
                 return ones;
         }
         """
        return count


s = Solution()
n = 11
print(f"test: {s.hammingWeight(n)}")