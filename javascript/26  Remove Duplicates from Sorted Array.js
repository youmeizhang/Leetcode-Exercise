var removeDuplicates = function(nums) {
    var i = 0;
    var j = 0;
    
    for (l=nums.length; i<l; i++){
        if (nums[j] != nums[i]) {
            nums[++j] = nums[i];
        }
    }
    return j+1;
};
