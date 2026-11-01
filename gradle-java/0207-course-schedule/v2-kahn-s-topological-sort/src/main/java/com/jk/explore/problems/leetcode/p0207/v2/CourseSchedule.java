package com.jk.explore.problems.leetcode.p0207.v2;

import java.util.*;

public class CourseSchedule {

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> next = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) next.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] p : prerequisites) {
            next.get(p[1]).add(p[0]);
            indegree[p[0]]++;
        }
        Deque<Integer> queue = new ArrayDeque<>();
        for (int c = 0; c < numCourses; c++) if (indegree[c] == 0) queue.add(c);
        int taken = 0;
        while (!queue.isEmpty()) {
            int c = queue.poll();
            taken++;
            for (int d : next.get(c)) {
                if (--indegree[d] == 0) queue.add(d);
            }
        }
        return taken == numCourses;
    }
}
