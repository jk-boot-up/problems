package com.jk.explore.problems.leetcode.p0039.v1;

import java.util.*;

public class CombinationSum {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        int[] c = candidates.clone();
        Arrays.sort(c);
        List<List<Integer>> out = new ArrayList<>();
        backtrack(c, 0, target, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(int[] c, int start, int remaining, List<Integer> path, List<List<Integer>> out) {
        if (remaining == 0) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < c.length && c[i] <= remaining; i++) {
            path.add(c[i]);
            backtrack(c, i, remaining - c[i], path, out);
            path.removeLast();
        }
    }
}
