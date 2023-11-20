/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 struct TreeNode* find_min(struct TreeNode* root)
{
    if(root==NULL){
        return NULL;
    }
    else if(root->left!=NULL){
        return find_min(root->left);
    }
    return root;
}
struct TreeNode* deleteNode(struct TreeNode* root, int x) {
    if(root==NULL){
        return root;
    }
    else if(x > root->val){
        root->right=deleteNode(root->right,x);
    }
    else if(x<root->val)
        root->left=deleteNode(root->left,x);
    else{
        if(root->left==NULL && root->right==NULL){
            free(root);
            return NULL;
        }
        else if(root->left==NULL || root->right==NULL){
            struct TreeNode* temp;
            if(root->left==NULL){
                temp=root->right;
            }
            else{
                temp=root->left;
            }
            free(root);
            return temp;
        }
        else{
            struct TreeNode* temp=find_min(root->right);
            root->val=temp->val;
            root->right=deleteNode(root->right,temp->val);

        }
    }  
    return root;  
}