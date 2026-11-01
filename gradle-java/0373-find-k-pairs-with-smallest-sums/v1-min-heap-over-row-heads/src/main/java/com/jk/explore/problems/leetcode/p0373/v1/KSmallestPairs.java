package com.jk.explore.problems.leetcode.p0373.v1;

import java.util.*;

public class KSmallestPairs {

    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(p -> nums1[p[0]] + nums2[p[1]]));
        for (int i = 0; i < Math.min(k, nums1.length); i++) heap.add(new int[]{i, 0});
        List<List<Integer>> out = new ArrayList<>();
        while (out.size() < k && !heap.isEmpty()) {
            int[] p = heap.poll();
            out.add(List.of(nums1[p[0]], nums2[p[1]]));
            if (p[1] + 1 < nums2.length) heap.add(new int[]{p[0], p[1] + 1});
        }
        return out;
    }
}
