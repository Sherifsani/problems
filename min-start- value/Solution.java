class Solution {
    public int minStartValue(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n + 1];
        int min = Integer.MAX_VALUE;

        for(int i = 0; i < n; i++){
            prefix[i + 1] = prefix[i] + nums[i];
            min = Math.min(min,  prefix[i+1]);
        }
        if (min < 1){
            return Math.abs(min) + 1;
        }
        return 1;
    }
}