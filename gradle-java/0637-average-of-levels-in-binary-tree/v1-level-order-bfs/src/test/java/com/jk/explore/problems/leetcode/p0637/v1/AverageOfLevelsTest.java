package com.jk.explore.problems.leetcode.p0637.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AverageOfLevelsTest {

    private final AverageOfLevels solution = new AverageOfLevels();

    @Test
    void example() {
        assertEquals(List.of(3.0, 14.5, 11.0), solution.averageOfLevels(TreeNode.of(3, 9, 20, null, null, 15, 7)));
    }

    @Test
    void noOverflow() {
        assertEquals(List.of(2147483647.0, 2147483647.0), solution.averageOfLevels(TreeNode.of(2147483647, 2147483647, 2147483647)));
    }
}
