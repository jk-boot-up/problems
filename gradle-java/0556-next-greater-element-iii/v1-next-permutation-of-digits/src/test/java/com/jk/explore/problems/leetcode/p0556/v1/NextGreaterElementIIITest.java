package com.jk.explore.problems.leetcode.p0556.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NextGreaterElementIIITest {

    private final NextGreaterElementIII solution = new NextGreaterElementIII();

    @ParameterizedTest
    @CsvSource({"12,21", "21,-1", "2147483486,-1", "230241,230412", "1999999999,-1"})
    void next(int n, int expected) {
        assertEquals(expected, solution.nextGreaterElement(n));
    }
}
