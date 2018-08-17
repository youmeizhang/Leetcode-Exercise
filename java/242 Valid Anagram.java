class Solution {
    public boolean isAnagram(String s, String t) {
        int[] s0 = new int[26];
        int[] t0 = new int[26];
        int m = s.length();
        int n = t.length();
        if (m != n) {
            return false;
        }
        for (int i = 0; i < m; i++) {
            char s1 = s.charAt(i);
            ++s0[s1-'a'];
        }

        for (int i = 0; i < n; i++) {
            char t1 = t.charAt(i);
            ++t0[t1-'a'];
        }

        if (Arrays.equals(s0, t0)) {
            return true;
        }
        return false;
    }
}
