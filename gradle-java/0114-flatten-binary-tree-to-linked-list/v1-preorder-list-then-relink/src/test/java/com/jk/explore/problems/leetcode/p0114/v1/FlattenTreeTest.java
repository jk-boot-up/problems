package com.jk.explore.problems.leetcode.p0114.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FlattenTreeTest {

    private final FlattenTree solution = new FlattenTree();

    @Test
    void example() {
        TreeNode root = TreeNode.of(1, 2, 5, 3, 4, null, 6);
        solution.flatten(root);
        assertEquals(Arrays.asList(1, null, 2, null, 3, null, 4, null, 5, null, 6), TreeNode.toList(root));
    }

    @Test
    void empty() {
        solution.flatten(null);
    }

    @Test
    void leftOnly() {
        TreeNode root = TreeNode.of(1, 2);
        solution.flatten(root);
        assertEquals(Arrays.asList(1, null, 2), TreeNode.toList(root));
    }
}
