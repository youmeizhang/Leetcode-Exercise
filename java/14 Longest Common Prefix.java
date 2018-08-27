class Solution {
    public static int short_method(String[] randomStrings) {
        String shortest = randomStrings[0];
        for (String element : randomStrings) {
            if (element.length() < shortest.length()) {
                shortest = element;
            }
        }
        return shortest.length();
    }
    
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0)
            return "";
        int len = short_method(strs);

        StringBuilder res = new StringBuilder();
        int index = 0;
        while (index < len) {
            for(int j = 1; j< strs.length; j++) {
                if (strs[j].charAt(index) != strs[0].charAt(index)) {
                    return res.toString();
                }
            }
            res.append(strs[0].charAt(index));
            index++;
        }
        return res.toString();
    }
}
