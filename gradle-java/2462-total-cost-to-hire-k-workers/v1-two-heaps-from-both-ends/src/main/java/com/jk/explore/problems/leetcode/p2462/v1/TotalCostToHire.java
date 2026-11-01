package com.jk.explore.problems.leetcode.p2462.v1;

import java.util.*;

public class TotalCostToHire {

    public long totalCost(int[] costs, int k, int candidates) {
        PriorityQueue<Integer> left = new PriorityQueue<>(), right = new PriorityQueue<>();
        int lo = 0, hi = costs.length - 1;
        long total = 0;
        for (int session = 0; session < k; session++) {
            while (left.size() < candidates && lo <= hi) left.add(costs[lo++]);
            while (right.size() < candidates && lo <= hi) right.add(costs[hi--]);
            int a = left.isEmpty() ? Integer.MAX_VALUE : left.peek();
            int b = right.isEmpty() ? Integer.MAX_VALUE : right.peek();
            if (a <= b) total += left.poll(); else total += right.poll();
        }
        return total;
    }
}
