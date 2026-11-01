package com.jk.explore.problems.leetcode.p0435.v1;

import java.util.*;

public class NonOverlappingIntervals {

    public int eraseOverlapIntervals(int[][] intervals) {
        int[][] a = intervals.clone();
        Arrays.sort(a, Comparator.comparingInt(x -> x[1]));
        int removed = 0, end = Integer.MIN_VALUE;
        for (int[] iv : a) {
            if (iv[0] >= end) end = iv[1];
            else removed++;
        }
        return removed;
    }
}
