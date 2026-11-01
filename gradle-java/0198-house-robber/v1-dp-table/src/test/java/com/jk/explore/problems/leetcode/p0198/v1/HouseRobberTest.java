package com.jk.explore.problems.leetcode.p0198.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class HouseRobberTest {

    private final HouseRobber solution = new HouseRobber();

    @Test
    void examples() {
        assertEquals(4, solution.rob(new int[]{1, 2, 3, 1}));
        assertEquals(12, solution.rob(new int[]{2, 7, 9, 3, 1}));
    }

    @Test
    void skipTwo() {
        assertEquals(4, solution.rob(new int[]{2, 1, 1, 2}));
    }

    @Test
    void single() {
        assertEquals(5, solution.rob(new int[]{5}));
    }
}
