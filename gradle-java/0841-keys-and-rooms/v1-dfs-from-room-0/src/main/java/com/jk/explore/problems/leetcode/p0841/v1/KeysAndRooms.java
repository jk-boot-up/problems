package com.jk.explore.problems.leetcode.p0841.v1;

import java.util.*;

public class KeysAndRooms {

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] seen = new boolean[rooms.size()];
        Deque<Integer> stack = new ArrayDeque<>(List.of(0));
        seen[0] = true;
        int visited = 1;
        while (!stack.isEmpty()) {
            for (int key : rooms.get(stack.pop())) {
                if (!seen[key]) {
                    seen[key] = true;
                    visited++;
                    stack.push(key);
                }
            }
        }
        return visited == rooms.size();
    }
}
