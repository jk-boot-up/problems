package com.jk.explore.problems.leetcode.p1462.v1;

import java.util.*;

public class CourseScheduleIV {

    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        boolean[][] reach = new boolean[numCourses][numCourses];
        for (int[] p : prerequisites) reach[p[0]][p[1]] = true;
        for (int k = 0; k < numCourses; k++)
            for (int a = 0; a < numCourses; a++)
                if (reach[a][k])
                    for (int b = 0; b < numCourses; b++) if (reach[k][b]) reach[a][b] = true;
        List<Boolean> out = new ArrayList<>(queries.length);
        for (int[] q : queries) out.add(reach[q[0]][q[1]]);
        return out;
    }
}
