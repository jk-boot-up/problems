package com.jk.explore.problems.leetcode.p0645.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SetMismatchTest {

    private final SetMismatch solution = new SetMismatch();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 3}, solution.findErrorNums(new int[]{1, 2, 2, 4}));
        assertArrayEquals(new int[]{1, 2}, solution.findErrorNums(new int[]{1, 1}));
        assertArrayEquals(new int[]{3, 1}, solution.findErrorNums(new int[]{3, 2, 3}));
    }
}
