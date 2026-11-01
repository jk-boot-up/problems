package com.jk.explore.problems.leetcode.p0050.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PowXNTest {

    private final PowXN solution = new PowXN();

    @Test
    void examples() {
        assertEquals(1024.0, solution.myPow(2.0, 10), 1e-9);
        assertEquals(9.261, solution.myPow(2.1, 3), 1e-9);
        assertEquals(0.25, solution.myPow(2.0, -2), 1e-12);
    }

    @Test
    void extremes() {
        assertEquals(1.0, solution.myPow(1.0, Integer.MIN_VALUE));
        assertEquals(0.0, solution.myPow(2.0, Integer.MIN_VALUE));
        assertEquals(1.0, solution.myPow(5.0, 0));
    }
}
