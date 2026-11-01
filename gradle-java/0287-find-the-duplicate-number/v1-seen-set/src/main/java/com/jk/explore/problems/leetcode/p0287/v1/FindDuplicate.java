package com.jk.explore.problems.leetcode.p0287.v1;

import java.util.*;

public class FindDuplicate {

    public int findDuplicate(int[] nums) {
        MyHashSet<Integer> seen = new MyHashSet<>();
        for (int x : nums) {
            if (!seen.add(x)) return x;
        }
        throw new IllegalArgumentException("No duplicate");
    }
}
