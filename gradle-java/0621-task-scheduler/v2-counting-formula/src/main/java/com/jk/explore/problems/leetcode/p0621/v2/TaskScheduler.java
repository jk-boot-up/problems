package com.jk.explore.problems.leetcode.p0621.v2;

import java.util.*;

public class TaskScheduler {

    public int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        for (char t : tasks) count[t - 'A']++;
        int maxCount = 0, tied = 0;
        for (int c : count) {
            if (c > maxCount) { maxCount = c; tied = 1; }
            else if (c == maxCount) tied++;
        }
        return Math.max(tasks.length, (maxCount - 1) * (n + 1) + tied);
    }
}
