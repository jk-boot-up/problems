package com.jk.explore.problems.leetcode.p0301.v2;

import java.util.*;

public class RemoveInvalidParentheses {

    public List<String> removeInvalidParentheses(String s) {
        int open = 0, close = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') open++;
            else if (c == ')') {
                if (open > 0) open--;
                else close++;
            }
        }
        List<String> out = new ArrayList<>();
        dfs(s, 0, open, close, out);
        return out;
    }

    private void dfs(String s, int start, int open, int close, List<String> out) {
        if (open == 0 && close == 0) {
            if (valid(s)) out.add(s);
            return;
        }
        for (int i = start; i < s.length(); i++) {
            if (open + close > s.length() - i) return;
            char c = s.charAt(i);
            if (i > start && c == s.charAt(i - 1)) continue;
            String t = s.substring(0, i) + s.substring(i + 1);
            if (c == '(' && open > 0) dfs(t, i, open - 1, close, out);
            if (c == ')' && close > 0) dfs(t, i, open, close - 1, out);
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
