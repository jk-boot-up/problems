package com.jk.explore.problems.leetcode.p0062.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class UniquePathsTest {

    private final UniquePaths solution = new UniquePaths();

    @ParameterizedTest
    @CsvSource({"3,7,28", "3,2,3", "1,1,1", "10,10,48620"})
    void counts(int m, int n, int expected) {
        assertEquals(expected, solution.uniquePaths(m, n));
    }
}
