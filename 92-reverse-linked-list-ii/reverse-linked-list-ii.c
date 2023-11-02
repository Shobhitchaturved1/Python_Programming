/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    struct ListNode* dummyNode=(struct ListNode*)malloc(sizeof(struct ListNode));
    dummyNode->val=0;
    dummyNode->next=head;
    struct ListNode* leftprev=dummyNode;
    struct ListNode* cur=head;
    for(int i=0;i<left-1;i++){
        leftprev=cur;
        cur=cur->next;
    }
    struct ListNode* prev=NULL;
    for(int i=0;i<right-left+1;i++){
        struct ListNode* next=cur->next;
        cur->next=prev;
        prev=cur;
        cur=next;
    }
    leftprev->next->next=cur;
    leftprev->next=prev;
    return dummyNode->next;
}