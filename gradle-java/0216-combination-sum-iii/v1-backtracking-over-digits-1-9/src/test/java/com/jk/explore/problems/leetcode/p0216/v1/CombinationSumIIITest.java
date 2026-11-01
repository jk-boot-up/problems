package com.jk.explore.problems.leetcode.p0216.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CombinationSumIIITest {

    private final CombinationSumIII solution = new CombinationSumIII();

    @Test
    void examples() {
        assertEquals(List.of(List.of(1, 2, 4)), solution.combinationSum3(3, 7));
        assertEquals(List.of(List.of(1, 2, 6), List.of(1, 3, 5), List.of(2, 3, 4)), solution.combinationSum3(3, 9));
        assertEquals(List.of(), solution.combinationSum3(4, 1));
        assertEquals(List.of(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9)), solution.combinationSum3(9, 45));
    }
}
