package com.jk.explore.problems.leetcode.p0144.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PreorderTraversalTest {

    private final PreorderTraversal solution = new PreorderTraversal();

    @Test
    void examples() {
        assertEquals(List.of(1, 2, 3), solution.preorderTraversal(TreeNode.of(1, null, 2, 3)));
        assertEquals(List.of(1, 2, 4, 5, 3), solution.preorderTraversal(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(List.of(), solution.preorderTraversal(null));
    }
}
