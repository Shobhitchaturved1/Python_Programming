/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    if(root==NULL)
        return 0;
    if(root->left==NULL && root->right==NULL)
        return 1;
    else{    
        int height_left;
        height_left=maxDepth(root->left);
        int height_right;
        height_right=maxDepth(root->right);
        int height;
        if(height_left>height_right)
            height=1+height_left;
        else
            height=1+height_right;    
        return height;    
    }    
}