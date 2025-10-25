class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        int x = 0;
        for(int i:nums){
            
            x^=i;


        }

        // std::cout<<x<<"\n";
        return x;


    }
};