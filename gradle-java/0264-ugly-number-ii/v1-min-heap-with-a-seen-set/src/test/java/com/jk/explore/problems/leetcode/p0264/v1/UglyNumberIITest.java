package com.jk.explore.problems.leetcode.p0264.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class UglyNumberIITest {

    private final UglyNumberII solution = new UglyNumberII();

    @ParameterizedTest
    @CsvSource({"1,1", "2,2", "7,8", "10,12", "11,15", "1690,2123366400"})
    void nth(int n, int expected) {
        assertEquals(expected, solution.nthUglyNumber(n));
    }
}
