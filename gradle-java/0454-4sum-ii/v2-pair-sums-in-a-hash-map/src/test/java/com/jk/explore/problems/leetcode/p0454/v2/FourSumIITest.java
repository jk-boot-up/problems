package com.jk.explore.problems.leetcode.p0454.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FourSumIITest {

    private final FourSumII solution = new FourSumII();

    @Test
    void examples() {
        assertEquals(2, solution.fourSumCount(new int[]{1, 2}, new int[]{-2, -1}, new int[]{-1, 2}, new int[]{0, 2}));
        assertEquals(1, solution.fourSumCount(new int[]{0}, new int[]{0}, new int[]{0}, new int[]{0}));
        assertEquals(16, solution.fourSumCount(new int[]{0, 0}, new int[]{0, 0}, new int[]{0, 0}, new int[]{0, 0}));
        assertEquals(0, solution.fourSumCount(new int[]{1}, new int[]{1}, new int[]{1}, new int[]{1}));
    }
}
