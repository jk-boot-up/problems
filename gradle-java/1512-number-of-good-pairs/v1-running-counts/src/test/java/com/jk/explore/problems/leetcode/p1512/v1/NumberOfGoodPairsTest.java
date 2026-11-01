package com.jk.explore.problems.leetcode.p1512.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NumberOfGoodPairsTest {

    private final NumberOfGoodPairs solution = new NumberOfGoodPairs();

    @Test
    void examples() {
        assertEquals(4, solution.numIdenticalPairs(new int[]{1, 2, 3, 1, 1, 3}));
        assertEquals(6, solution.numIdenticalPairs(new int[]{1, 1, 1, 1}));
        assertEquals(0, solution.numIdenticalPairs(new int[]{1, 2, 3}));
    }
}
