package com.jk.explore.problems.leetcode.p0560.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SubarraySumEqualsKTest {

    private final SubarraySumEqualsK solution = new SubarraySumEqualsK();

    @Test
    void examples() {
        assertEquals(2, solution.subarraySum(new int[]{1, 1, 1}, 2));
        assertEquals(2, solution.subarraySum(new int[]{1, 2, 3}, 3));
    }

    @Test
    void negatives() {
        assertEquals(4, solution.subarraySum(new int[]{1, -1, 1, -1}, 0));
    }
}
