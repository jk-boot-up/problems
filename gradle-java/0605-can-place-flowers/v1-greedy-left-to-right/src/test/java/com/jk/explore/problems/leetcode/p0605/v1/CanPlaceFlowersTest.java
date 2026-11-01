package com.jk.explore.problems.leetcode.p0605.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CanPlaceFlowersTest {

    private final CanPlaceFlowers solution = new CanPlaceFlowers();

    @Test
    void examples() {
        assertTrue(solution.canPlaceFlowers(new int[]{1, 0, 0, 0, 1}, 1));
        assertFalse(solution.canPlaceFlowers(new int[]{1, 0, 0, 0, 1}, 2));
        assertTrue(solution.canPlaceFlowers(new int[]{0, 0, 1, 0, 0}, 2));
        assertTrue(solution.canPlaceFlowers(new int[]{0}, 1));
    }
}
