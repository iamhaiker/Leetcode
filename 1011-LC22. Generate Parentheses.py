# https: // leetcode.com / problems / generate - parentheses / submissions /
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''
        brute force
        
        def checkValidParen():
        
        def permutateParen():
            
            if checkValidParen():
                ans.append
        '''
        list = ['(']*n+[')']*n
        # turn ['()'] to ['(',')']
        # list = ['(',')']
        parens = self.permutateParen(list)
        # parens_set = set(parens)
        ans = []
        # clean duplicate parens
        s = set()
        for p in parens:
            tp = tuple(p)
            if tp not in s:
                s.add(tp)
        txt=''
        for paren in s:
            if self.checkValidParen(paren):
                # [['(', ')']] to ["()"]
                # for p in paren:
                for s in paren:
                    txt+=s
                ans.append(txt)
                txt = ''
        return ans


    def permutateParen(self, lst):

        if len(lst) == 0:
            return []

        if len(lst) == 1:
            return [lst]

        l = []

        for i in range(len(lst)):
            m= lst[i]

            remLst = lst[:i] +lst[i+1:]

            for p in self.permutateParen(remLst):
                l.append([m]+p)
        return l

    def checkValidParen(self, parens):

        stk = []
        for i in range(len(parens)):
            p = parens[i]
            if p == '(':
                stk.append(p)
            else:
                if stk:
                    l = stk.pop()
                else:
                    return False
        return True





# s = Solution()
# n = 4
# print(s.generateParenthesis(n))


# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Driver program to test above function
data = list('123')
for p in permutation(data):
    print(p)