package com.jk.explore.problems.leetcode.p0752.v1;

import java.util.*;

public class OpenTheLock {

    public int openLock(String[] deadends, String target) {
        MyHashSet<String> blocked = new MyHashSet<>();
        for (String d : deadends) blocked.add(d);
        if (blocked.contains("0000")) return -1;
        MyHashSet<String> seen = new MyHashSet<>();
        Deque<String> queue = new ArrayDeque<>(List.of("0000"));
        seen.add("0000");
        for (int moves = 0; !queue.isEmpty(); moves++) {
            for (int size = queue.size(); size > 0; size--) {
                String cur = queue.poll();
                if (cur.equals(target)) return moves;
                char[] c = cur.toCharArray();
                for (int w = 0; w < 4; w++) {
                    char orig = c[w];
                    for (int delta : new int[]{1, 9}) {
                        c[w] = (char) ('0' + (orig - '0' + delta) % 10);
                        String next = new String(c);
                        if (!blocked.contains(next) && seen.add(next)) queue.add(next);
                    }
                    c[w] = orig;
                }
            }
        }
        return -1;
    }
}
