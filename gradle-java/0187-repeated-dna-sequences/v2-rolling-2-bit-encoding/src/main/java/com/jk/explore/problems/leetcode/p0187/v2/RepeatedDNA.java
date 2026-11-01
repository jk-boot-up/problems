package com.jk.explore.problems.leetcode.p0187.v2;

import java.util.*;

public class RepeatedDNA {

    public List<String> findRepeatedDnaSequences(String s) {
        int[] code = new int[128];
        code['C'] = 1;
        code['G'] = 2;
        code['T'] = 3;
        int mask = (1 << 20) - 1, h = 0;
        MyHashSet<Integer> seen = new MyHashSet<>(), reported = new MyHashSet<>();
        List<String> out = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            h = ((h << 2) | code[s.charAt(i)]) & mask;
            if (i >= 9 && !seen.add(h) && reported.add(h)) out.add(s.substring(i - 9, i + 1));
        }
        return out;
    }
}
