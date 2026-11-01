package com.jk.explore.problems.leetcode.p0344.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReverseStringTest {

    private final ReverseString solution = new ReverseString();

    @Test
    void hello() {
        char[] s = "hello".toCharArray();
        solution.reverseString(s);
        assertArrayEquals("olleh".toCharArray(), s);
    }

    @Test
    void even() {
        char[] s = "Hannah".toCharArray();
        solution.reverseString(s);
        assertArrayEquals("hannaH".toCharArray(), s);
    }
}
