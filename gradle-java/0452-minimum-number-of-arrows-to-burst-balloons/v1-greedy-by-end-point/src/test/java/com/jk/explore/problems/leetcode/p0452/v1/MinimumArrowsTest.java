package com.jk.explore.problems.leetcode.p0452.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinimumArrowsTest {

    private final MinimumArrows solution = new MinimumArrows();

    @Test
    void overlapping() {
        assertEquals(2, solution.findMinArrowShots(new int[][]{{10, 16}, {2, 8}, {1, 6}, {7, 12}}));
    }

    @Test
    void disjoint() {
        assertEquals(4, solution.findMinArrowShots(new int[][]{{1, 2}, {3, 4}, {5, 6}, {7, 8}}));
    }

    @Test
    void touching() {
        assertEquals(2, solution.findMinArrowShots(new int[][]{{1, 2}, {2, 3}, {3, 4}, {4, 5}}));
    }

    @Test
    void extremeValues() {
        assertEquals(2, solution.findMinArrowShots(new int[][]{{-2147483646, -2147483645}, {2147483646, 2147483647}}));
    }
}
