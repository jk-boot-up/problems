package com.jk.explore.problems.leetcode.p0014.v1;

import java.util.*;

public class LongestCommonPrefix {

    public String longestCommonPrefix(String[] strs) {
        String first = strs[0];
        for (int c = 0; c < first.length(); c++) {
            char ch = first.charAt(c);
            for (int i = 1; i < strs.length; i++) {
                if (c >= strs[i].length() || strs[i].charAt(c) != ch) {
                    return first.substring(0, c);
                }
            }
        }
        return first;
    }
}
