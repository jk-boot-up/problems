package com.jk.explore.problems.leetcode.p0073.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SetMatrixZeroesTest {

    private final SetMatrixZeroes solution = new SetMatrixZeroes();

    @Test
    void centreZero() {
        int[][] m = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
        solution.setZeroes(m);
        assertArrayEquals(new int[][]{{1, 0, 1}, {0, 0, 0}, {1, 0, 1}}, m);
    }

    @Test
    void zerosInFirstRow() {
        int[][] m = {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}};
        solution.setZeroes(m);
        assertArrayEquals(new int[][]{{0, 0, 0, 0}, {0, 4, 5, 0}, {0, 3, 1, 0}}, m);
    }

    @Test
    void zeroInFirstColumnOnly() {
        int[][] m = {{1, 2}, {0, 3}};
        solution.setZeroes(m);
        assertArrayEquals(new int[][]{{0, 2}, {0, 0}}, m);
    }
}
