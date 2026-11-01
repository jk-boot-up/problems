package com.jk.explore.problems.leetcode.p2215.v1;

import java.util.*;

public class DifferenceOfTwoArrays {

    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        MyHashSet<Integer> a = new MyHashSet<>(), b = new MyHashSet<>();
        for (int x : nums1) a.add(x);
        for (int x : nums2) b.add(x);
        List<Integer> onlyA = new ArrayList<>(), onlyB = new ArrayList<>();
        for (int x : a) if (!b.contains(x)) onlyA.add(x);
        for (int x : b) if (!a.contains(x)) onlyB.add(x);
        return List.of(onlyA, onlyB);
    }
}
