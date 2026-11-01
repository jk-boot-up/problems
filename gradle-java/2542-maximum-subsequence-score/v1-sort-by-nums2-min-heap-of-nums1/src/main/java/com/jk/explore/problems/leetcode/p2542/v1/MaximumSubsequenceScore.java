package com.jk.explore.problems.leetcode.p2542.v1;

import java.util.*;

public class MaximumSubsequenceScore {

    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, (a, b) -> Integer.compare(nums2[b], nums2[a]));
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        long sum = 0, best = 0;
        for (int i : order) {
            heap.add(nums1[i]);
            sum += nums1[i];
            if (heap.size() > k) sum -= heap.poll();
            if (heap.size() == k) best = Math.max(best, sum * nums2[i]);
        }
        return best;
    }
}
