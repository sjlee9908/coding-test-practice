#include <iostream>
#include <vector>
#include <ctype.h>
#include <algorithm>
using namespace std;

bool compare(string s1, string s2) {
    if (s1.substr(s1.find(" ")) != s2.substr(s2.find(" ")))
        return s1.substr(s1.find(" ")) < s2.substr(s2.find(" "));
    else
        return s1.substr(0, s1.find(" ")) < s2.substr(0, s2.find(" "));
}



class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        vector<string> alpha;
        vector<string> digit;
        vector<string> res;

        for (int i = 0; i < logs.size(); i++) {
            if (isdigit(logs[i][logs[i].find(" ") + 1])) digit.push_back(logs[i]);
            else alpha.push_back(logs[i]);
        }


        sort(alpha.begin(), alpha.end(), compare);



        for (int i = 0; i < alpha.size(); i++) {
            res.push_back(alpha[i]);
        }
        for (int i = 0; i < digit.size(); i++) {
            res.push_back(digit[i]);
        }

        return res;

    }
};

int main() {
    Solution s;

}