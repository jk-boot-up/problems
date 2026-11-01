package com.jk.explore.problems.leetcode.p0509.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FibonacciNumberTest {

    private final FibonacciNumber solution = new FibonacciNumber();

    @ParameterizedTest
    @CsvSource({"0,0", "1,1", "2,1", "3,2", "4,3", "30,832040"})
    void values(int n, int expected) {
        assertEquals(expected, solution.fib(n));
    }
}
