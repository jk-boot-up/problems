package com.jk.explore.problems.leetcode.p1295.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class EvenNumberOfDigitsTest {

    private final EvenNumberOfDigits solution = new EvenNumberOfDigits();

    @Test
    void examples() {
        assertEquals(2, solution.findNumbers(new int[]{12, 345, 2, 6, 7896}));
        assertEquals(1, solution.findNumbers(new int[]{555, 901, 482, 1771}));
        assertEquals(1, solution.findNumbers(new int[]{100000}));
    }
}
