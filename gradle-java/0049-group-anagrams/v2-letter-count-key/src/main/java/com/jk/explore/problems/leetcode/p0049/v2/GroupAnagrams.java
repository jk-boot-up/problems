package com.jk.explore.problems.leetcode.p0049.v2;

import java.util.*;

public class GroupAnagrams {

    public List<List<String>> groupAnagrams(String[] strs) {
        MyHashMap<String, List<String>> groups = new MyHashMap<>();
        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) count[c - 'a']++;
            groups.computeIfAbsent(Arrays.toString(count), k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(groups.values());
    }
}
