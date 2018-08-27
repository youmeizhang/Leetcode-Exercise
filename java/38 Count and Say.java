class Solution {
    public String countAndSay(int n) {
        if (n == 0) return "";
        String str = "1";

        for(int i = 1; i < n; i++) {
            int count = 0;
            Character prev = '.';
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < str.length(); j++) {
                if(str.charAt(j) == prev || prev == '.') {
                    count++;
                }else {
                    sb.append(count + Character.toString(prev));
                    count = 1;
                }
                prev = str.charAt(j);
            }
            sb.append(count + Character.toString(prev));
            str = sb.toString();
        }
        return str;
    }
}
