class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                break;
            }else{
                digits[i] = 0;
            }
        }

        int[] res;
        if (digits[0] == 0) {
            res = new int[n + 1];
            res[0] = 1;
            for (int i = 1; i < n + 1; i++) {
                res[i] = digits[i - 1];
            }
        }else {
            res = new int[n];
            for (int i = 0; i < n; i++) {
                res[i] = digits[i];
            }
        }
        return res;
    }
}
