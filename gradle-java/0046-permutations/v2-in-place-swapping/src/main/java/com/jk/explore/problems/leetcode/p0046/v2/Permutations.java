package com.jk.explore.problems.leetcode.p0046.v2;

import java.util.*;

public class Permutations {

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        permute(nums.clone(), 0, out);
        return out;
    }

    private void permute(int[] a, int i, List<List<Integer>> out) {
        if (i == a.length) {
            List<Integer> p = new ArrayList<>();
            for (int x : a) p.add(x);
            out.add(p);
            return;
        }
        for (int j = i; j < a.length; j++) {
            swap(a, i, j);
            permute(a, i + 1, out);
            swap(a, i, j);
        }
    }

    private static void swap(int[] a, int i, int j) {
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}
