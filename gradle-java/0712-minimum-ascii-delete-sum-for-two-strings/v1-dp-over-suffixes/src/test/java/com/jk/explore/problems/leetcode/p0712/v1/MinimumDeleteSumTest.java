package com.jk.explore.problems.leetcode.p0712.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinimumDeleteSumTest {

    private final MinimumDeleteSum solution = new MinimumDeleteSum();

    @ParameterizedTest
    @CsvSource({"sea,eat,231", "delete,leet,403", "a,a,0", "a,b,195"})
    void cost(String a, String b, int expected) {
        assertEquals(expected, solution.minimumDeleteSum(a, b));
    }
}
