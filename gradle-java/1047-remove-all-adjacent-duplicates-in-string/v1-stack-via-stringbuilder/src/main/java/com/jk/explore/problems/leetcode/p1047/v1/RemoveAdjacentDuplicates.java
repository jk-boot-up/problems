package com.jk.explore.problems.leetcode.p1047.v1;

import java.util.*;

public class RemoveAdjacentDuplicates {

    public String removeDuplicates(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            int last = sb.length() - 1;
            if (last >= 0 && sb.charAt(last) == c) sb.deleteCharAt(last);
            else sb.append(c);
        }
        return sb.toString();
    }
}
