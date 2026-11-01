package com.jk.explore.problems.leetcode.p0207.v1;

import java.util.*;

public class CourseSchedule {

    private List<List<Integer>> next;
    private int[] state; // 0 = unvisited, 1 = on the current path, 2 = done

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        next = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) next.add(new ArrayList<>());
        for (int[] p : prerequisites) next.get(p[1]).add(p[0]);
        state = new int[numCourses];
        for (int c = 0; c < numCourses; c++) {
            if (hasCycle(c)) return false;
        }
        return true;
    }

    private boolean hasCycle(int c) {
        if (state[c] == 1) return true;
        if (state[c] == 2) return false;
        state[c] = 1;
        for (int d : next.get(c)) {
            if (hasCycle(d)) return true;
        }
        state[c] = 2;
        return false;
    }
}
