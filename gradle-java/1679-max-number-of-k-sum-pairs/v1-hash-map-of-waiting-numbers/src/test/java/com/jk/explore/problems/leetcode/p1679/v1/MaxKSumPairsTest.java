package com.jk.explore.problems.leetcode.p1679.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaxKSumPairsTest {

    private final MaxKSumPairs solution = new MaxKSumPairs();

    @Test
    void examples() {
        assertEquals(2, solution.maxOperations(new int[]{1, 2, 3, 4}, 5));
        assertEquals(1, solution.maxOperations(new int[]{3, 1, 3, 4, 3}, 6));
    }
}
