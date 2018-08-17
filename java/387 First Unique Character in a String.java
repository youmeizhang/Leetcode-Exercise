class Solution {
    public int firstUniqChar(String s) {
        int[] tmp = new int[26];
        int ans = -1;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            ++tmp[c - 'a'];
        }

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (tmp[c-'a'] == 1) {
                ans = i;
                break;
            }
        }
        return ans;
    }
}
