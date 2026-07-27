class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for(int count : nums) {
            if(set.contains(count)) return true;
            set.add(count);
        }
        return false;
    }
}