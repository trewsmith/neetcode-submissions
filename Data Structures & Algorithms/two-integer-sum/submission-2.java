class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++ ) {
            map.put(nums[i], i);
        }
        for(int i = 0; i < nums.length; i++) {
            int num2 = target - nums[i];
            int otherIndex = map.get(num2);
            if (otherIndex != i ) {
                if (map.containsKey(num2)) {
                int[] result = {i , map.get(num2)};
                return result;
            }
            }
            
            
        }
        return null;
    }
}