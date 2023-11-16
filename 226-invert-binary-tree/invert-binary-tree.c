/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* invertTree(struct TreeNode* root) {
    if(root==NULL)
        return root;
    if(root->left==NULL && root->right==NULL)
        return root;
    else{
        struct TreeNode* t=root->right;
        root->right=invertTree(root->left);
        root->left=invertTree(t);
        return root;
    }        
}