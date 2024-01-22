#include <iostream>
#include <string>
using namespace std;

int main() {
	string s;
	cin >> s;

	for (int i = 0; i < s.size(); i++) {
		char ex = s[i] - 3;
		if (ex < 'A') ex += 26;
		cout << ex;
	}
}