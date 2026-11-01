package com.jk.explore.problems.leetcode.p0210.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CourseScheduleIITest {

    private final CourseScheduleII solution = new CourseScheduleII();

    private static void assertValid(int n, int[][] pre, int[] order) {
        assertEquals(n, order.length);
        int[] pos = new int[n];
        for (int i = 0; i < n; i++) pos[order[i]] = i;
        for (int[] p : pre) assertTrue(pos[p[1]] < pos[p[0]], "prerequisite order violated");
    }

    @Test
    void diamond() {
        int[][] pre = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
        assertValid(4, pre, solution.findOrder(4, pre));
    }

    @Test
    void cycle() {
        assertArrayEquals(new int[0], solution.findOrder(2, new int[][]{{1, 0}, {0, 1}}));
    }

    @Test
    void single() {
        assertArrayEquals(new int[]{0}, solution.findOrder(1, new int[][]{}));
    }
}
