package com.jk.explore.problems.leetcode.p0217.v2;

import java.util.*;

public class ContainsDuplicate {

    public boolean containsDuplicate(int[] nums) {
        MyHashSet<Integer> seen = new MyHashSet<>();
        for (int x : nums) {
            if (!seen.add(x)) return true;
        }
        return false;
    }
}
