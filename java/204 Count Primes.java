class Solution {
    public boolean isPrime(int n) {
        if (n % 2 == 0 && n != 2) return false;
        for (int i = 3; i * i <= n; i+=2) {
            if (n % i == 0) return false;
        }
        return true;
    }
    public int countPrimes(int n) {
        int res = 0;
        for (int i = 2; i < n; i++){
            if (isPrime(i)) {
                // System.out.print(i);
                res += 1;
            }
        }
        return res;
    }
}
