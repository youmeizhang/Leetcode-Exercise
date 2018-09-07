class Solution {
    public int hammingDistance(int x, int y) {
        int i = x ^ y;
        int res = 0;
        // System.out.print(i);
        while(i != 0) {
            ++ res;
            i = (i - 1) & i;
        }
        return res;
    }
}
