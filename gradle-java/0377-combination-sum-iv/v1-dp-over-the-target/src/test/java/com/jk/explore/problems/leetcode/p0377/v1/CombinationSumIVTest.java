package com.jk.explore.problems.leetcode.p0377.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CombinationSumIVTest {

    private final CombinationSumIV solution = new CombinationSumIV();

    @Test
    void examples() {
        assertEquals(7, solution.combinationSum4(new int[]{1, 2, 3}, 4));
        assertEquals(0, solution.combinationSum4(new int[]{9}, 3));
        assertEquals(1, solution.combinationSum4(new int[]{1}, 1));
        assertEquals(181997601, solution.combinationSum4(new int[]{1, 2, 3}, 32));
        assertEquals(1132436852, solution.combinationSum4(new int[]{2, 1, 3}, 35));
    }
}
