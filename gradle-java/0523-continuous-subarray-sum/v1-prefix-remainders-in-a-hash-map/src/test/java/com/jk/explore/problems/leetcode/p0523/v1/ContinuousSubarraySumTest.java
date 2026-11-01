package com.jk.explore.problems.leetcode.p0523.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ContinuousSubarraySumTest {

    private final ContinuousSubarraySum solution = new ContinuousSubarraySum();

    @Test
    void examples() {
        assertTrue(solution.checkSubarraySum(new int[]{23, 2, 4, 6, 7}, 6));
        assertTrue(solution.checkSubarraySum(new int[]{23, 2, 6, 4, 7}, 6));
        assertFalse(solution.checkSubarraySum(new int[]{23, 2, 6, 4, 7}, 13));
    }

    @Test
    void edgeCases() {
        assertFalse(solution.checkSubarraySum(new int[]{0}, 1));
        assertTrue(solution.checkSubarraySum(new int[]{0, 0}, 1));
        assertTrue(solution.checkSubarraySum(new int[]{5, 0, 0, 0}, 3));
        assertFalse(solution.checkSubarraySum(new int[]{1, 0}, 2));
        assertFalse(solution.checkSubarraySum(new int[]{1_000_000_000, 1_000_000_000, 1_000_000_000}, Integer.MAX_VALUE));
    }
}
