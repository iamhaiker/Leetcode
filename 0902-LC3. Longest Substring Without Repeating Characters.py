class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        for i in
            for j in
                dict count the string s
                if repeated, count len, add len to list break
        return max(len list)
        
        "a"
        '''
        l = len(s)
        d = dict()
        ans_lst = []
        cnt = 0
        if l == 1:
            return 1
        for i in range(l):
            for j in range(i,l):
                w = s[j]
                if w not in d:
                    d[w] = True
                    cnt+=1
                else:
                    ans_lst.append(cnt)
                    cnt=0
                    d=dict()
                    break
        if not ans_lst:
            return 0
        return max(ans_lst)




s = Solution()
t = "aba"
print(s.lengthOfLongestSubstring(t))

'''
i: a
j: max(0,0+1)
map: a:0, b:1, a

   public int lengthOfLongestSubstring(String s) {
        if (s.length()==0) return 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max=0;
        for (int i=0, j=0; i<s.length(); ++i){
            if (map.containsKey(s.charAt(i))){
                j = Math.max(j,map.get(s.charAt(i))+1);
            }
            map.put(s.charAt(i),i);
            max = Math.max(max,i-j+1);
        }
        return max;
    }
'''