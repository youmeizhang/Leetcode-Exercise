class TwoSum {
    private ArrayList<Integer> list = new ArrayList<>();
    
    /** Initialize your data structure here. */
    public TwoSum() {
        
    }
    
    /** Add the number to an internal data structure.. */
    public void add(int number) {
        list.add(number);
        Collections.sort(list);
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    public boolean find(int value) {
        int l = 0;
        int r = list.size() - 1;
        while (l < r) {
            if (list.get(l) + list.get(r) == value) {
                return true;
            }
            else if (list.get(l) + list.get(r) > value) {
                r -= 1;
            } else {
                l += 1;
            }
        }
        return false;
    }
}

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * boolean param_2 = obj.find(value);
 */
 
 /** credit to: https://leetcode.com/problems/two-sum-iii-data-structure-design/discuss/52015/Beats-100-Java-Code */
 class TwoSum {
    private ArrayList<Integer> list = new ArrayList<>();
    private HashMap<Integer, Integer> map = new HashMap<>();
    
    /** Initialize your data structure here. */
    public TwoSum() {
        
    }
    
    /** Add the number to an internal data structure.. */
    public void add(int number) {
        if (map.containsKey(number)) {
            map.put(number, map.get(number) + 1);
        } else {
            map.put(number, 1);
            list.add(number);
        }
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    public boolean find(int value) {
        for (int i = 0; i < list.size(); i++ ) {
            int num1 = list.get(i);
            int num2 = value - num1;
            if (num1 != num2 && map.containsKey(num2) || (num1 == num2 && map.get(num1) > 1)) {
                return true;
            }     
        }
        return false;
        
    }
}

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * boolean param_2 = obj.find(value);
 */
