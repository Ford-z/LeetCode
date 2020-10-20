//*给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        if(head==nullptr){
            return;
        }
        vector<ListNode*> vec;
        ListNode* cur = head;
        while(cur){//进入队列
            vec.push_back(cur);
            cur=cur->next;
        }
        int left = 0;
        int right = vec.size() - 1;
        while(left<right){
            vec[left]->next=vec[right];
            vec[right]->next=vec[left+1];
            right-=1;
            left+=1;
        }
        vec[left]->next=nullptr;
    }
};
