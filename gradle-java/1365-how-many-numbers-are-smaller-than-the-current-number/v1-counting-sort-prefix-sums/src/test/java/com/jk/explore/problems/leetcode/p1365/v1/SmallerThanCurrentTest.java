package com.jk.explore.problems.leetcode.p1365.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SmallerThanCurrentTest {

    private final SmallerThanCurrent solution = new SmallerThanCurrent();

    @Test
    void examples() {
        assertArrayEquals(new int[]{4, 0, 1, 1, 3}, solution.smallerNumbersThanCurrent(new int[]{8, 1, 2, 2, 3}));
        assertArrayEquals(new int[]{2, 1, 0, 3}, solution.smallerNumbersThanCurrent(new int[]{6, 5, 4, 8}));
        assertArrayEquals(new int[]{0, 0, 0, 0}, solution.smallerNumbersThanCurrent(new int[]{7, 7, 7, 7}));
    }
}
