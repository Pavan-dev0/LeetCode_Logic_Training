class Solution {
public:
    int smallestBalancedIndex(vector<int>& nums) {
        int n = nums.size();
        long long mod1 = 1e9 + 7;
        long long mod2 = 1e9 + 9;

        vector<long long> suffix_prod1(n + 1, 1);
        vector<long long> suffix_prod2(n + 1, 1);

        for (int i = n - 1; i >= 0; i--) {
            suffix_prod1[i] = (suffix_prod1[i + 1] * (nums[i] % mod1)) % mod1;
            suffix_prod2[i] = (suffix_prod2[i + 1] * (nums[i] % mod2)) % mod2;
        }

        long long current_left_sum = 0;
        for (int i = 0; i < n; i++) {
            long long target1 = suffix_prod1[i + 1];
            long long target2 = suffix_prod2[i + 1];

            if ((current_left_sum % mod1) == target1 && (current_left_sum % mod2) == target2) {
                return i;
            }
            current_left_sum += nums[i];
        }

        return -1;
    }
};