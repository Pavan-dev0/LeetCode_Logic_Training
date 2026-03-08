class Solution {
public:
    long long minCost(string s, int encCost, int flatCost) {
        int n=s.length();
        vector<int> pref(n+1,0);

        for(int i=0;i<n;i++){
            pref[i+1]=pref[i]+(s[i]-'0');
        }
        return solve(0,n,pref,encCost,flatCost);
    }

private:
    long long solve(int start, int len, const vector<int>& pref, long long encCost, long long flatCost) {
        long long x = pref[start + len] - pref[start];
        long long base_cost;
        
        if (x == 0) {
            base_cost = flatCost;
        } else {
            base_cost = (long long)len * x * encCost;
        }

        if (len % 2 != 0) {
            return base_cost;
        }

        int half = len / 2;
        long long split_cost = solve(start, half, pref, encCost, flatCost) + 
                               solve(start + half, half, pref, encCost, flatCost);

        return min(base_cost, split_cost);
    }
};