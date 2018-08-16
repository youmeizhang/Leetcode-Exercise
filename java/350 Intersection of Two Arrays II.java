class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        List<Integer> tmp = new ArrayList<Integer>();
        List<Integer> res = new ArrayList<Integer>();

        for (int num : nums1) {
            tmp.add(num);
        }

        for (int i = 0; i < nums2.length; i++) {
            if (tmp.contains(nums2[i])) {
                res.add(nums2[i]);
                tmp.remove(tmp.indexOf(nums2[i]));
            }
        }
        
        int[] ans = new int[res.size()];
        int cnt = 0;
        for (int num : res) {
            ans[cnt++] = num;
        }
        return ans;
    }
}
