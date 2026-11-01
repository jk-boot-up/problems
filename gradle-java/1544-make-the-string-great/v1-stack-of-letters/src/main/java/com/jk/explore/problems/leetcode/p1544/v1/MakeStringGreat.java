package com.jk.explore.problems.leetcode.p1544.v1;

import java.util.*;

public class MakeStringGreat {

    public String makeGood(String s) {
        StringBuilder stack = new StringBuilder();
        for (char c : s.toCharArray()) {
            int n = stack.length();
            if (n > 0 && Math.abs(stack.charAt(n - 1) - c) == 'a' - 'A') stack.setLength(n - 1);
            else stack.append(c);
        }
        return stack.toString();
    }
}
