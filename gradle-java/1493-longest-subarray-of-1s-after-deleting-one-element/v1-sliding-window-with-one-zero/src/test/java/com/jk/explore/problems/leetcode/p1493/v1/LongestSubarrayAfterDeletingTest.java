package com.jk.explore.problems.leetcode.p1493.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestSubarrayAfterDeletingTest {

    private final LongestSubarrayAfterDeleting solution = new LongestSubarrayAfterDeleting();

    @Test
    void examples() {
        assertEquals(3, solution.longestSubarray(new int[]{1, 1, 0, 1}));
        assertEquals(5, solution.longestSubarray(new int[]{0, 1, 1, 1, 0, 1, 1, 0, 1}));
        assertEquals(2, solution.longestSubarray(new int[]{1, 1, 1}));
    }
}
