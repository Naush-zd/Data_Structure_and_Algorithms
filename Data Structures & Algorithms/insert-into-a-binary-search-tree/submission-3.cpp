/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(!root){
            return new TreeNode(val);
        }
        TreeNode* cur = root;
        while(true){
            if (val > cur->val) {
                if (!cur->right) {
                    cur->right = new TreeNode(val);
                    return root;
                }
                cur = cur->right;
            } else {
                if (!cur->left) {
                    cur->left = new TreeNode(val);
                    return root;
                }
                cur = cur->left;
            }


        }
    }
};