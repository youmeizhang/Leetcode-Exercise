class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        
        int j = 1;
        int prev = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == prev) {
                continue;
            }else {
                nums[j] = nums[i];
                j += 1;
                prev = nums[i];
            }
        }
        return j;
    }
};
