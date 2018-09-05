class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length <= 1) return 0;
        int n = prices.length;
        int min = prices[0];
        int [] dp = new int[n];
        int res = 0;
        
        for(int i=0; i <n; i++){
            dp[i] = prices[i] - min;
            if (prices[i] < min) min = prices[i];
            if (res < dp[i]) res = dp[i];
        }
        return res;
    }
}
