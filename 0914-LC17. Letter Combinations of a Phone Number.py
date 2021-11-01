class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        '''
        dict to map key: 1 (number), values: [a,b,c] (chars)
        compute the combinations of chars given number
        
        m1: recursion? like a tree
            ans = []
            def m1(s):
                if s[1] is None:
                    return
                else:
                    ans.append(s[0])
                    m1(s[1])
        similar to create a graph and do  BFS  
        r   > a > d
                > e
                > f
            > b
            > c
        digits
            [2,3] [3]
        g:
            b[a]=[d]
            b[a]=[d,e]
                          
        m2: for v1
                for v2
            cons: not scalable
        
        '''
        d = dict()
        d['1'] = ['0', '1']
        d['2'] = ['a', 'b']
        d['3'] = ['e', 'f']
        # d['2']=['a','b','c']
        # d['3']=['e','f','g']
        digits = "123"
        g = dict()
        # self.create_graph(digits, d, g)

        d_list = [
            ['0', '1'],
            ['a', 'b'],
            ['e', 'f']
        ]
        self.tree(d_list,0,'',[])
        return g

    def tree(self, d_list, level, ans, ans_list):
        if level >= len(d_list):
            ans_list.append(ans)
            return
        for l in d_list[level]:
                level += 1
                ans += l
                self.tree(d_list, level, ans, ans_list)


    # def bfs(self,g):
    #     visited = [False] * (max())

    def create_graph(self, digits, d, g):
        if digits is "":
            return ""
        elif len(digits) == 1:
            s = digits[0]  # 3
            vals = d[s]  # d,e,f
            return vals
        else:
            s = digits[0]  # 2
            vals = d[s]  # a,b,c
            for c in vals:
                g[c] = self.create_graph(digits[1:], d, g)  # 3

        # return g


'''
d_list = [
    ['0','1'],
    ['a', 'b'],
    ['e', 'f']
]
'''





s = Solution()
digits = "123"
print(s.letterCombinations(digits))
