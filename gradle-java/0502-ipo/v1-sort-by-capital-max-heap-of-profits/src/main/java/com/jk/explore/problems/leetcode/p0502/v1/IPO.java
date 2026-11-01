package com.jk.explore.problems.leetcode.p0502.v1;

import java.util.*;

public class IPO {

    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, Comparator.comparingInt(i -> capital[i]));
        PriorityQueue<Integer> best = new PriorityQueue<>(Comparator.reverseOrder());
        int next = 0;
        for (int round = 0; round < k; round++) {
            while (next < n && capital[order[next]] <= w) best.add(profits[order[next++]]);
            if (best.isEmpty()) break;
            w += best.poll();
        }
        return w;
    }
}
