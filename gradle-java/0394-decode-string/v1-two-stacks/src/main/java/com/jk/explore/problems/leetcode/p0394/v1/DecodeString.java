package com.jk.explore.problems.leetcode.p0394.v1;

import java.util.*;

public class DecodeString {

    public String decodeString(String s) {
        Deque<Integer> counts = new ArrayDeque<>();
        Deque<StringBuilder> outer = new ArrayDeque<>();
        StringBuilder cur = new StringBuilder();
        int k = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                k = k * 10 + (c - '0');
            } else if (c == '[') {
                counts.push(k);
                outer.push(cur);
                cur = new StringBuilder();
                k = 0;
            } else if (c == ']') {
                StringBuilder prev = outer.pop();
                prev.append(cur.toString().repeat(counts.pop()));
                cur = prev;
            } else {
                cur.append(c);
            }
        }
        return cur.toString();
    }
}
