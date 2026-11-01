package com.jk.explore.problems.leetcode.p0145.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PostorderTraversalTest {

    private final PostorderTraversal solution = new PostorderTraversal();

    @Test
    void examples() {
        assertEquals(List.of(3, 2, 1), solution.postorderTraversal(TreeNode.of(1, null, 2, 3)));
        assertEquals(List.of(4, 5, 2, 3, 1), solution.postorderTraversal(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(List.of(), solution.postorderTraversal(null));
    }
}
