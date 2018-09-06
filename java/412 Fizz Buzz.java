class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> res = new ArrayList<String>(n);
        for (int i = 0; i < n; i++) {
            if ((i+1) % 3 == 0 && (i+1) % 5 ==0) res.add("FizzBuzz");
            else if ((i+1) % 3 == 0) res.add("Fizz");
            else if ((i + 1) % 5 == 0) res.add("Buzz");
            else res.add(Integer.toString(i+1));
        }
        return res;
    }
}
