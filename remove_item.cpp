class Solution {
public:
    int removeElement_destructive(vector<int>& nums, int val) {
        int i = 0;
        for (int j = 0; j<nums.size(); j++){
            if (nums[j]!=val){
                nums[i]=nums[j];
                i++;
            }
        }
        return i;
    }
    int removeElement_elementswitching(vector<int>& nums, int val) {
        if (nums.size()==0){
            return 0;
        }
        // assign end and beginning
        int i = 0;
        int end = nums.size()-1;
        int hold;
        while (i<end){
            while (nums[end]==val and i<end){
                end--;
            }
            if (nums[i]==val){
                hold = nums[i];
                nums[i]=nums[end];
                nums[end]=hold;
                end-=1;
            }
            i++;
        }
        if (end>=0){
            while (nums[end]==val and end>0){
                end--;
            }
            if (nums[end]==val and end==0){
                return 0;
            }
        }
        return end+1;
    }
};