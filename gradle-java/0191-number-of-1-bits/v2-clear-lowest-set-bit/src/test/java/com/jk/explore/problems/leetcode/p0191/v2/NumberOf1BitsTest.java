package com.jk.explore.problems.leetcode.p0191.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NumberOf1BitsTest {

    private final NumberOf1Bits solution = new NumberOf1Bits();

    @ParameterizedTest
    @CsvSource({"11,3", "128,1", "2147483645,30", "1,1"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.hammingWeight(n));
    }
}
