package com.jk.explore.problems.leetcode.p0165.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CompareVersionNumbersTest {

    private final CompareVersionNumbers solution = new CompareVersionNumbers();

    @ParameterizedTest
    @CsvSource({"1.2,1.10,-1", "1.01,1.001,0", "1.0,1.0.0.0,0", "0.1,1.1,-1", "1.0.1,1,1"})
    void compares(String a, String b, int expected) {
        assertEquals(expected, solution.compareVersion(a, b));
    }
}
