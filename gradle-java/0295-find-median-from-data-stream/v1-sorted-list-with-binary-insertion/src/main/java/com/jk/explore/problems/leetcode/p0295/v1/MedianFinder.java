package com.jk.explore.problems.leetcode.p0295.v1;

import java.util.*;

public class MedianFinder {

    private final List<Integer> sorted = new ArrayList<>();

    public void addNum(int num) {
        int lo = 0, hi = sorted.size();
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (sorted.get(mid) < num) lo = mid + 1; else hi = mid;
        }
        sorted.add(lo, num);
    }

    public double findMedian() {
        int n = sorted.size();
        return n % 2 == 1 ? sorted.get(n / 2) : (sorted.get(n / 2 - 1) + (double) sorted.get(n / 2)) / 2;
    }
}
