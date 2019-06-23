class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        while (k > 0) {
            int tmp = nums.back();
            nums.pop_back();
            nums.insert(nums.begin(), tmp);
            k -= 1;
        }
    }
};
