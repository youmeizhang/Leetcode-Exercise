class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0, j = 0;
        int n = nums.length;
        for (i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nums[j] = nums[i];
                j++;
            }
        }

        for(; j < n; j++) {
            nums[j] = 0;
        }  
    }
}
