/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* new_node(int x){
    struct TreeNode* temp=(struct TreeNode*)malloc(sizeof(struct TreeNode));
    temp->val=x;
    temp->left=NULL;
    temp->right=NULL;
    return temp;
} 
struct TreeNode* insertIntoBST(struct TreeNode* root, int x) {
    if(root==NULL){
        root=new_node(x);
        return root;
    }
    else if(x > root->val){
        root->right=insertIntoBST(root->right,x);
    }
    else{
        root->left=insertIntoBST(root->left,x);
    }
    return root;
}