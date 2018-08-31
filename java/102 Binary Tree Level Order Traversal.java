class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        levelRecursion(root, result, 0);
        return result;
    }
    
    public void levelRecursion(TreeNode node, List<List<Integer>> result, int level) {
        if (node == null) {
            return;
        }
        if (result.size() < level + 1) {
            result.add(new ArrayList<Integer>());
        }
        result.get(level).add(node.val);
            
        levelRecursion(node.left, result, level + 1);
        levelRecursion(node.right, result, level + 1);
            
            
    }
}
