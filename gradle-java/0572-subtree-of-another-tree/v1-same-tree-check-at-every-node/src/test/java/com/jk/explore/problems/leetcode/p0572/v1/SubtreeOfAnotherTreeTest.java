package com.jk.explore.problems.leetcode.p0572.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SubtreeOfAnotherTreeTest {

    private final SubtreeOfAnotherTree solution = new SubtreeOfAnotherTree();

    @Test
    void examples() {
        assertTrue(solution.isSubtree(TreeNode.of(3, 4, 5, 1, 2), TreeNode.of(4, 1, 2)));
        assertFalse(solution.isSubtree(TreeNode.of(3, 4, 5, 1, 2, null, null, null, null, 0), TreeNode.of(4, 1, 2)));
    }
}
