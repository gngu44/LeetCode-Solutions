class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> pairs = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int num = nums[i];
            if (pairs.containsKey(target - num)){
                return new int[] {i, pairs.get(target-num)};
            }
            pairs.put(num, i);

        }

        return new int[] {};
    }
}