class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.m2(s)


    def m1(self,s):
        '''
        # brute force O(n^3)
        def iterateStr:
            max_len, i , j

            checkPalindrome

        def checkPalindrome >> Boolean:

        '''
        s_len = len(s)
        max_len = 0
        max_txt = ""
        for i in range(s_len):
            for j in range(i,s_len+1):
                txt = s[i:j]
                isPalindrome = self.checkPalindrome(txt)
                if isPalindrome:
                    if len(txt) > max_len:
                        max_txt = txt
                        max_len = len(txt)
        return max_txt
        # return self.checkPalindrome(s)


    def checkPalindrome(self, txt):
        # stack
        s = []
        # mid_idx
        l = len(txt)
        mid_idx = 0
        if l%2 == 0:
            mid_idx = l/2 -1
        else:
            mid_idx = int(l/2)
        idx = 0
        while idx < l:
            if l%2==0:
                if idx <= mid_idx:
                    s.append(txt[idx])
                else:
                    t = s.pop()
                    if t != txt[idx]:
                        return False
            else:
                if idx < mid_idx:
                    s.append(txt[idx])
                elif idx >mid_idx:
                    t = s.pop()
                    if t!= txt[idx]:
                        return False
            idx+=1
        return True

    max_len = 0
    max_s = ""
    def m2(self,s):
        '''
        :param s:
        :return:

        mid is the center idx of palindrome
        i is idx from the right side of mid, starting from 0
        j is idx from the left side of mid, starting from 0

        m2 pass in mid to extendPalindrome from 0... len(s)
        j... mid ... i
        if s[j] == s[i]:
            j--, i++
        else:
            return i,j and s[i:j] if len(s[i:j]) > max_len
            break
        '''
        s_len = len(s)
        for i in range(s_len):
            self.extendPalindrome(s, i, i)
            self.extendPalindrome(s,i,i+1)
        return self.max_s

    def extendPalindrome(self,s,i,j):

        while i>=0 and j<len(s) and s[i]==s[j]:
            i-=1
            j+=1

        if j-i+1 > self.max_len:
            self.max_len = (j-i+1)
            self.max_s = s[i+1:j]

        # i=0
        # j=0
        # while mid-j>=0 and mid+i<s_len:
        #     # if s_len is odd, eg "abcba"
        #     if s[mid-j] == s[mid+i]:
        #         j+=1
        #         i+=1
        #     else:
        #         break
        #
        # if i+j+1> max_len:
        #     max_len = i+j-1
        #     max_s = s[mid-j+1:mid+i]
        # return max_s, max_len
        #




s = Solution()
t = "abcba"
print(s.longestPalindrome(t))


'''
public class Solution {
private int lo, maxLen;

public String longestPalindrome(String s) {
	int len = s.length();
	if (len < 2)
		return s;
	
    for (int i = 0; i < len-1; i++) {
     	extendPalindrome(s, i, i);  //assume odd length, try to extend Palindrome as possible
     	extendPalindrome(s, i, i+1); //assume even length.
    }
    return s.substring(lo, lo + maxLen);
}

private void extendPalindrome(String s, int j, int k) {
	while (j >= 0 && k < s.length() && s.charAt(j) == s.charAt(k)) {
		j--;
		k++;
	}
	if (maxLen < k - j - 1) {
		lo = j + 1;
		maxLen = k - j - 1;
	}
}}
'''