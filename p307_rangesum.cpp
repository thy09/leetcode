#include <iostream>
#include <vector>
#include <string>
    using namespace std;
#include <stdio.h>

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
    int prefix_sum(int idx){
        int total = 0;
        for (; idx>0; idx-=lowbit(idx)){
            total += sums[idx];
        }
        return total;
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
        this->show();
    }
    void show(){
        for (int i=1; i<=this->size; i++){
            cout<<vals[i]<<","<<sums[i]<<"\t";
        }
        cout<<endl;
    }
    int range_sum(int left, int right){
        return this->prefix_sum(right) - this->prefix_sum(left-1);
    }
    void update(int i, int val){
        int delta = val - this->vals[i];
        this->vals[i] = val;
        for (;i<=this->size;i+=lowbit(i)){
            this->sums[i] += delta;
        }
    }
};

class NumArray {
private:
    BinaryIndexedTree* _bit;
public:
    NumArray(vector<int> nums) {
        this->_bit = new BinaryIndexedTree(nums);
    }
    
    void update(int i, int val) {
        this->_bit->update(i+1, val);     
        //this->_bit->show();
    }
    
    int sumRange(int i, int j) {
        return this->_bit->range_sum(i+1, j+1);
    }
};

int main(){
    int size = 10;
    vector<int> nums;
    scanf("%d\n", &size);
    int temp;
    for (int i=0;i<size; i++){
        scanf("%d", &temp);
        nums.push_back(temp);
    }
    int action_size = 0;
    NumArray obj = NumArray(nums);
    scanf("%d\n", &action_size);
    for (int i=0;i<action_size;i++){
        char action;
        int a,b;
        scanf("%c %d %d\n", &action, &a, &b);
        if (action == 'u'){
            obj.update(a,b);
        }
        if (action == 's'){
            cout<<obj.sumRange(a,b)<<endl;
        }
    }
    return 0;
}
