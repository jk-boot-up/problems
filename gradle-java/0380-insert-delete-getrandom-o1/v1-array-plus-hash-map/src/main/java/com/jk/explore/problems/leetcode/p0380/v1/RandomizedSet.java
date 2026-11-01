package com.jk.explore.problems.leetcode.p0380.v1;

import java.util.*;

public class RandomizedSet {

    private final List<Integer> values = new ArrayList<>();
    private final MyHashMap<Integer, Integer> indexOf = new MyHashMap<>();
    private final Random random;

    public RandomizedSet() {
        this(new Random());
    }

    RandomizedSet(Random random) {
        this.random = random;
    }

    public boolean insert(int val) {
        if (indexOf.containsKey(val)) {
            return false;
        }
        indexOf.put(val, values.size());
        values.add(val);
        return true;
    }

    public boolean remove(int val) {
        Integer idx = indexOf.remove(val);
        if (idx == null) {
            return false;
        }
        int last = values.removeLast();
        if (idx < values.size()) {
            values.set(idx, last);
            indexOf.put(last, idx);
        }
        return true;
    }

    public int getRandom() {
        return values.get(random.nextInt(values.size()));
    }
}
