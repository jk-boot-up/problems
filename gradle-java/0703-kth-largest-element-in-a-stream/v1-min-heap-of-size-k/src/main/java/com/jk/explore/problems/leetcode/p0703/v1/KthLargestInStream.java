package com.jk.explore.problems.leetcode.p0703.v1;

import java.util.*;

public class KthLargestInStream {

    private final int k;
    private final PriorityQueue<Integer> heap = new PriorityQueue<>();

    public KthLargestInStream(int k, int[] nums) {
        this.k = k;
        for (int x : nums) add(x);
    }

    public int add(int val) {
        heap.add(val);
        if (heap.size() > k) heap.poll();
        return heap.peek();
    }
}
