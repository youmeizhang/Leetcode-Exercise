class MyQueue {
    private Stack<Integer> s1 = new Stack<Integer>();
    private Stack<Integer> s2 = new Stack<Integer>();
        
    /** Initialize your data structure here. */
    public MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        s1.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        int val = -1;
        int v;
        while (!s1.empty()) {
            val = s1.pop();
            s2.push(val);
        }
        
        s2.pop();
        while (!s2.empty()) {
            v = s2.pop();
            s1.push(v);
        }
        
        return val;
    }
    
    /** Get the front element. */
    public int peek() {
        int val = -1;
        int v;
        while (!s1.empty()) {
            val = s1.pop();
            s2.push(val);
        }

        while (!s2.empty()) {
            v = s2.pop();
            s1.push(v);
        }
        
        return val;
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return s1.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */

/** credit to: https://leetcode.com/problems/implement-queue-using-stacks/discuss/64206/Short-O(1)-amortized-C%2B%2B-Java-Ruby*/

class MyQueue {
    private Stack<Integer> input = new Stack<Integer>();
    private Stack<Integer> output = new Stack<Integer>();
        
    /** Initialize your data structure here. */
    public MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        input.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        peek();
        return output.pop();
        
    }
    
    /** Get the front element. */
    public int peek() {
        if (output.empty())
            while (!input.empty())
                output.push(input.pop());
        return output.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return input.empty() && output.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
