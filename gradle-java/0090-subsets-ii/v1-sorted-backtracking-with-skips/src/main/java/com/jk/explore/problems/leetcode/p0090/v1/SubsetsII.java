package com.jk.explore.problems.leetcode.p0090.v1;

import java.util.*;

public class SubsetsII {

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        List<List<Integer>> out = new ArrayList<>();
        backtrack(a, 0, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(int[] a, int start, List<Integer> path, List<List<Integer>> out) {
        out.add(new ArrayList<>(path));
        for (int i = start; i < a.length; i++) {
            if (i > start && a[i] == a[i - 1]) continue;
            path.add(a[i]);
            backtrack(a, i + 1, path, out);
            path.removeLast();
        }
    }
}
