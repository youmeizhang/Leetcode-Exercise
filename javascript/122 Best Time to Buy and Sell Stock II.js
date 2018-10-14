var maxProfit = function(prices) {
    var res = 0;
    i = 1;
    for (l=prices.length; i<l;i++){
        if (prices[i-1] < prices[i]) {
            res += prices[i] - prices[i-1];
        }
    }
    return res;
};
