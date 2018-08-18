class Solution {
    public int myAtoi(String str) {
        str = str.trim();
        int n = str.length();
        if (n < 1 || str == null) return 0;
        double ans = 0;
        int sign = 1;
        int i = 0;
        if (str.charAt(0) == '-') {
            sign = -1;
            i++;
        }else if(str.charAt(0) == '+') {
            sign = 1;
            i++;
        }
        while (str.length() > i && str.charAt(i) >= '0' && str.charAt(i) <= '9') {
            ans = ans * 10 + (str.charAt(i) - '0');
            i++;
        }
        ans = ans * sign;

        if (ans > Integer.MAX_VALUE) return Integer.MAX_VALUE;
        if (ans < Integer.MIN_VALUE) return Integer.MIN_VALUE;

        return (int) ans;
    }
}
