package com.jk.explore.problems.leetcode.p0300.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestIncreasingSubsequenceTest {

    private final LongestIncreasingSubsequence solution = new LongestIncreasingSubsequence();

    @Test
    void examples() {
        assertEquals(4, solution.lengthOfLIS(new int[]{10, 9, 2, 5, 3, 7, 101, 18}));
        assertEquals(4, solution.lengthOfLIS(new int[]{0, 1, 0, 3, 2, 3}));
        assertEquals(1, solution.lengthOfLIS(new int[]{7, 7, 7, 7}));
    }

    @Test
    void decreasing() {
        assertEquals(1, solution.lengthOfLIS(new int[]{5, 4, 3, 2, 1}));
    }
}
