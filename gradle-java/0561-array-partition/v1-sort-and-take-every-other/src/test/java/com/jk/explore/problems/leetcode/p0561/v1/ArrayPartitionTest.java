package com.jk.explore.problems.leetcode.p0561.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ArrayPartitionTest {

    private final ArrayPartition solution = new ArrayPartition();

    @Test
    void examples() {
        assertEquals(4, solution.arrayPairSum(new int[]{1, 4, 3, 2}));
        assertEquals(9, solution.arrayPairSum(new int[]{6, 2, 6, 5, 1, 2}));
    }
}
