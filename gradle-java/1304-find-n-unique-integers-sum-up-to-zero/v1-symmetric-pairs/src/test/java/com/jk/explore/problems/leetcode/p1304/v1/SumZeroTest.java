package com.jk.explore.problems.leetcode.p1304.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SumZeroTest {

    private final SumZero solution = new SumZero();

    @ParameterizedTest
    @CsvSource({"1", "2", "3", "5", "10", "1000"})
    void valid(int n) {
        int[] a = solution.sumZero(n);
        assertEquals(n, a.length);
        assertEquals(0, Arrays.stream(a).sum());
        assertEquals(n, Arrays.stream(a).distinct().count());
    }
}
