package com.jk.explore.problems.leetcode.p0289.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class GameOfLifeTest {

    private final GameOfLife solution = new GameOfLife();

    @Test
    void glider() {
        int[][] b = {{0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}};
        solution.gameOfLife(b);
        assertArrayEquals(new int[][]{{0, 0, 0}, {1, 0, 1}, {0, 1, 1}, {0, 1, 0}}, b);
    }

    @Test
    void block() {
        int[][] b = {{1, 1}, {1, 0}};
        solution.gameOfLife(b);
        assertArrayEquals(new int[][]{{1, 1}, {1, 1}}, b);
    }

    @Test
    void blinker() {
        int[][] b = {{0, 0, 0}, {1, 1, 1}, {0, 0, 0}};
        solution.gameOfLife(b);
        assertArrayEquals(new int[][]{{0, 1, 0}, {0, 1, 0}, {0, 1, 0}}, b);
    }
}
