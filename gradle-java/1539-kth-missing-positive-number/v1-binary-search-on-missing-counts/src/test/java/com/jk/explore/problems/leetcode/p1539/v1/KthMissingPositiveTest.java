package com.jk.explore.problems.leetcode.p1539.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KthMissingPositiveTest {

    private final KthMissingPositive solution = new KthMissingPositive();

    @Test
    void examples() {
        assertEquals(9, solution.findKthPositive(new int[]{2, 3, 4, 7, 11}, 5));
        assertEquals(6, solution.findKthPositive(new int[]{1, 2, 3, 4}, 2));
        assertEquals(1, solution.findKthPositive(new int[]{5}, 1));
        assertEquals(6, solution.findKthPositive(new int[]{5}, 5));
    }
}
