package com.jk.explore.problems.leetcode.p0151.v2;

import java.util.*;

public class ReverseWords {

    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();
        int i = s.length() - 1;
        while (i >= 0) {
            while (i >= 0 && s.charAt(i) == ' ') {
                i--;
            }
            if (i < 0) {
                break;
            }
            int end = i;
            while (i >= 0 && s.charAt(i) != ' ') {
                i--;
            }
            if (!sb.isEmpty()) {
                sb.append(' ');
            }
            sb.append(s, i + 1, end + 1);
        }
        return sb.toString();
    }
}
