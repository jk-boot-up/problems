package com.jk.explore.problems.leetcode.p1351.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CountNegativesTest {

    private final CountNegatives solution = new CountNegatives();

    @Test
    void examples() {
        assertEquals(8, solution.countNegatives(new int[][]{{4, 3, 2, -1}, {3, 2, 1, -1}, {1, 1, -1, -2}, {-1, -1, -2, -3}}));
        assertEquals(0, solution.countNegatives(new int[][]{{3, 2}, {1, 0}}));
        assertEquals(1, solution.countNegatives(new int[][]{{-1}}));
        assertEquals(3, solution.countNegatives(new int[][]{{5, 1, 0}, {-5, -5, -5}}));
    }
}
