/*给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。*/

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head=new ListNode(-1);//存放结果的链表
        ListNode* h=head;//移动指针
        int ans=0;
        int temp=0;
        while(l1!=NULL || l2!=NULL){
            if(l1){
                ans+=l1->val;
                l1=l1->next;
            }
            if(l2){
                ans+=l2->val;
                l2=l2->next;
            }
            if(temp!=0){
                ans++;
            }
            if(ans>=10){
                temp=1;
            }
            else{
                temp=0;
            }
            h->next=new ListNode(ans%10);
            h=h->next;
            ans=0;
        }
        if(temp!=0)
        {
            h->next=new ListNode(1);
        }
        return head->next;
    }
};
