package com.jk.explore.problems.leetcode.p0112.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PathSumTest {

    private final PathSum solution = new PathSum();

    @Test
    void found() {
        assertTrue(solution.hasPathSum(TreeNode.of(5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1), 22));
    }

    @Test
    void notFound() {
        assertFalse(solution.hasPathSum(TreeNode.of(1, 2, 3), 5));
    }

    @Test
    void empty() {
        assertFalse(solution.hasPathSum(null, 0));
    }
}
