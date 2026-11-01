package com.jk.explore.problems.leetcode.p1219.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PathWithMaximumGoldTest {

    private final PathWithMaximumGold solution = new PathWithMaximumGold();

    @Test
    void examples() {
        assertEquals(24, solution.getMaximumGold(new int[][]{{0, 6, 0}, {5, 8, 7}, {0, 9, 0}}));
        assertEquals(28, solution.getMaximumGold(new int[][]{{1, 0, 7}, {2, 0, 6}, {3, 4, 5}, {0, 3, 0}, {9, 0, 20}}));
        assertEquals(0, solution.getMaximumGold(new int[][]{{0}}));
    }

    @Test
    void gridIsRestored() {
        int[][] g = {{0, 6, 0}, {5, 8, 7}, {0, 9, 0}};
        solution.getMaximumGold(g);
        assertArrayEquals(new int[][]{{0, 6, 0}, {5, 8, 7}, {0, 9, 0}}, g);
    }
}
