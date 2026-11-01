package com.jk.explore.problems.leetcode.p0350.v1;

import java.util.*;

public class IntersectionOfTwoArraysII {

    public int[] intersect(int[] nums1, int[] nums2) {
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int x : nums1) count.merge(x, 1, Integer::sum);
        List<Integer> out = new ArrayList<>();
        for (int x : nums2) {
            int c = count.getOrDefault(x, 0);
            if (c > 0) {
                out.add(x);
                count.put(x, c - 1);
            }
        }
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
}
