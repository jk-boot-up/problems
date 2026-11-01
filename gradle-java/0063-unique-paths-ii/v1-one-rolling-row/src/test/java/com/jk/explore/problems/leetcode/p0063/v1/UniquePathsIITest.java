package com.jk.explore.problems.leetcode.p0063.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class UniquePathsIITest {

    private final UniquePathsII solution = new UniquePathsII();

    @Test
    void centreObstacle() {
        assertEquals(2, solution.uniquePathsWithObstacles(new int[][]{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}));
    }

    @Test
    void blockedStart() {
        assertEquals(0, solution.uniquePathsWithObstacles(new int[][]{{1}}));
    }

    @Test
    void column() {
        assertEquals(1, solution.uniquePathsWithObstacles(new int[][]{{0, 1}, {0, 0}}));
    }
}
