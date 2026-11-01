package com.jk.explore.problems.leetcode.p0066.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PlusOneTest {

    private final PlusOne solution = new PlusOne();

    @Test
    void simple() {
        assertArrayEquals(new int[]{1, 2, 4}, solution.plusOne(new int[]{1, 2, 3}));
    }

    @Test
    void carry() {
        assertArrayEquals(new int[]{1, 3, 0, 0}, solution.plusOne(new int[]{1, 2, 9, 9}));
    }

    @Test
    void allNines() {
        assertArrayEquals(new int[]{1, 0, 0}, solution.plusOne(new int[]{9, 9}));
    }
}
