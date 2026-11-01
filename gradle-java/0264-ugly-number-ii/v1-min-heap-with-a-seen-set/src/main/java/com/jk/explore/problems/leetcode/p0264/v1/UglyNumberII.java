package com.jk.explore.problems.leetcode.p0264.v1;

import java.util.*;

public class UglyNumberII {

    public int nthUglyNumber(int n) {
        PriorityQueue<Long> heap = new PriorityQueue<>();
        MyHashSet<Long> queued = new MyHashSet<>();
        heap.add(1L);
        queued.add(1L);
        long x = 1;
        for (int k = 0; k < n; k++) {
            x = heap.poll();
            for (long f : new long[]{2, 3, 5}) if (queued.add(x * f)) heap.add(x * f);
        }
        return (int) x;
    }
}
