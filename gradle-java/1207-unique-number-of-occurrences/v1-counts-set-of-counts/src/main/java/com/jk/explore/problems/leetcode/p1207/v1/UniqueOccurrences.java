package com.jk.explore.problems.leetcode.p1207.v1;

import java.util.*;

public class UniqueOccurrences {

    public boolean uniqueOccurrences(int[] arr) {
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int x : arr) count.merge(x, 1, Integer::sum);
        MyHashSet<Integer> seen = new MyHashSet<>();
        for (int c : count.values()) {
            if (!seen.add(c)) return false;
        }
        return true;
    }
}
