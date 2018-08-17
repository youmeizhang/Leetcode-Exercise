class Solution {
    public boolean isPalindrome(String s) {
        int n = s.length();
        if (n == 0) {
            return true;
        }

        s = s.toUpperCase();
        int left = 0;
        int right = n - 1;

        while (left < right) {
            while (left < right && !isValid(s.charAt(left))) {
                left++;
            }
            while (left < right && !isValid(s.charAt(right))) {
                right--;
            }
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    public static boolean isValid(char c) {
        if ('a' <= c && c <= 'z' || 'A' <= c && c <= 'Z') return true;
        if ('0' <= c && c <= '9') return true;
        return false;
    }
}
