/** credit to: https://leetcode.com/problems/design-hashset/discuss/143434/Beats-100-Real-Java-Solution-(Not-boolean-array)*/

class MyHashSet {
    
    private int buckets = 1000;
    private int itemPerBucket = 1001;
    private boolean[][] table;
    
    /** Initialize your data structure here. */
    public MyHashSet() {
        table = new boolean[buckets][];
    }
    
    public int hash(int key) {
        return key % buckets;
    }
    
    public int pos(int key) {
        return key / itemPerBucket;
    }
        
    public void add(int key) {
        int hashKey = hash(key);
        if (table[hashKey] == null) {
            table[hashKey] = new boolean[itemPerBucket];
        }
        table[hashKey][pos(key)] = true;
    }
    
    public void remove(int key) {
        int hashKey = hash(key);
        if (table[hashKey] != null) {
            table[hashKey][pos(key)] = false;
        }   
    }
    
    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        int hashKey = hash(key);
        return table[hashKey] != null  && table[hashKey][pos(key)];
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
