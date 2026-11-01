package com.jk.explore.problems.leetcode.p0931.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinimumFallingPathSumTest {

    private final MinimumFallingPathSum solution = new MinimumFallingPathSum();

    @Test
    void examples() {
        assertEquals(13, solution.minFallingPathSum(new int[][]{{2, 1, 3}, {6, 5, 4}, {7, 8, 9}}));
        assertEquals(-59, solution.minFallingPathSum(new int[][]{{-19, 57}, {-40, -5}}));
        assertEquals(7, solution.minFallingPathSum(new int[][]{{7}}));
    }
}
