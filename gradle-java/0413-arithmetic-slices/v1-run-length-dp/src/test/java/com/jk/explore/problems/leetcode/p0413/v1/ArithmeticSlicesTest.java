package com.jk.explore.problems.leetcode.p0413.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ArithmeticSlicesTest {

    private final ArithmeticSlices solution = new ArithmeticSlices();

    @Test
    void examples() {
        assertEquals(3, solution.numberOfArithmeticSlices(new int[]{1, 2, 3, 4}));
        assertEquals(0, solution.numberOfArithmeticSlices(new int[]{1}));
        assertEquals(2, solution.numberOfArithmeticSlices(new int[]{1, 2, 3, 8, 9, 10}));
        assertEquals(6, solution.numberOfArithmeticSlices(new int[]{1, 3, 5, 7, 9}));
        assertEquals(1, solution.numberOfArithmeticSlices(new int[]{7, 7, 7}));
    }
}
