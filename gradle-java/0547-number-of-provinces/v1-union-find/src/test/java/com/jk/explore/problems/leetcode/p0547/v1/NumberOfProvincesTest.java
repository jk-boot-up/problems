package com.jk.explore.problems.leetcode.p0547.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NumberOfProvincesTest {

    private final NumberOfProvinces solution = new NumberOfProvinces();

    @Test
    void examples() {
        assertEquals(2, solution.findCircleNum(new int[][]{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}}));
        assertEquals(3, solution.findCircleNum(new int[][]{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}));
    }
}
