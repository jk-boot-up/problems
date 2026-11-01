package com.jk.explore.problems.leetcode.p0213.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class HouseRobberIITest {

    private final HouseRobberII solution = new HouseRobberII();

    @Test
    void examples() {
        assertEquals(3, solution.rob(new int[]{2, 3, 2}));
        assertEquals(4, solution.rob(new int[]{1, 2, 3, 1}));
        assertEquals(3, solution.rob(new int[]{1, 2, 3}));
        assertEquals(5, solution.rob(new int[]{5}));
    }
}
