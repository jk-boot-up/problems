package com.jk.explore.problems.leetcode.p0433.v1;

import java.util.*;

public class MinimumGeneticMutation {

    public int minMutation(String startGene, String endGene, String[] bank) {
        MyHashSet<String> valid = new MyHashSet<>();
        for (String g : bank) valid.add(g);
        if (!valid.contains(endGene)) return -1;
        MyHashSet<String> seen = new MyHashSet<>();
        seen.add(startGene);
        Deque<String> queue = new ArrayDeque<>(List.of(startGene));
        for (int steps = 0; !queue.isEmpty(); steps++) {
            for (int size = queue.size(); size > 0; size--) {
                String g = queue.poll();
                if (g.equals(endGene)) return steps;
                char[] chars = g.toCharArray();
                for (int i = 0; i < chars.length; i++) {
                    char original = chars[i];
                    for (char c : "ACGT".toCharArray()) {
                        chars[i] = c;
                        String next = new String(chars);
                        if (valid.contains(next) && seen.add(next)) queue.add(next);
                    }
                    chars[i] = original;
                }
            }
        }
        return -1;
    }
}
