package com.jk.explore.problems.leetcode.p1631.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PathWithMinimumEffortTest {

    private final PathWithMinimumEffort solution = new PathWithMinimumEffort();

    @Test
    void examples() {
        assertEquals(2, solution.minimumEffortPath(new int[][]{{1, 2, 2}, {3, 8, 2}, {5, 3, 5}}));
        assertEquals(1, solution.minimumEffortPath(new int[][]{{1, 2, 3}, {3, 8, 4}, {5, 3, 5}}));
        assertEquals(0, solution.minimumEffortPath(new int[][]{{1, 2, 1, 1, 1}, {1, 2, 1, 2, 1}, {1, 2, 1, 2, 1}, {1, 2, 1, 2, 1}, {1, 1, 1, 2, 1}}));
        assertEquals(0, solution.minimumEffortPath(new int[][]{{5}}));
    }
}
