package com.jk.explore.problems.leetcode.p1094.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CarPoolingTest {

    private final CarPooling solution = new CarPooling();

    @Test
    void examples() {
        assertFalse(solution.carPooling(new int[][]{{2, 1, 5}, {3, 3, 7}}, 4));
        assertTrue(solution.carPooling(new int[][]{{2, 1, 5}, {3, 3, 7}}, 5));
        assertTrue(solution.carPooling(new int[][]{{2, 1, 5}, {3, 5, 7}}, 3));
        assertTrue(solution.carPooling(new int[][]{{3, 2, 7}, {3, 7, 9}, {8, 3, 9}}, 11));
    }
}
