package com.jk.explore.problems.leetcode.p1046.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LastStoneWeightTest {

    private final LastStoneWeight solution = new LastStoneWeight();

    @Test
    void examples() {
        assertEquals(1, solution.lastStoneWeight(new int[]{2, 7, 4, 1, 8, 1}));
        assertEquals(1, solution.lastStoneWeight(new int[]{1}));
        assertEquals(0, solution.lastStoneWeight(new int[]{3, 3}));
    }
}
