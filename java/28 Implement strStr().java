class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.length() == 0){return 0;}
        int start = 0;
        while(start <= haystack.length() - needle.length()) {
            int i = start;
            int j = 0;
            while (j < needle.length() && haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
            }
            if (j == needle.length()) {
                return start;
            }
            start++;
        }
        return -1;
    }
}
