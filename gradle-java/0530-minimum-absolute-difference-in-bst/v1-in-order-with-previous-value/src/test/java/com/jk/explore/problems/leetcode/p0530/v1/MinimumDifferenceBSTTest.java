package com.jk.explore.problems.leetcode.p0530.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinimumDifferenceBSTTest {

    private final MinimumDifferenceBST solution = new MinimumDifferenceBST();

    @Test
    void example1() {
        assertEquals(1, solution.getMinimumDifference(TreeNode.of(4, 2, 6, 1, 3)));
    }

    @Test
    void example2() {
        assertEquals(1, solution.getMinimumDifference(TreeNode.of(1, 0, 48, null, null, 12, 49)));
    }

    @Test
    void twoNodes() {
        assertEquals(7, solution.getMinimumDifference(TreeNode.of(10, 3)));
    }
}
