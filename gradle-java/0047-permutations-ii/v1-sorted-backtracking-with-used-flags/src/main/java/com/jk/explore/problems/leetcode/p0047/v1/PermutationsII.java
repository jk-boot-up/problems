package com.jk.explore.problems.leetcode.p0047.v1;

import java.util.*;

public class PermutationsII {

    public List<List<Integer>> permuteUnique(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        List<List<Integer>> out = new ArrayList<>();
        backtrack(a, new boolean[a.length], new ArrayList<>(), out);
        return out;
    }

    private void backtrack(int[] a, boolean[] used, List<Integer> path, List<List<Integer>> out) {
        if (path.size() == a.length) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < a.length; i++) {
            if (used[i] || (i > 0 && a[i] == a[i - 1] && !used[i - 1])) continue;
            used[i] = true;
            path.add(a[i]);
            backtrack(a, used, path, out);
            path.removeLast();
            used[i] = false;
        }
    }
}
