package com.jk.explore.problems.leetcode.p0594.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestHarmoniousSubsequenceTest {

    private final LongestHarmoniousSubsequence solution = new LongestHarmoniousSubsequence();

    @Test
    void examples() {
        assertEquals(5, solution.findLHS(new int[]{1, 3, 2, 2, 5, 2, 3, 7}));
        assertEquals(2, solution.findLHS(new int[]{1, 2, 3, 4}));
        assertEquals(0, solution.findLHS(new int[]{1, 1, 1, 1}));
    }
}
