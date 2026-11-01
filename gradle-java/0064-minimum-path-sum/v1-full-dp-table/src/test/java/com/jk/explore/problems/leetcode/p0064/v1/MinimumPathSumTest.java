package com.jk.explore.problems.leetcode.p0064.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinimumPathSumTest {

    private final MinimumPathSum solution = new MinimumPathSum();

    @Test
    void square() {
        assertEquals(7, solution.minPathSum(new int[][]{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}}));
    }

    @Test
    void wide() {
        assertEquals(12, solution.minPathSum(new int[][]{{1, 2, 3}, {4, 5, 6}}));
    }

    @Test
    void single() {
        assertEquals(5, solution.minPathSum(new int[][]{{5}}));
    }
}
