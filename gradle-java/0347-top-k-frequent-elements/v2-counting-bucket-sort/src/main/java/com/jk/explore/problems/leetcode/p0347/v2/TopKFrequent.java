package com.jk.explore.problems.leetcode.p0347.v2;

import java.util.*;

public class TopKFrequent {

    public int[] topKFrequent(int[] nums, int k) {
        MyHashMap<Integer, Integer> count = new MyHashMap<>();
        for (int x : nums) count.merge(x, 1, Integer::sum);
        List<List<Integer>> bucket = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++) bucket.add(new ArrayList<>());
        for (MyHashMap.Entry<Integer, Integer> e : count.entries()) bucket.get(e.getValue()).add(e.getKey());
        int[] out = new int[k];
        int filled = 0;
        for (int f = nums.length; f > 0 && filled < k; f--) {
            for (int v : bucket.get(f)) {
                if (filled < k) out[filled++] = v;
            }
        }
        return out;
    }
}
