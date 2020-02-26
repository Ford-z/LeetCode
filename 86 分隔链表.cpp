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
    ListNode* partition(ListNode* head, int x) {
        ListNode*part1=new ListNode(0);
        ListNode*before=part1;
        ListNode*part2=new ListNode(0);
        ListNode*after=part2;

        while(head!=NULL){
            if(head->val < x){
                before->next=head;
                before=before->next;
            }
            else{
                after->next=head;
                after=after->next;
            }
            head=head->next;//跳到下一元素
        }        
        after->next = NULL;//直接在最后补上即可
        before->next=part2->next;//连接两个链表
        return part1->next;
    }
};
