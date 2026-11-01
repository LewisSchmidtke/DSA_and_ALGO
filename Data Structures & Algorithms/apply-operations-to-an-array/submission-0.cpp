class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        for (int i = 1; i < nums.size(); i++){
            if (nums[i-1] == nums[i]){
                nums[i-1] *= 2;
                nums[i] = 0;
            }

        }
        for (int num : nums){
            std::cout << num;
        }


        int place = 0;
        for (int x = 0; x < nums.size(); x++){
            if (nums[x] != 0){
                nums[place] = nums[x];
                if (place != x){
                    nums[x] = 0;
                }
                place += 1;
            }
        }
    return nums;
    }
};
