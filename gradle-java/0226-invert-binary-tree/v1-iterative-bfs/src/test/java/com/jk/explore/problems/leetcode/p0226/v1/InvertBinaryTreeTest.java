package com.jk.explore.problems.leetcode.p0226.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class InvertBinaryTreeTest {

    private final InvertBinaryTree solution = new InvertBinaryTree();

    @Test
    void full() {
        assertEquals(List.of(4, 7, 2, 9, 6, 3, 1), TreeNode.toList(solution.invertTree(TreeNode.of(4, 2, 7, 1, 3, 6, 9))));
    }

    @Test
    void small() {
        assertEquals(List.of(2, 3, 1), TreeNode.toList(solution.invertTree(TreeNode.of(2, 1, 3))));
    }

    @Test
    void empty() {
        assertNull(solution.invertTree(null));
    }
}
