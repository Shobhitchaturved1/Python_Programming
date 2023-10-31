/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode* temp=head;
    struct ListNode* temp1=head;
    while(temp){
        while(temp && temp1 && temp->val==temp1->val){
            temp=temp->next;
        }
        temp1->next=temp;
        temp1=temp;
        if(temp){
            temp=temp->next;
        }
    }
    return head;
}