/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int size;

void inorder(struct TreeNode* root,int *arr){
     if (root->left)
        inorder(root->left,arr);
     arr[(size)++] = root->val;
     if(root->right)
        inorder(root->right,arr);
 }

struct TreeNode* insertRight(struct TreeNode *root, int value){
    if (root == NULL){
        struct TreeNode* newnode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newnode->val = value;
        newnode->left = NULL;
        newnode->right = NULL;
        return newnode;
    } else {
            root->right = insertRight(root->right, value);
    }
    return root;
}
struct TreeNode* increasingBST(struct TreeNode* root) {
    
    struct TreeNode* increaseBST=NULL;

    if ( root == NULL){
        return NULL;
    }
    
    if (root->right == NULL && root->left == NULL)
        return root;

    int *arr=(int*)malloc(sizeof(int)*10000);
    size = 0;
    inorder(root,arr);
    printf("%d",size);

    for (int i = 0;i<size;i++){
        increaseBST = insertRight(increaseBST, arr[i]);
    }

    return increaseBST;
}