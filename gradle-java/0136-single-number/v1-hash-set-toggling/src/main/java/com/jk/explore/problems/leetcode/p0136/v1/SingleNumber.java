package com.jk.explore.problems.leetcode.p0136.v1;

import java.util.*;

public class SingleNumber {

    public int singleNumber(int[] nums) {
        MyHashSet<Integer> seen = new MyHashSet<>();
        for (int v : nums) {
            if (!seen.add(v)) seen.remove(v);
        }
        return seen.iterator().next();
    }
}
