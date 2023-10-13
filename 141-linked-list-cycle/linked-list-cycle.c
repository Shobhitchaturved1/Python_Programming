/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *slow=head;
    if (head==NULL || head->next==NULL ){
        return false;
    }
    struct ListNode *fast=head->next;
    
    while(fast && fast->next){
        if(slow==fast){
            return true;
        }
        slow=slow->next;
        fast=fast->next->next;
    }
    return false;
    
}