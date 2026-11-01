package com.jk.explore.problems.leetcode.p0853.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CarFleetTest {

    private final CarFleet solution = new CarFleet();

    @Test
    void examples() {
        assertEquals(3, solution.carFleet(12, new int[]{10, 8, 0, 5, 3}, new int[]{2, 4, 1, 1, 3}));
        assertEquals(1, solution.carFleet(10, new int[]{3}, new int[]{3}));
        assertEquals(1, solution.carFleet(100, new int[]{0, 2, 4}, new int[]{4, 2, 1}));
    }
}
