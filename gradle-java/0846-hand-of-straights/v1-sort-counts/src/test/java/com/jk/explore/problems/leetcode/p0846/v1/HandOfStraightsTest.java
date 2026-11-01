package com.jk.explore.problems.leetcode.p0846.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class HandOfStraightsTest {

    private final HandOfStraights solution = new HandOfStraights();

    @Test
    void examples() {
        assertTrue(solution.isNStraightHand(new int[]{1, 2, 3, 6, 2, 3, 4, 7, 8}, 3));
        assertFalse(solution.isNStraightHand(new int[]{1, 2, 3, 4, 5}, 4));
        assertTrue(solution.isNStraightHand(new int[]{8, 10, 12}, 1));
    }
}
