/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {//运用floyd算法（My60SHA曾经用过）
        if (head == NULL || head->next == NULL) {
            return NULL;
        }
        ListNode*tortoise = head;
        ListNode*hare = head;

        while(hare != NULL && hare->next != NULL){
            tortoise=tortoise->next;
            hare=hare->next->next;
            if (tortoise == hare){
                break;
            } 
        }
        if (tortoise != hare){
            return NULL;
        } 
        ListNode*temp1=head;
        ListNode*temp2=tortoise;
        while(temp1!=temp2){
            temp1=temp1->next;
            temp2=temp2->next;
        }
        return temp1;
    }
};
