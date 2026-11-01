package com.jk.explore.problems.leetcode.p0057.v1;

import java.util.*;

public class InsertInterval {

    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> out = new ArrayList<>();
        int i = 0, n = intervals.length, start = newInterval[0], end = newInterval[1];
        while (i < n && intervals[i][1] < start) out.add(intervals[i++]);
        while (i < n && intervals[i][0] <= end) {
            start = Math.min(start, intervals[i][0]);
            end = Math.max(end, intervals[i][1]);
            i++;
        }
        out.add(new int[]{start, end});
        while (i < n) out.add(intervals[i++]);
        return out.toArray(new int[0][]);
    }
}
