package com.jk.explore.problems.leetcode.p0416.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PartitionEqualSubsetSumTest {

    private final PartitionEqualSubsetSum solution = new PartitionEqualSubsetSum();

    @Test
    void examples() {
        assertTrue(solution.canPartition(new int[]{1, 5, 11, 5}));
        assertFalse(solution.canPartition(new int[]{1, 2, 3, 5}));
        assertFalse(solution.canPartition(new int[]{1}));
    }
}
