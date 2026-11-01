package com.jk.explore.problems.leetcode.p0187.v1;

import java.util.*;

public class RepeatedDNA {

    public List<String> findRepeatedDnaSequences(String s) {
        MyHashSet<String> seen = new MyHashSet<>(), reported = new MyHashSet<>();
        List<String> out = new ArrayList<>();
        for (int i = 0; i + 10 <= s.length(); i++) {
            String w = s.substring(i, i + 10);
            if (!seen.add(w) && reported.add(w)) out.add(w);
        }
        return out;
    }
}
