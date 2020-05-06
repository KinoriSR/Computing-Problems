#include <iostream>

struct ListNode {
     int val;
     ListNode *next;
    //  ListNode(int x) : val(x), next(NULL) {}
 };

// what is this: ptr->next=l1?l1:l2;
class Solution {
public:
    ListNode* mergeTwoLists_better(ListNode* l1, ListNode* l2) {
        ListNode head(0);
        ListNode* ret = &head;
        while(l1!=NULL && l2!=NULL){
            if (l1->val <= l2->val){
                ret->next=l1;
                l1=l1->next;
            }
            else{
                ret->next=l2;
                l2=l2->next;
            }
            ret=ret->next;
        }
        if (l1==NULL){
            ret->next=l2;
        }
        else {
            ret->next=l1;
        }
        return head.next;
        // what is this: ptr->next=l1?l1:l2;
    }
};

// recursive - faster than iterative in this case
class Solution {
public:
    ListNode* mergeTwoLists_recursive(ListNode* l1, ListNode* l2) {
        if (l1==NULL){
            return l2;
        }
        else if (l2==NULL){
            return l1;
        }
        if (l1->val < l2->val){
            l1->next = mergeTwoLists(l1->next,l2);
            return l1;
        }
        else{
            l2->next = mergeTwoLists(l1,l2->next);
            return l2;
        }
    }
};

class Solution {
public:
    ListNode* mergeTwoLists_worse(ListNode* l1, ListNode* l2) {
        // handle empty lists
        if (l1 == NULL & l2 == NULL){
            return NULL;
        }
        else if (l1 == NULL){
            return l2;
        }
        else if (l2 == NULL){
            return l1;
        }
        else{
            ListNode* head;
            ListNode* ret;
            if (l1->val <= l2->val){
                ret = l1;
                if (l1-> next != NULL){
                    l1 = l1->next;
                }
                else{
                    ret->next=l2;
                    return ret;
                }
            }
            else{
                ret = l2;
                if (l2->next != NULL){
                    l2 = l2->next;
                }
                else{
                    ret->next=l1;
                    return ret;
                }
            }
            head = ret;
            while (l1 != NULL & l2 != NULL){
                if (l1->val <= l2->val){
                    ret->next = l1;
                    if (l1->next != NULL){
                        l1 = l1->next;
                    }
                    else{
                        ret = ret->next;
                        ret->next = l2;
                        break;
                    }
                    ret = ret->next;

                }
                else{
                    ret->next = l2;
                    if (l2->next != NULL){
                        l2 = l2->next;    
                    }
                    else{
                        ret = ret->next;
                        ret->next = l1;
                        break;
                    }
                    ret = ret->next;
                }
            }
            return head;
        }
    }
};