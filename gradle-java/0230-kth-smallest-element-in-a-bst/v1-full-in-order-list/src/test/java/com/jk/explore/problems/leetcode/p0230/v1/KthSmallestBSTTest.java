package com.jk.explore.problems.leetcode.p0230.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KthSmallestBSTTest {

    private final KthSmallestBST solution = new KthSmallestBST();

    @Test
    void first() {
        assertEquals(1, solution.kthSmallest(TreeNode.of(3, 1, 4, null, 2), 1));
    }

    @Test
    void third() {
        assertEquals(3, solution.kthSmallest(TreeNode.of(5, 3, 6, 2, 4, null, null, 1), 3));
    }

    @Test
    void largest() {
        assertEquals(6, solution.kthSmallest(TreeNode.of(5, 3, 6, 2, 4, null, null, 1), 6));
    }
}
