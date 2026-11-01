package com.jk.explore.problems.leetcode.p0347.v1;

import java.util.*;

public class TopKFrequent {

    public int[] topKFrequent(int[] nums, int k) {
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int x : nums) count.merge(x, 1, Integer::sum);
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(e -> e[1]));
        for (MyHashMap.Entry<Integer, Integer> e : count.entries()) {
            heap.add(new int[]{e.getKey(), e.getValue()});
            if (heap.size() > k) heap.poll();
        }
        int[] out = new int[k];
        for (int i = 0; i < k; i++) out[i] = heap.poll()[0];
        return out;
    }
}
