package com.jk.explore.problems.leetcode.p0733.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FloodFillTest {

    private final FloodFill solution = new FloodFill();

    @Test
    void examples() {
        assertArrayEquals(new int[][]{{2, 2, 2}, {2, 2, 0}, {2, 0, 1}}, solution.floodFill(new int[][]{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}}, 1, 1, 2));
        assertArrayEquals(new int[][]{{0, 0, 0}, {0, 0, 0}}, solution.floodFill(new int[][]{{0, 0, 0}, {0, 0, 0}}, 0, 0, 0));
    }
}
