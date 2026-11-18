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
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        stack<TreeNode*> s;
        unordered_set<TreeNode*> visited;
        unordered_map<TreeNode*, TreeNode*> parents;
        parents[root]= nullptr;
        s.push(root);
        while(!s.empty()){
            TreeNode* node = s.top();
            s.pop();
            if(!node->left && !node->right){
                if (node->val == target) {
                    TreeNode* p = parents[node];
                    if (!p) {
                        return nullptr;
                    }
                    if (p->left == node) {
                        p->left = nullptr;
                    }
                    if (p->right == node) {
                        p->right = nullptr;
                    }
                }
            } else if (visited.find(node) == visited.end()) {
                visited.insert(node);
                s.push(node);
                if (node->left) {
                    s.push(node->left);
                    parents[node->left] = node;
                }
                if (node->right) {
                    s.push(node->right);
                    parents[node->right] = node;
                }
            }
        }

        return root;

        
        
    }
};