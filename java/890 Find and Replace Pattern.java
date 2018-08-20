class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        int n = pattern.length();
        List<String> res = new ArrayList<String>();

        HashMap<Character, Integer> dic = new HashMap<Character, Integer>();
        int count = 1;
        String tmp="";
        for (int i = 0; i < n; i++) {
            if (dic.get(pattern.charAt(i)) != null) {
                tmp += dic.get(pattern.charAt(i));
            }else {
                tmp += Integer.toString(count);
                dic.put(pattern.charAt(i), count);
                count += 1;
            }
        }

        HashMap<Character, Integer> dic2 = new HashMap<Character, Integer>();
        int count2 = 1;
        String tmp2= "";
        for (String i : words) {
            for (int j = 0; j < i.length(); j++) {
                if (dic2.get(i.charAt(j)) != null ) {
                    tmp2 += dic2.get(i.charAt(j));
                }else {
                    tmp2 += Integer.toString(count2);
                    dic2.put(i.charAt(j), count2);
                    count2 += 1;
                }
            }
            if (tmp.equalsIgnoreCase(tmp2)) {
                res.add(i);
            }
            count2 = 1;
            dic2.clear();
            tmp2 = "";
        }
        return res;
    }
}
