class Solution {
    public boolean isAnagram(String s, String t) {
        Set<Character> chars = new HashSet<>();

        for (char c : s.toCharArray()) {
            chars.add(c);
        }

        Set<Character> chars1 = new HashSet<>();

        for (char c : t.toCharArray()) {
            chars1.add(c);
        }
        if (chars.equals(chars1)) {
            return true;
        }
        return false;

    }
}
