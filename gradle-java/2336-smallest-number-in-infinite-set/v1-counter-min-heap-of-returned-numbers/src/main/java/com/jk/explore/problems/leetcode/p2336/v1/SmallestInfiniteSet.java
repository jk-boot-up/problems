package com.jk.explore.problems.leetcode.p2336.v1;

import java.util.*;

public class SmallestInfiniteSet {

    private int next = 1;
    private final PriorityQueue<Integer> returned = new PriorityQueue<>();
    private final MyHashSet<Integer> inHeap = new MyHashSet<>();

    public int popSmallest() {
        if (!returned.isEmpty()) {
            int x = returned.poll();
            inHeap.remove(x);
            return x;
        }
        return next++;
    }

    public void addBack(int num) {
        if (num < next && inHeap.add(num)) returned.add(num);
    }
}
