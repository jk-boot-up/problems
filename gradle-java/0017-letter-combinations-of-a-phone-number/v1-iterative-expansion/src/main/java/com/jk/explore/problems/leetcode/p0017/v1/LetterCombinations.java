package com.jk.explore.problems.leetcode.p0017.v1;

import java.util.*;

public class LetterCombinations {

    private static final String[] KEYS = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) return new ArrayList<>();
        List<String> partial = new ArrayList<>(List.of(""));
        for (char d : digits.toCharArray()) {
            List<String> next = new ArrayList<>();
            for (String p : partial) {
                for (char c : KEYS[d - '0'].toCharArray()) next.add(p + c);
            }
            partial = next;
        }
        return partial;
    }
}
