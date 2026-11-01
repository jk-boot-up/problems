package com.jk.explore.problems.leetcode.p0695.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaxAreaOfIslandTest {

    private final MaxAreaOfIsland solution = new MaxAreaOfIsland();

    @Test
    void examples() {
        int[][] g = {{0, 0, 1, 0, 0}, {0, 1, 1, 0, 1}, {0, 0, 0, 1, 1}, {1, 1, 0, 1, 1}};
        assertEquals(5, solution.maxAreaOfIsland(g));
        assertEquals(0, solution.maxAreaOfIsland(new int[][]{{0, 0, 0}}));
    }
}
