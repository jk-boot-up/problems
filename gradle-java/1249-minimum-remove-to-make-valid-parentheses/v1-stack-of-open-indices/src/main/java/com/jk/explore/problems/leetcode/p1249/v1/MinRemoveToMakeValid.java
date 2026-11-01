package com.jk.explore.problems.leetcode.p1249.v1;

import java.util.*;

public class MinRemoveToMakeValid {

    public String minRemoveToMakeValid(String s) {
        boolean[] remove = new boolean[s.length()];
        Deque<Integer> open = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') open.push(i);
            else if (c == ')') {
                if (open.isEmpty()) remove[i] = true;
                else open.pop();
            }
        }
        for (int i : open) remove[i] = true;
        StringBuilder sb = new StringBuilder(s.length());
        for (int i = 0; i < s.length(); i++) if (!remove[i]) sb.append(s.charAt(i));
        return sb.toString();
    }
}
