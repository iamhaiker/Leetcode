class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        if len(digits) == 0:
            return ans
        mapping = [
            "0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        ]
        ans.append("")
        for i in range(len(digits)):
            x = int(digits[i])
            while len(ans[0])== i:
                t = ans.pop(0)
                for s in mapping[x]:
                    ans.append(t+s)
        return ans




s = Solution()
digits = "23"
print(s.letterCombinations(digits))

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


'''
0
1:
2:abc
3:def
4:ghi
...
https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8064/My-java-solution-with-FIFO-queue

public List<String> letterCombinations(String digits) {
		LinkedList<String> ans = new LinkedList<String>();
		if(digits.isEmpty()) return ans;
		String[] mapping = new String[] {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
		ans.add("");
		for(int i =0; i<digits.length();i++){
			int x = Character.getNumericValue(digits.charAt(i)); //3
			
			while(ans.peek().length()==i){ 1==1
				String t = ans.remove(); //"" t=a ans=""
				for(char s : mapping[x].toCharArray()) //def
					ans.add(t+s);  ""+a = ad, ae, af
			}
		}
		return ans;
	}
'''