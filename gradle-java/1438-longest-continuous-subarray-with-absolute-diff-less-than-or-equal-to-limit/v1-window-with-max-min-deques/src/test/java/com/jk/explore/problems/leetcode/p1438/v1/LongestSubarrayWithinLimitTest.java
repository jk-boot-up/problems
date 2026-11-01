package com.jk.explore.problems.leetcode.p1438.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestSubarrayWithinLimitTest {

    private final LongestSubarrayWithinLimit solution = new LongestSubarrayWithinLimit();

    @Test
    void examples() {
        assertEquals(2, solution.longestSubarray(new int[]{8, 2, 4, 7}, 4));
        assertEquals(4, solution.longestSubarray(new int[]{10, 1, 2, 4, 7, 2}, 5));
        assertEquals(3, solution.longestSubarray(new int[]{4, 2, 2, 2, 4, 4, 2, 2}, 0));
        assertEquals(1, solution.longestSubarray(new int[]{5}, 0));
    }
}
