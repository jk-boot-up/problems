package com.jk.explore.problems.leetcode.p0282.v1;

import java.util.*;

public class ExpressionAddOperators {

    public List<String> addOperators(String num, int target) {
        List<String> out = new ArrayList<>();
        dfs(num, target, 0, 0, 0, new StringBuilder(), out);
        return out;
    }

    private void dfs(String num, long target, int pos, long value, long last, StringBuilder expr, List<String> out) {
        if (pos == num.length()) {
            if (value == target) out.add(expr.toString());
            return;
        }
        int len = expr.length();
        for (int i = pos; i < num.length(); i++) {
            if (i > pos && num.charAt(pos) == '0') break;
            long cur = Long.parseLong(num.substring(pos, i + 1));
            if (pos == 0) {
                dfs(num, target, i + 1, cur, cur, expr.append(cur), out);
                expr.setLength(len);
                continue;
            }
            dfs(num, target, i + 1, value + cur, cur, expr.append('+').append(cur), out);
            expr.setLength(len);
            dfs(num, target, i + 1, value - cur, -cur, expr.append('-').append(cur), out);
            expr.setLength(len);
            dfs(num, target, i + 1, value - last + last * cur, last * cur, expr.append('*').append(cur), out);
            expr.setLength(len);
        }
    }
}
