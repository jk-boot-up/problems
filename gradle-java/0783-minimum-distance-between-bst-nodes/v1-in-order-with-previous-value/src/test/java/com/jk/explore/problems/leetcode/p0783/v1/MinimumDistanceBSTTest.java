package com.jk.explore.problems.leetcode.p0783.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinimumDistanceBSTTest {

    private final MinimumDistanceBST solution = new MinimumDistanceBST();

    @Test
    void examples() {
        assertEquals(1, solution.minDiffInBST(TreeNode.of(4, 2, 6, 1, 3)));
        assertEquals(1, solution.minDiffInBST(TreeNode.of(1, 0, 48, null, null, 12, 49)));
        assertEquals(1, solution.minDiffInBST(TreeNode.of(90, 69, null, 49, 89, null, 52)));
    }
}
