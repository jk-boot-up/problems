package com.jk.explore.problems.leetcode.p0007.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReverseIntegerTest {

    private final ReverseInteger solution = new ReverseInteger();

    @ParameterizedTest
    @CsvSource({"123,321", "-123,-321", "120,21", "0,0", "1534236469,0", "-2147483648,0", "1463847412,2147483641"})
    void reverses(int x, int expected) {
        assertEquals(expected, solution.reverse(x));
    }
}
