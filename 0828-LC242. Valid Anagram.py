class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        # add s and count in dictionary
        for a in s:
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1

        # deduct t and count in dictionary
        for b in t:
            if b in d:
                if d[b] <= 0:
                    return False
                else:
                    d[b] -= 1
            else:
                return False
        # check d is 0
        if all(value == 0 for value in d.values()):
            return True
        else:
            return False


        # m2 with C++
'''
https://leetcode.com/problems/valid-anagram/discuss/66519/2-C%2B%2B-Solutions-with-Explanations

        class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        int n = s.length();
        unordered_map<char, int> counts;
        for (int i = 0; i < n; i++) {
            counts[s[i]]++;
            counts[t[i]]--;
        }
        for (auto count : counts)
            if (count.second) return false;
        return true;
    }
};
'''

s = Solution()
# a = "anagram"
# b = "nagaram"
a= "ab"
b="a"
print(s.isAnagram(a,b))

