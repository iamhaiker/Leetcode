

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max_cur = 0
        # max_sofar = 0
        # price_len = len(prices)
        # for i in range(0, price_len):
        #     max_cur += (prices[i] - prices[i - 1])
        #     max_cur = max(0, max_cur)
        #     max_sofar = max(max_cur, max_sofar)
        # return max_sofar

        min1 = 1000000
        max1 = 0
        for p in prices:
            min1 = min(p, min1)
            max1 = max(max1, p - min1)
        return max1

s = Solution()
prices = [7,1,5,3,6,4]
# prices = [1, 7, 0, 11]
# prices = [7,6,4,3,1]
print(s.maxProfit(prices))



"""
7-1 = 6
max_cur = 6
max_sofar = 6
4-7=-3
max_cur = 3 (6-3)
max_sofar = 6
11-4=7
max_cur = 7
max_sofar = 7
"""

# int
# min = Integer.MAX_VALUE, max = 0;
# for (int c: prices) {
#     min = Math.min(c, min);
# max = Math.max(max, c - min);
# }
# return max;