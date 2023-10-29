/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode *temp=head;
    if (head==NULL){
        return NULL;
    }
    int length=0;
    while(temp!=NULL){
        temp=temp->next;
        length+=1;
    }
    if (length==1){
        return NULL;
    }
    int rem_ind=length-n-1;
    int count=0;
    struct ListNode *temp1=head;
    if(rem_ind==-1){
        return head->next;
    }
    while(count<rem_ind){
        temp1=temp1->next;
        count+=1;
    }
    temp1->next=temp1->next->next;
    return head;

}