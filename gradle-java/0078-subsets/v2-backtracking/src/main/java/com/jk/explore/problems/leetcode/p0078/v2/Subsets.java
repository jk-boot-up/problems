package com.jk.explore.problems.leetcode.p0078.v2;

import java.util.*;

public class Subsets {

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), out);
        return out;
    }

    private void backtrack(int[] nums, int start, List<Integer> path, List<List<Integer>> out) {
        out.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrack(nums, i + 1, path, out);
            path.removeLast();
        }
    }
}
