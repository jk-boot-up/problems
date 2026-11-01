package com.jk.explore.problems.leetcode.p0049.v1;

import java.util.*;

public class GroupAnagrams {

    public List<List<String>> groupAnagrams(String[] strs) {
        MyHashMap<String, List<String>> groups = new MyHashMap<>();
        for (String s : strs) {
            char[] key = s.toCharArray();
            Arrays.sort(key);
            groups.computeIfAbsent(new String(key), k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(groups.values());
    }
}
