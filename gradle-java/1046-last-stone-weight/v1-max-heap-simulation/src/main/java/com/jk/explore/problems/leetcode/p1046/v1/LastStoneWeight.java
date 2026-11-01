package com.jk.explore.problems.leetcode.p1046.v1;

import java.util.*;

public class LastStoneWeight {

    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.reverseOrder());
        for (int s : stones) heap.add(s);
        while (heap.size() > 1) {
            int y = heap.poll(), x = heap.poll();
            if (y > x) heap.add(y - x);
        }
        return heap.isEmpty() ? 0 : heap.peek();
    }
}
