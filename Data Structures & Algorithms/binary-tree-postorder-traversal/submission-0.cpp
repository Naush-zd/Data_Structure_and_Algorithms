/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> st;
        stack<bool> visited;
        visited.push(false);
        st.push(root);
        while (!st.empty()){
        TreeNode* cur = st.top();
        bool v = visited.top();
        st.pop();
        visited.pop();
        if(cur){
            if(v){
                res.push_back(cur->val);
            }
            else{
                st.push(cur);
                visited.push(true);
                st.push(cur->right);
                visited.push(false);
                st.push(cur->left);
                visited.push(false);

            }
        }
        }
        return res;

    }
};