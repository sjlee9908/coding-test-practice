#include <iostream>
#include <vector>
#include <map>
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
    string mostCommonWord(string paragraph, vector<string>& banned) {
        for (int i = 0; i < paragraph.length(); i++) {
            paragraph[i] = tolower(paragraph[i]);
            if (!isalpha(paragraph[i]) && !isdigit(paragraph[i]) && !isspace(paragraph[i])) paragraph[i] = ' ';
        }
        cout << paragraph << endl;
        string s;
        map<string, int> m;
        map<string, int>::iterator it;


        for (int i = 0; i < paragraph.length(); i++) {
            if (paragraph[i] != ' ')
                s += paragraph[i];
            else {
                m[s]++;
                s = "";
            }
        }
        m[s]++;
        m[""] = -1;
        s = "";
        for (int i = 0; i < banned.size(); i++) {
            m[banned[i]] = -1;
        }

        int maxCount = -1;
        for (it = m.begin(); it != m.end(); it++) {
            cout << it->first << ":" << it->second << endl;
            if (maxCount < it->second) {
                maxCount = it->second;
                s = it->first;
            }
        }
        return s;
    }
};

int main() {
    Solution s;
    string ss = "Bob";
    vector<string> v;
    v.push_back("hit");
    cout << s.mostCommonWord(ss, v);

}