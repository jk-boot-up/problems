package com.jk.explore.problems.leetcode.p0039.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CombinationSumTest {

    private final CombinationSum solution = new CombinationSum();

    @Test
    void example1() {
        assertEquals(List.of(List.of(2, 2, 3), List.of(7)), solution.combinationSum(new int[]{2, 3, 6, 7}, 7));
    }

    @Test
    void example2() {
        assertEquals(List.of(List.of(2, 2, 2, 2), List.of(2, 3, 3), List.of(3, 5)), solution.combinationSum(new int[]{2, 3, 5}, 8));
    }

    @Test
    void none() {
        assertEquals(List.of(), solution.combinationSum(new int[]{2}, 1));
    }
}
