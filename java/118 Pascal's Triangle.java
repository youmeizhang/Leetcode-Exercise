class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(numRows == 0) return res;
        
        for (int j = 0; j < numRows; j++) {
            List<Integer> tmp = new ArrayList<Integer>();
            tmp.add(1);
            for (int i = 1; i < j; i++) {
                List<Integer> prev = res.get(j - 1);
                int temp_num = prev.get(i-1) + prev.get(i);
                tmp.add(temp_num);
            }
            if(j != 0) tmp.add(1);
            res.add(tmp);
        }
        return res;
    }
}
