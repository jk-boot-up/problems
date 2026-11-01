package com.jk.explore.problems.leetcode.p0746.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinCostClimbingStairsTest {

    private final MinCostClimbingStairs solution = new MinCostClimbingStairs();

    @Test
    void examples() {
        assertEquals(15, solution.minCostClimbingStairs(new int[]{10, 15, 20}));
        assertEquals(6, solution.minCostClimbingStairs(new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}));
    }
}
