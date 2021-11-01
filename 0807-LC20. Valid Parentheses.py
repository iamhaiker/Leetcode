class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        stack
        a:()
        b:{}
        c:[]
        s = {()}
        s = {{}()}
        b
        a
        for
            if (,{,[, put into stack
            if ).},], pop out of stack
                if stack ==empty, return false 
        if a,b,c are empty, return true
        '''

        d = []
        for i in range(len(s)):
            w = s[i]

            try:
                if w ==")":
                    k = d.pop()
                    if k != "(":
                        return False

                elif w =="}":
                    k = d.pop()
                    if k != "{":
                        return False

                elif w =="]":
                    k = d.pop()
                    if k != "[":
                        return False
                else:
                    d.append(w)

            except IndexError as err:
                print("Error =={}".format(err))
                return False

        if d:
            return False
        else:
            return True
            # print("{}a:{}".format(i,a))
            # print("b:{}".format(b))
            # print("c:{}".format(c))

s = Solution()
# t = "([)]"
t = "{{}()}"
print(s.isValid(t))