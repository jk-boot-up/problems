package com.jk.explore.problems.leetcode.p0077.v1;

import java.util.*;

public class Combinations {

    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> out = new ArrayList<>();
        backtrack(n, k, 1, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(int n, int k, int start, List<Integer> path, List<List<Integer>> out) {
        if (path.size() == k) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i <= n - (k - path.size()) + 1; i++) {
            path.add(i);
            backtrack(n, k, i + 1, path, out);
            path.removeLast();
        }
    }
}
