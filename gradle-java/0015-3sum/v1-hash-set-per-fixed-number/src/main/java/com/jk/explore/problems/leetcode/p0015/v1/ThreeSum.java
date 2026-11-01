package com.jk.explore.problems.leetcode.p0015.v1;

import java.util.*;

public class ThreeSum {

    public List<List<Integer>> threeSum(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        MyHashSet<List<Integer>> found = new MyHashSet<>();
        for (int i = 0; i < a.length - 2; i++) {
            MyHashSet<Integer> seen = new MyHashSet<>();
            for (int j = i + 1; j < a.length; j++) {
                int need = -a[i] - a[j];
                if (seen.contains(need)) {
                    found.add(List.of(a[i], need, a[j]));
                }
                seen.add(a[j]);
            }
        }
        List<List<Integer>> out = new ArrayList<>();
        for (List<Integer> triplet : found) out.add(triplet);
        return out;
    }
}
