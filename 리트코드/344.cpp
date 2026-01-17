#include <iostream>
#include <vector>
#include <ctype.h>
using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        int len = s.size();
        for (int i = 0; i < s.size() / 2; i++) {
            char tmp;
            tmp = s[i];
            s[i] = s[len - 1 - i];
            s[len - 1 - i] = tmp;
        }
    }
};

int main() {
    Solution s;

}