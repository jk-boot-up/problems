package com.jk.explore.problems.leetcode.p1584.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinCostConnectPointsTest {

    private final MinCostConnectPoints solution = new MinCostConnectPoints();

    @Test
    void examples() {
        assertEquals(20, solution.minCostConnectPoints(new int[][]{{0, 0}, {2, 2}, {3, 10}, {5, 2}, {7, 0}}));
        assertEquals(18, solution.minCostConnectPoints(new int[][]{{3, 12}, {-2, 5}, {-4, 1}}));
        assertEquals(0, solution.minCostConnectPoints(new int[][]{{0, 0}}));
    }
}
