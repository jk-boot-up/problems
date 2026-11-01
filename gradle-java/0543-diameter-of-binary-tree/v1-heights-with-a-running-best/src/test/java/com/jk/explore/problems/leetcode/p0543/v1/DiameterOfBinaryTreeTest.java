package com.jk.explore.problems.leetcode.p0543.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DiameterOfBinaryTreeTest {

    private final DiameterOfBinaryTree solution = new DiameterOfBinaryTree();

    @Test
    void examples() {
        assertEquals(3, solution.diameterOfBinaryTree(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(1, solution.diameterOfBinaryTree(TreeNode.of(1, 2)));
    }

    @Test
    void notThroughRoot() {
        assertEquals(4, solution.diameterOfBinaryTree(TreeNode.of(1, 2, null, 3, 4, 5, null, null, 6)));
    }
}
