class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for(int i = 0; i < nums.length; i++){
            int num2 = target - nums[i];
            if (map.containsKey(num2)) {
                if (map.get(num2) != i) {

                
                    int[] solution = new int[2];
                    solution[0] = i;
                    solution[1 ]= map.get(num2);
                    return solution;
                }
            }
        }
        return null;
    }
}
