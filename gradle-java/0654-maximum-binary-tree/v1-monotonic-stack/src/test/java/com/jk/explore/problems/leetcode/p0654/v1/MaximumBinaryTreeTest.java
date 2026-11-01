package com.jk.explore.problems.leetcode.p0654.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumBinaryTreeTest {

    private final MaximumBinaryTree solution = new MaximumBinaryTree();

    @Test
    void examples() {
        assertEquals(Arrays.asList(6, 3, 5, null, 2, 0, null, null, 1), TreeNode.toList(solution.constructMaximumBinaryTree(new int[]{3, 2, 1, 6, 0, 5})));
        assertEquals(Arrays.asList(3, null, 2, null, 1), TreeNode.toList(solution.constructMaximumBinaryTree(new int[]{3, 2, 1})));
    }
}
