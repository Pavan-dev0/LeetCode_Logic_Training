class Solution {
public:
    int minOperations(string s) {
        int n = s.length();
        string target = s;
        sort(target.begin(), target.end());

        if (s == target) return 0;
        if (n == 2) return -1;
        if (s[0] == target[0] || s[n - 1] == target[n - 1]) return 1;

        string p = s;
        sort(p.begin(), p.end() - 1);
        sort(p.begin() + 1, p.end());
        if (p == target) return 2;

        string q = s;
        sort(q.begin() + 1, q.end());
        sort(q.begin(), q.end() - 1);
        if (q == target) return 2;

        return 3;
    }
};