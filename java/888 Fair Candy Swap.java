class Solution {
    public int[] fairCandySwap(int[] A, int[] B) {
        int m = A.length;
        int n = B.length;
        int a = 0;
        int b = 0;
        
        for (int i : A) a += i;
        for (int j: B) b += j;
        int tmp = (a - b) / 2;

        int[] ans = new int[2];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (A[i] - B[j] == tmp) {
                    ans[0] = A[i];
                    ans[1] = B[j];
                    break;
                }
            }
        }
        return ans;

    }
}
