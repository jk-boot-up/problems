package com.jk.explore.problems.leetcode.p0933.v1;

import java.util.*;

public class RecentCounter {

    private final Deque<Integer> pings = new ArrayDeque<>();

    public int ping(int t) {
        pings.addLast(t);
        while (pings.peekFirst() < t - 3000) pings.pollFirst();
        return pings.size();
    }
}
