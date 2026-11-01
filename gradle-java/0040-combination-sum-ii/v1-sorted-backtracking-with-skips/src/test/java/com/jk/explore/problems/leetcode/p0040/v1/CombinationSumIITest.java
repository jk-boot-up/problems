package com.jk.explore.problems.leetcode.p0040.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CombinationSumIITest {

    private final CombinationSumII solution = new CombinationSumII();

    @Test
    void example1() {
        assertEquals(List.of(List.of(1, 1, 6), List.of(1, 2, 5), List.of(1, 7), List.of(2, 6)), solution.combinationSum2(new int[]{10, 1, 2, 7, 6, 1, 5}, 8));
    }

    @Test
    void example2() {
        assertEquals(List.of(List.of(1, 2, 2), List.of(5)), solution.combinationSum2(new int[]{2, 5, 2, 1, 2}, 5));
    }
}
