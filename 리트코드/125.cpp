#include <iostream>
#include <string>
#include <ctype.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int len = s.length();
        int p1 = 0, p2 = len - 1;

        while (p1 < p2) {
            if ((isalpha(s[p1]) || isdigit(s[p1])) && (isalpha(s[p2]) || isdigit(s[p2]))) {
                if (tolower(s[p1]) != tolower(s[p2])) return false;
                p1++, p2--;
            }
            else if ((isalpha(s[p1]) || isdigit(s[p1])) && !(isalpha(s[p2]) || isdigit(s[p2]))) p2--;
            else if (!(isalpha(s[p1]) || isdigit(s[p1])) && (isalpha(s[p2]) || isdigit(s[p2]))) p1++;
            else if (!(isalpha(s[p1]) || isdigit(s[p1])) && !(isalpha(s[p2]) || isdigit(s[p2]))) p1++, p2--;
        }
        return true;
    }
};

int main() {
    Solution s;
    cout << s.isPalindrome("0e0e");

}