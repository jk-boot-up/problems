package com.jk.explore.problems.leetcode.p2462.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TotalCostToHireTest {

    private final TotalCostToHire solution = new TotalCostToHire();

    @Test
    void examples() {
        assertEquals(11, solution.totalCost(new int[]{17, 12, 10, 2, 7, 2, 11, 20, 8}, 3, 4));
        assertEquals(4, solution.totalCost(new int[]{1, 2, 4, 1}, 3, 3));
    }
}
