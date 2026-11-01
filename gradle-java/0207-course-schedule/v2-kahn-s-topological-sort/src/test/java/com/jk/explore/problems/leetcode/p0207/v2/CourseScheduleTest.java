package com.jk.explore.problems.leetcode.p0207.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CourseScheduleTest {

    private final CourseSchedule solution = new CourseSchedule();

    @Test
    void possible() {
        assertTrue(solution.canFinish(2, new int[][]{{1, 0}}));
        assertTrue(solution.canFinish(4, new int[][]{{1, 0}, {2, 0}, {3, 1}, {3, 2}}));
    }

    @Test
    void cycle() {
        assertFalse(solution.canFinish(2, new int[][]{{1, 0}, {0, 1}}));
        assertFalse(solution.canFinish(3, new int[][]{{0, 1}, {1, 2}, {2, 0}}));
    }

    @Test
    void noPrerequisites() {
        assertTrue(solution.canFinish(3, new int[][]{}));
    }
}
