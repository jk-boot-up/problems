package com.jk.explore.problems.leetcode.p0313.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SuperUglyNumberTest {

    private final SuperUglyNumber solution = new SuperUglyNumber();

    @Test
    void examples() {
        assertEquals(32, solution.nthSuperUglyNumber(12, new int[]{2, 7, 13, 19}));
        assertEquals(1, solution.nthSuperUglyNumber(1, new int[]{2, 3, 5}));
        assertEquals(12, solution.nthSuperUglyNumber(10, new int[]{2, 3, 5}));
        assertEquals(1024, solution.nthSuperUglyNumber(11, new int[]{2}));
    }
}
