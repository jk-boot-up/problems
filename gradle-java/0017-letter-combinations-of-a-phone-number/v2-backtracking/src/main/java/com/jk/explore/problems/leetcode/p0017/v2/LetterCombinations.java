package com.jk.explore.problems.leetcode.p0017.v2;

import java.util.*;

public class LetterCombinations {

    private static final String[] KEYS = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> out = new ArrayList<>();
        if (!digits.isEmpty()) backtrack(digits, 0, new StringBuilder(), out);
        return out;
    }

    private void backtrack(String digits, int i, StringBuilder sb, List<String> out) {
        if (i == digits.length()) {
            out.add(sb.toString());
            return;
        }
        for (char c : KEYS[digits.charAt(i) - '0'].toCharArray()) {
            sb.append(c);
            backtrack(digits, i + 1, sb, out);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
