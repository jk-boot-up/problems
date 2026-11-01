package com.jk.explore.problems.leetcode.p0304.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NumMatrixTest {

    @Test
    void example() {
        NumMatrix m = new NumMatrix(new int[][]{{3, 0, 1, 4, 2}, {5, 6, 3, 2, 1}, {1, 2, 0, 1, 5}, {4, 1, 0, 1, 7}, {1, 0, 3, 0, 5}});
        assertEquals(8, m.sumRegion(2, 1, 4, 3));
        assertEquals(11, m.sumRegion(1, 1, 2, 2));
        assertEquals(12, m.sumRegion(1, 2, 2, 4));
        assertEquals(3, m.sumRegion(0, 0, 0, 0));
        assertEquals(58, m.sumRegion(0, 0, 4, 4));
    }
}
