package com.jk.explore.problems.leetcode.p0134.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class GasStationTest {

    private final GasStation solution = new GasStation();

    @Test
    void example1() {
        assertEquals(3, solution.canCompleteCircuit(new int[]{1, 2, 3, 4, 5}, new int[]{3, 4, 5, 1, 2}));
    }

    @Test
    void impossible() {
        assertEquals(-1, solution.canCompleteCircuit(new int[]{2, 3, 4}, new int[]{3, 4, 3}));
    }

    @Test
    void singleStation() {
        assertEquals(0, solution.canCompleteCircuit(new int[]{5}, new int[]{4}));
    }
}
