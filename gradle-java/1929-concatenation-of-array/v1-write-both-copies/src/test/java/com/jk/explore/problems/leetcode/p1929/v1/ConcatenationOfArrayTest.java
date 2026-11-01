package com.jk.explore.problems.leetcode.p1929.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ConcatenationOfArrayTest {

    private final ConcatenationOfArray solution = new ConcatenationOfArray();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 2, 1, 1, 2, 1}, solution.getConcatenation(new int[]{1, 2, 1}));
        assertArrayEquals(new int[]{1, 3, 2, 1, 1, 3, 2, 1}, solution.getConcatenation(new int[]{1, 3, 2, 1}));
        assertArrayEquals(new int[]{9, 9}, solution.getConcatenation(new int[]{9}));
    }
}
