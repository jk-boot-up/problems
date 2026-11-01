package com.jk.explore.problems.leetcode.p0110.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BalancedBinaryTreeTest {

    private final BalancedBinaryTree solution = new BalancedBinaryTree();

    @Test
    void examples() {
        assertTrue(solution.isBalanced(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertFalse(solution.isBalanced(TreeNode.of(1, 2, 2, 3, 3, null, null, 4, 4)));
        assertTrue(solution.isBalanced(null));
    }
}
