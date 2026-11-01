package com.jk.explore.problems.leetcode.p1710.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumUnitsOnTruckTest {

    private final MaximumUnitsOnTruck solution = new MaximumUnitsOnTruck();

    @Test
    void examples() {
        assertEquals(8, solution.maximumUnits(new int[][]{{1, 3}, {2, 2}, {3, 1}}, 4));
        assertEquals(91, solution.maximumUnits(new int[][]{{5, 10}, {2, 5}, {4, 7}, {3, 9}}, 10));
        assertEquals(10, solution.maximumUnits(new int[][]{{1, 3}, {2, 2}, {3, 1}}, 100));
    }
}
