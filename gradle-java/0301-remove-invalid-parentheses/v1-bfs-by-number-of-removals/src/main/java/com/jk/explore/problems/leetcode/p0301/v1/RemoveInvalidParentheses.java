package com.jk.explore.problems.leetcode.p0301.v1;

import java.util.*;

public class RemoveInvalidParentheses {

    public List<String> removeInvalidParentheses(String s) {
        MyHashSet<String> seen = new MyHashSet<>();
        List<String> level = new ArrayList<>(List.of(s));
        seen.add(s);
        while (true) {
            List<String> out = new ArrayList<>();
            for (String t : level) if (valid(t)) out.add(t);
            if (!out.isEmpty()) return out;
            List<String> next = new ArrayList<>();
            for (String t : level)
                for (int i = 0; i < t.length(); i++) {
                    char c = t.charAt(i);
                    if (c != '(' && c != ')') continue;
                    String u = t.substring(0, i) + t.substring(i + 1);
                    if (seen.add(u)) next.add(u);
                }
            level = next;
        }
    }

    private boolean valid(String s) {
        int depth = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') depth++;
            else if (c == ')' && --depth < 0) return false;
        }
        return depth == 0;
    }
}
