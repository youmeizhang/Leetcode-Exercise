/** credit to: https://www.jianshu.com/p/7118b50696eb?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation */

class MaxStack {
    private Stack<Integer> stack;
    private PriorityQueue<Integer> pq;
    
    /** initialize your data structure here. */
    public MaxStack() {
         stack = new Stack<Integer>();
         pq = new PriorityQueue<Integer>(10000, Collections.reverseOrder());
    }
    
    public void push(int x) {
        stack.push(x);
        pq.offer(x);
    }
    
    public int pop() {
        int top = stack.pop();
        pq.remove(top);
        return top;
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int peekMax() {
        return pq.peek();
    }
    
    public int popMax() {
        int max = pq.poll();
            
        Stack<Integer> tmp = new Stack<Integer>();
        while (stack.peek() != max)
            tmp.push(stack.pop());
        
        stack.pop();
        while (!tmp.empty())
            stack.push(tmp.pop());
        
        return max;
        
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */
