class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> m;
        map<string, vector<string>>::iterator it;
        vector<vector<string>> res;

        for (int i = 0; i < strs.size(); i++) {
            string s = strs[i];
            sort(s.begin(), s.end());
            m[s].push_back(strs[i]);
        }

        for (it = m.begin(); it != m.end(); it++) {
            res.push_back(it->second);
        }
        return res;
    }
};