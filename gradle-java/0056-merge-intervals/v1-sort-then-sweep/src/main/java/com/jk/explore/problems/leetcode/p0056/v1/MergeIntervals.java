package com.jk.explore.problems.leetcode.p0056.v1;

import java.util.*;

public class MergeIntervals {

    public int[][] merge(int[][] intervals) {
        int[][] sorted = intervals.clone();
        Arrays.sort(sorted, Comparator.comparingInt(a -> a[0]));
        List<int[]> out = new ArrayList<>();
        for (int[] cur : sorted) {
            if (!out.isEmpty() && cur[0] <= out.getLast()[1]) {
                out.getLast()[1] = Math.max(out.getLast()[1], cur[1]);
            } else {
                out.add(new int[]{cur[0], cur[1]});
            }
        }
        return out.toArray(new int[0][]);
    }
}
