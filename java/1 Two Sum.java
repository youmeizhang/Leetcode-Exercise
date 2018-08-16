class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];

        List<Integer> list = new ArrayList<Integer>();
        for (int i : nums) {
            list.add(i);
        }

        for (int i = 0; i < list.size(); i++) {

            int tmp = list.indexOf(target - nums[i]);

            if (tmp != -1 && tmp != i) {
                res[0] = i;
                res[1] = tmp;
                break;
            }
        }
        return res;
    }
}
