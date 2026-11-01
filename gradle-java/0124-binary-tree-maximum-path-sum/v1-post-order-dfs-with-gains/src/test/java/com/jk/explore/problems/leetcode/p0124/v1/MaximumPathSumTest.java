package com.jk.explore.problems.leetcode.p0124.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumPathSumTest {

    private final MaximumPathSum solution = new MaximumPathSum();

    @Test
    void small() {
        assertEquals(6, solution.maxPathSum(TreeNode.of(1, 2, 3)));
    }

    @Test
    void avoidsRoot() {
        assertEquals(42, solution.maxPathSum(TreeNode.of(-10, 9, 20, null, null, 15, 7)));
    }

    @Test
    void allNegative() {
        assertEquals(-3, solution.maxPathSum(TreeNode.of(-3)));
        assertEquals(-1, solution.maxPathSum(TreeNode.of(-2, -1)));
    }
}
