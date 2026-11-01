package com.jk.explore.problems.leetcode.p1291.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SequentialDigitsTest {

    private final SequentialDigits solution = new SequentialDigits();

    @Test
    void examples() {
        assertEquals(List.of(123, 234), solution.sequentialDigits(100, 300));
        assertEquals(List.of(1234, 2345, 3456, 4567, 5678, 6789, 12345), solution.sequentialDigits(1000, 13000));
        assertEquals(36, solution.sequentialDigits(10, 1_000_000_000).size());
        assertEquals(List.of(), solution.sequentialDigits(58, 66));
    }
}
