package com.jk.explore.problems.leetcode.p0621.v1;

import java.util.*;

public class TaskScheduler {

    public int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        for (char t : tasks) count[t - 'A']++;
        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.reverseOrder());
        for (int c : count) if (c > 0) heap.add(c);
        int time = 0;
        while (!heap.isEmpty()) {
            List<Integer> left = new ArrayList<>();
            int ran = 0;
            for (int i = 0; i <= n && !heap.isEmpty(); i++, ran++) {
                int c = heap.poll() - 1;
                if (c > 0) left.add(c);
            }
            heap.addAll(left);
            time += heap.isEmpty() ? ran : n + 1;
        }
        return time;
    }
}
