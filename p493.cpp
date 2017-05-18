#include<stdlib.h>
#include <stdio.h>
#include <vector>
using namespace std;

typedef struct NODE{
  int count;
  int fix;
  int val;
  struct NODE* lchild;
  struct NODE* rchild;
} Node;

Node* new_node(int val){
    Node* node = new Node;
    node->val = val;
    node->fix = rand();
    node->count = 1;
    node->lchild = node->rchild = NULL;
    return node;
}

int update_count(Node* node){
  int total = 1;
  if (node->lchild != NULL)
    total += node->lchild->count;
  if (node->rchild != NULL)
    total += node->rchild->count;
  node->count = total;
  return total;
}

Node* rotateLeft(Node* node, Node* rc){
  node->rchild = rc->lchild;
  rc->lchild = node;
  update_count(node);
  return rc;
}
Node* rotateRight(Node* node, Node* lc){
  node->lchild = lc->rchild;
  lc->rchild = node;
  update_count(node);
  return lc;
}

Node* insert_to_node(Node* node, int val){
  if (val < node->val){
    if (node->lchild == NULL){
      node->lchild = new_node(val);
    }else{
      node->lchild = insert_to_node(node->lchild, val);
    }
    if (node->lchild->fix < node->fix){
      node = rotateRight(node, node->lchild);
    }
  }else{
    if (node->rchild == NULL){
      node->rchild = new_node(val);
    }else{
      node->rchild = insert_to_node(node->rchild, val);
    }
    if (node->rchild->fix < node->fix){
      node = rotateLeft(node, node->rchild);
    }
  }
  update_count(node);
  return node;
}

Node* insert(Node* root, int val){
  if (root == NULL){
    return new_node(val);
  }
  return insert_to_node(root,val);
}

int show_node(Node* node,int depth,char lr){
  if (node == NULL){
    return -1;
  }
  printf("%d-%c %d\n", depth, lr, node->val);
  if (node->lchild != NULL){
    show_node(node->lchild, depth+1, 'l');
  }
  if (node->rchild != NULL){
    show_node(node->rchild, depth+1, 'r');
  }
  return 0;
}

int greater_than(Node* root,long long val){
  Node* node = root;
  int result = 0;
  while (node != NULL){
    if (val < node->val){
      result += 1;
      if (node->rchild != NULL)
        result += node->rchild->count;
      node = node->lchild;
    }else{
      node = node->rchild;
    }
  }
  return result;
}

class Solution {
public:
    int reversePairs(vector<int>& nums) {
      int result = 0;
      Node* root = NULL;
      for (int i=0;i<nums.size();i++){
          int num = nums[i];
          int count = greater_than(root, 2*(long long)num);
          root = insert(root, num);
          //printf("%d : %d\n", num, count);
          //show_node(root, 0, 'c');
          result += count;
      }  
      return result;
    }
};

int main(){
  vector<int> v;
  int x;
  while (EOF!= scanf("%d\n", &x)){
    v.push_back(x);
    //printf("%d\n", x);
  }
  Solution solu;
  int result = solu.reversePairs(v);
  printf("%d\n", result);
  return 0;
}
