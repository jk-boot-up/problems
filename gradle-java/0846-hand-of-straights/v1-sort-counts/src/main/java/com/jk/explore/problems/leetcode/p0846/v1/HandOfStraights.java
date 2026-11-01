package com.jk.explore.problems.leetcode.p0846.v1;

import java.util.*;

public class HandOfStraights {

    public boolean isNStraightHand(int[] hand, int groupSize) {
        if (hand.length % groupSize != 0) return false;
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int c : hand) count.merge(c, 1, Integer::sum);
        int[] values = hand.clone();
        Arrays.sort(values);
        for (int v : values) {
            int c = count.get(v);
            if (c == 0) continue;
            for (int x = v; x < v + groupSize; x++) {
                int have = count.getOrDefault(x, 0);
                if (have < c) return false;
                count.put(x, have - c);
            }
        }
        return true;
    }
}
