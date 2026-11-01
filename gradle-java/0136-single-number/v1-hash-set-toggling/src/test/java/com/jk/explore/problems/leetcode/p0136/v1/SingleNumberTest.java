package com.jk.explore.problems.leetcode.p0136.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SingleNumberTest {

    private final SingleNumber solution = new SingleNumber();

    @Test
    void examples() {
        assertEquals(1, solution.singleNumber(new int[]{2, 2, 1}));
        assertEquals(4, solution.singleNumber(new int[]{4, 1, 2, 1, 2}));
        assertEquals(1, solution.singleNumber(new int[]{1}));
    }

    @Test
    void negatives() {
        assertEquals(-5, solution.singleNumber(new int[]{-1, -5, -1}));
    }
}
