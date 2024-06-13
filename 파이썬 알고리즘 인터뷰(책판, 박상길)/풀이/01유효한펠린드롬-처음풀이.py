class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list = []
        for i in range(0, len(s)):
            ss = s[i].lower()
            if(ss in "qwertyuiopasdfghjklzxcvbnm1234567890"):
                str_list.append(ss)
        str_list_reversed = list(reversed(str_list))
        print(str_list)
        print(str_list_reversed)
        for i in range(0, len(str_list)):
            if(str_list_reversed[i] != str_list[i]):
                print(str_list[i], str_list_reversed[i])
                return False
        return True

lol =  Solution()
print(lol.isPalindrome("123A man, a plan, a canal: Panama321"))