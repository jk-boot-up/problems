package com.jk.explore.problems.leetcode.p0649.v1;

import java.util.*;

public class Dota2Senate {

    public String predictPartyVictory(String senate) {
        int n = senate.length();
        Deque<Integer> r = new ArrayDeque<>(), d = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (senate.charAt(i) == 'R') r.add(i); else d.add(i);
        }
        while (!r.isEmpty() && !d.isEmpty()) {
            int a = r.poll(), b = d.poll();
            if (a < b) r.add(a + n); else d.add(b + n);
        }
        return r.isEmpty() ? "Dire" : "Radiant";
    }
}
