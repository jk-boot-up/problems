package com.jk.explore.problems.leetcode.p0454.v2;

import java.util.*;

public class FourSumII {

    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        MyHashMap<Integer, Integer> pairs = new MyHashMap<>();
        for (int a : nums1) for (int b : nums2) pairs.merge(a + b, 1, Integer::sum);
        int count = 0;
        for (int c : nums3) for (int d : nums4) count += pairs.getOrDefault(-(c + d), 0);
        return count;
    }
}
