package com.jk.explore.problems.leetcode.p0406.v1;

import java.util.*;

public class QueueReconstruction {

    public int[][] reconstructQueue(int[][] people) {
        int[][] p = people.clone();
        Arrays.sort(p, (a, b) -> a[0] != b[0] ? Integer.compare(b[0], a[0]) : Integer.compare(a[1], b[1]));
        List<int[]> queue = new ArrayList<>();
        for (int[] person : p) queue.add(person[1], person);
        return queue.toArray(new int[0][]);
    }
}
