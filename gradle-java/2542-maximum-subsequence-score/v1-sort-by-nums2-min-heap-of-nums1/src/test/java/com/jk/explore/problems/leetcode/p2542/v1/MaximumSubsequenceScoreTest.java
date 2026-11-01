package com.jk.explore.problems.leetcode.p2542.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumSubsequenceScoreTest {

    private final MaximumSubsequenceScore solution = new MaximumSubsequenceScore();

    @Test
    void examples() {
        assertEquals(12, solution.maxScore(new int[]{1, 3, 3, 2}, new int[]{2, 1, 3, 4}, 3));
        assertEquals(30, solution.maxScore(new int[]{4, 2, 3, 1, 1}, new int[]{7, 5, 10, 9, 6}, 1));
    }
}
