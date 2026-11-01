package com.jk.explore.problems.leetcode.p0094.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class InorderTraversalTest {

    private final InorderTraversal solution = new InorderTraversal();

    @Test
    void examples() {
        assertEquals(List.of(1, 3, 2), solution.inorderTraversal(TreeNode.of(1, null, 2, 3)));
        assertEquals(List.of(4, 2, 5, 1, 3), solution.inorderTraversal(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(List.of(), solution.inorderTraversal(null));
    }
}
