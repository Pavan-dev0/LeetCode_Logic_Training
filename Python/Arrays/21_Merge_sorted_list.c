#include<stdio.h> 
#include<stdlib.h> 

// Define the structure for a singly linked list node
struct ListNode {
    int val;
    struct ListNode *next;
};

/**
 * Definition for singly-linked list.
 * struct ListNode {
 * int val;
 * struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) { 
    if(list1==NULL){ 
        return list2; 
    } 
    if(list2==NULL){ 
        return list1; 
    } 
    if(list1->val <=list2->val){ 
        list1->next=mergeTwoLists(list1->next,list2); 
        return list1; 
    } 
    else{ 
        list2->next=mergeTwoLists(list1,list2->next); 
        return list2; 
    } 
}
