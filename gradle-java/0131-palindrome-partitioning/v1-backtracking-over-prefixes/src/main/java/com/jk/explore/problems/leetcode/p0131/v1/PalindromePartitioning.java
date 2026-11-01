package com.jk.explore.problems.leetcode.p0131.v1;

import java.util.*;

public class PalindromePartitioning {

    public List<List<String>> partition(String s) {
        List<List<String>> out = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(String s, int start, List<String> path, List<List<String>> out) {
        if (start == s.length()) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                path.add(s.substring(start, end + 1));
                backtrack(s, end + 1, path, out);
                path.removeLast();
            }
        }
    }

    private static boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--)) return false;
        }
        return true;
    }
}
