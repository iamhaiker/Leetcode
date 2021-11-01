class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        # """
        # price_len = len(prices)
        # accu_min = 100000000
        # accu_max = -1
        # new_min = 10000000
        # new_max = -1
        # total_max = -1
        # for ind, p in enumerate(prices):
        #     accu_min = min(p,accu_min)
        #     accu_max = max(accu_max,p-accu_min)
        #
        #     for q in range(ind+1, price_len):
        #         new_p = prices[q]
        #         new_min = min(new_p,new_min)
        #         new_max = max(new_max,new_p - new_min)
        #         total_max = max(total_max, accu_max+new_max)
        # return total_max

        price_len = len(prices)
        profit = 0
        i=0
        while i < price_len-1:
            while i<(price_len-1) and prices[i+1] <= prices[i]:
                i+=1
            buy = prices[i]
            while i<(price_len-1) and prices[i+1] > prices[i]:
                i+=1
            sell = prices[i]

            profit += (sell - buy)
        return profit



s = Solution()
prices = [7,1,5,3,6,4]
# prices = [1, 7, 0, 11]
# prices = [7,6,4,3,1]
print(s.maxProfit(prices))