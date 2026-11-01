package com.jk.explore.problems.leetcode.p0040.v1;

import java.util.*;

public class CombinationSumII {

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
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
            if (i > start && c[i] == c[i - 1]) continue;
            path.add(c[i]);
            backtrack(c, i + 1, remaining - c[i], path, out);
            path.removeLast();
        }
    }
}
