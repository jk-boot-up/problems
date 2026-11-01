package com.jk.explore.problems.leetcode.p0662.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumWidthTest {

    private final MaximumWidth solution = new MaximumWidth();

    @Test
    void examples() {
        assertEquals(4, solution.widthOfBinaryTree(TreeNode.of(1, 3, 2, 5, 3, null, 9)));
        assertEquals(7, solution.widthOfBinaryTree(TreeNode.of(1, 3, 2, 5, null, null, 9, 6, null, 7)));
        assertEquals(2, solution.widthOfBinaryTree(TreeNode.of(1, 3, 2, 5)));
    }
}
