class Solution {
    public void rotate(int[] nums, int k) {
        int tmp = k % nums.length;
        reverse(nums, 0, nums.length - tmp - 1);
        reverse(nums, nums.length - tmp, nums.length - 1);
        reverse(nums, 0, nums.length - 1);
    }
    
    public void reverse(int[] nums, int s, int e) {
        for (int i = s, j = e; i < j; i++, j--) {
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
    }
}
