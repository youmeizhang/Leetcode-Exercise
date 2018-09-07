class Solution {
    public boolean isPowerOfThree(int n) {
        if (n <= 0) return false;
        int i = n;
        int j = 0;
        while(i > 1) {
            j = i % 3;
            i = i / 3;
            if (j != 0) return false;
        }
        return true;
        
    }
}
