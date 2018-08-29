
// credit to: awangdev

class Solution {
    public boolean isValidBST(TreeNode root) {
        return valid(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    public boolean valid(TreeNode node, long MIN, long MAX){
        
        if (node == null) return true;
        
        if(node.val > MIN && node.val < MAX && valid(node.left, MIN, node.val) &&
          valid(node.right, node.val, MAX)) {
              return true;
          } else {
            return false;
        }
    }
}
