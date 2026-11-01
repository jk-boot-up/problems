package com.jk.explore.problems.leetcode.p1318.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinimumFlipsTest {

    private final MinimumFlips solution = new MinimumFlips();

    @ParameterizedTest
    @CsvSource({"2,6,5,3", "4,2,7,1", "1,2,3,0"})
    void flips(int a, int b, int c, int expected) {
        assertEquals(expected, solution.minFlips(a, b, c));
    }
}
