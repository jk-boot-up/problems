package com.jk.explore.problems.leetcode.p1376.v1;

import java.util.*;

public class TimeToInform {

    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        int[] firstChild = new int[n], nextSibling = new int[n], time = new int[n];
        Arrays.fill(firstChild, -1);
        for (int i = 0; i < n; i++)
            if (manager[i] != -1) {
                nextSibling[i] = firstChild[manager[i]];
                firstChild[manager[i]] = i;
            }
        Deque<Integer> queue = new ArrayDeque<>(List.of(headID));
        int best = 0;
        while (!queue.isEmpty()) {
            int p = queue.poll();
            best = Math.max(best, time[p]);
            for (int c = firstChild[p]; c != -1; c = nextSibling[c]) {
                time[c] = time[p] + informTime[p];
                queue.add(c);
            }
        }
        return best;
    }
}
