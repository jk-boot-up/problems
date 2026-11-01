package com.jk.explore.problems.leetcode.p0402.v1;

import java.util.*;

public class RemoveKDigits {

    public String removeKdigits(String num, int k) {
        StringBuilder stack = new StringBuilder();
        for (char d : num.toCharArray()) {
            while (k > 0 && stack.length() > 0 && stack.charAt(stack.length() - 1) > d) {
                stack.setLength(stack.length() - 1);
                k--;
            }
            stack.append(d);
        }
        stack.setLength(stack.length() - k);
        int start = 0;
        while (start < stack.length() - 1 && stack.charAt(start) == '0') start++;
        return stack.length() == 0 ? "0" : stack.substring(start);
    }
}
