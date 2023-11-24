/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int kthSmallest(struct TreeNode* root, int k) {
    void preorder(struct TreeNode* root,int arr[],int *a){
        if(root){
            preorder(root->left,arr,a);
            arr[(*a)++]=root->val;
            preorder(root->right,arr,a);
        }
    }
    int arr[100000];
    int a=0;
    preorder(root,arr,&a);
    return arr[k-1];
}