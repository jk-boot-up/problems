package com.jk.explore.problems.leetcode.p0022.v1;

import java.util.*;

public class GenerateParentheses {

    public List<String> generateParenthesis(int n) {
        List<String> out = new ArrayList<>();
        backtrack(n, 0, 0, new StringBuilder(), out);
        return out;
    }

    private void backtrack(int n, int open, int close, StringBuilder sb, List<String> out) {
        if (sb.length() == 2 * n) {
            out.add(sb.toString());
            return;
        }
        if (open < n) {
            sb.append('(');
            backtrack(n, open + 1, close, sb, out);
            sb.deleteCharAt(sb.length() - 1);
        }
        if (close < open) {
            sb.append(')');
            backtrack(n, open, close + 1, sb, out);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
