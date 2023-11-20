/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int min_diff;
struct TreeNode *prev_node;

void dfs(struct TreeNode *node) {
    if (!node) return;
    dfs(node->left);

    if (prev_node) {
        int curr_diff = node->val - prev_node->val;
        min_diff = min_diff < curr_diff ? min_diff : curr_diff;
    }
    prev_node = node;

    dfs(node->right);
}

int getMinimumDifference(struct TreeNode* root) {
    prev_node = NULL;
    min_diff = INT_MAX;
    dfs(root);
    return min_diff;
}

    
