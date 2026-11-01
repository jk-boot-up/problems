package com.jk.explore.problems.leetcode.p0263.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class UglyNumberTest {

    private final UglyNumber solution = new UglyNumber();

    @ParameterizedTest
    @CsvSource({"6,true", "1,true", "8,true", "30,true", "14,false", "0,false", "-6,false", "7,false", "2147483647,false"})
    void check(int n, boolean expected) {
        assertEquals(expected, solution.isUgly(n));
    }
}
