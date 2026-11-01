package com.jk.explore.problems.leetcode.p0210.v1;

import java.util.*;

public class CourseScheduleII {

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> next = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) next.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] p : prerequisites) {
            next.get(p[1]).add(p[0]);
            indegree[p[0]]++;
        }
        Deque<Integer> queue = new ArrayDeque<>();
        for (int c = 0; c < numCourses; c++) if (indegree[c] == 0) queue.add(c);
        int[] order = new int[numCourses];
        int taken = 0;
        while (!queue.isEmpty()) {
            int c = queue.poll();
            order[taken++] = c;
            for (int d : next.get(c)) {
                if (--indegree[d] == 0) queue.add(d);
            }
        }
        return taken == numCourses ? order : new int[0];
    }
}
