package com.jk.explore.problems.leetcode.p1462.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CourseScheduleIVTest {

    private final CourseScheduleIV solution = new CourseScheduleIV();

    @Test
    void examples() {
        assertEquals(List.of(false, true), solution.checkIfPrerequisite(2, new int[][]{{1, 0}}, new int[][]{{0, 1}, {1, 0}}));
        assertEquals(List.of(false, false), solution.checkIfPrerequisite(2, new int[][]{}, new int[][]{{1, 0}, {0, 1}}));
        assertEquals(List.of(true, true), solution.checkIfPrerequisite(3, new int[][]{{1, 2}, {1, 0}, {2, 0}}, new int[][]{{1, 0}, {1, 2}}));
        assertEquals(List.of(true, false), solution.checkIfPrerequisite(4, new int[][]{{0, 1}, {1, 2}, {2, 3}}, new int[][]{{0, 3}, {3, 0}}));
    }
}
