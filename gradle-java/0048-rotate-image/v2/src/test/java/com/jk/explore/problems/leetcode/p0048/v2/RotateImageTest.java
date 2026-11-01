package com.jk.explore.problems.leetcode.p0048.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RotateImageTest {

    private final RotateImage solution = new RotateImage();

    @Test
    void threeByThree() {
        int[][] m = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        solution.rotate(m);
        assertArrayEquals(new int[][]{{7, 4, 1}, {8, 5, 2}, {9, 6, 3}}, m);
    }

    @Test
    void fourByFour() {
        int[][] m = {{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}};
        solution.rotate(m);
        assertArrayEquals(new int[][]{{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11}}, m);
    }

    @Test
    void single() {
        int[][] m = {{1}};
        solution.rotate(m);
        assertArrayEquals(new int[][]{{1}}, m);
    }
}
