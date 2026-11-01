package com.jk.explore.problems.leetcode.p0496.v1;

import java.util.*;

public class NextGreaterElementI {

    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        MyHashMap<Integer, Integer> next = new MyHashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();
        for (int x : nums2) {
            while (!stack.isEmpty() && stack.peek() < x) next.put(stack.pop(), x);
            stack.push(x);
        }
        int[] out = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) out[i] = next.getOrDefault(nums1[i], -1);
        return out;
    }
}
