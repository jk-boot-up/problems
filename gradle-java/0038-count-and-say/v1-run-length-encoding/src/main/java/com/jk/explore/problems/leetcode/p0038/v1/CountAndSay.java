package com.jk.explore.problems.leetcode.p0038.v1;

import java.util.*;

public class CountAndSay {

    public String countAndSay(int n) {
        String s = "1";
        for (int k = 1; k < n; k++) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < s.length(); ) {
                int j = i;
                while (j < s.length() && s.charAt(j) == s.charAt(i)) j++;
                sb.append(j - i).append(s.charAt(i));
                i = j;
            }
            s = sb.toString();
        }
        return s;
    }
}
