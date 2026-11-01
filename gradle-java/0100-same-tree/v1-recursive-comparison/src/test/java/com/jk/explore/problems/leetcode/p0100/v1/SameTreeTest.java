package com.jk.explore.problems.leetcode.p0100.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SameTreeTest {

    private final SameTree solution = new SameTree();

    @Test
    void same() {
        assertTrue(solution.isSameTree(TreeNode.of(1, 2, 3), TreeNode.of(1, 2, 3)));
    }

    @Test
    void differentShape() {
        assertFalse(solution.isSameTree(TreeNode.of(1, 2), TreeNode.of(1, null, 2)));
    }

    @Test
    void differentValues() {
        assertFalse(solution.isSameTree(TreeNode.of(1, 2, 1), TreeNode.of(1, 1, 2)));
    }
}
