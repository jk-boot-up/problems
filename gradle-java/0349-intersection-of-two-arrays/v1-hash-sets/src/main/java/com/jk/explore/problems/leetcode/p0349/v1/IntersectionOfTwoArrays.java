package com.jk.explore.problems.leetcode.p0349.v1;

import java.util.*;

public class IntersectionOfTwoArrays {

    public int[] intersection(int[] nums1, int[] nums2) {
        MyHashSet<Integer> set = new MyHashSet<>();
        for (int x : nums1) set.add(x);
        List<Integer> out = new ArrayList<>();
        for (int x : nums2) {
            if (set.remove(x)) out.add(x);
        }
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
}
