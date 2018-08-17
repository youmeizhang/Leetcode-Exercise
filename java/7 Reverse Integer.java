class Solution {
    public int reverse(int x) {
        if (x == Integer.MIN_VALUE) {
            return 0;
        }
        int num = Math.abs(x);
        int ans = 0;
        
        while(num != 0) {
            if (ans > (Integer.MAX_VALUE - num % 10) / 10) {
                return 0;
            }
            ans = ans * 10 + num % 10;
            num /= 10;
        }
        return x > 0 ? ans : -ans;
    }
}
