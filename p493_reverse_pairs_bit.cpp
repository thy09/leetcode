#include <vector>
#include <iostream>
#include <stdio.h>
    using namespace std;

class BinaryIndexedTree{
private:
    int size;
    int* vals;
    int* sums;
    int lowbit(int num){
        return num & (-num);
    }
    int build_sum(){
        for (int i=1;i<=this->size;i++){
            sums[i] = vals[i];
            int lb = lowbit(i);
            if (lb == 1)
                continue;
            int base = i - lb + (lb>>1);
            for (int idx=i-1; idx>=base; idx-=lowbit(idx)){
                sums[i] += sums[idx];
            }
        }
        return 0;
    }
public:
    BinaryIndexedTree(vector<int> nums){
        this->size = nums.size();
        this->vals = new int[nums.size() + 1];
        this->sums = new int[nums.size() + 1];
        int i = 1;
        for (auto iter = nums.begin();
             iter != nums.end();
             iter++
            ){
           this->vals[i++] = *iter; 
        }
        this->build_sum();
        //this->show();
    }
    void show(){
        for (int i=1; i<=this->size; i++){
            cout<<vals[i]<<","<<sums[i]<<"\t";
        }
        cout<<endl;
    }
    int get_val(int idx){
        return this->vals[idx];
    }
    int range_sum(int left, int right){
        return this->prefix_sum(right) - this->prefix_sum(left-1);
    }
    int prefix_sum(int idx){
        int total = 0;
        for (; idx>0; idx-=lowbit(idx)){
            total += sums[idx];
        }
        return total;
    }
    void update(int i, int val){
        int delta = val - this->vals[i];
        this->vals[i] = val;
        for (;i<=this->size;i+=lowbit(i)){
            this->sums[i] += delta;
        }
    }
};

class Solution {
private:
    vector<int> sorted;
    int get_index(long long val){
        int l = -1;
        int r = this->sorted.size();
        while (l+1<r){
            int mid = (l + r) >> 1;
            //printf("searching %d %d -> %d\n", l, r, mid);
            int num = this->sorted[mid];
            if (val < num){
                r = mid;
            }else{
                l = mid;
            }
        }
        return l;
    }
    void init_sorted(vector<int>& nums){
        this->sorted = vector<int>(nums);
        sort(this->sorted.begin(), this->sorted.end());
    }
public:
    int reversePairs(vector<int>& nums) {
        int result = 0;
        this->init_sorted(nums);

        vector<int> initial;
        for (int i=0;i<nums.size();i++)
            initial.push_back(0);
        BinaryIndexedTree bit(initial);

        int total = 0;
        for (auto iter=nums.begin(); iter!=nums.end(); iter++){
            int idx_double = this->get_index((long long)(*iter) * 2);
            int count = total - bit.prefix_sum(idx_double + 1);
            int idx = this->get_index(* iter);
            int new_val = bit.get_val(idx + 1) + 1;
            //printf("%d %d\n", *iter, count);

            //printf("num=%d, idx=%d, didx=%d, val=%d, count=%d\n",*iter, idx, idx_double, new_val, count);
            bit.update(idx + 1, new_val);
            result += count;
            total += 1;
        }
        return result;
    }
};

int main(){
  vector<int> v;
  int x;
  while (EOF!= scanf("%d\n", &x)){
   // v.push_back(x);
    v.push_back(x);
    //printf("%d\n", x);
  }
  Solution solu;
  int result = solu.reversePairs(v);
  printf("%d\n", result);
  return 0;
}
