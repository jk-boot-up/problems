package com.jk.explore.problems.leetcode.p0102.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LevelOrderTraversalTest {

    private final LevelOrderTraversal solution = new LevelOrderTraversal();

    @Test
    void example() {
        assertEquals(List.of(List.of(3), List.of(9, 20), List.of(15, 7)), solution.levelOrder(TreeNode.of(3, 9, 20, null, null, 15, 7)));
    }

    @Test
    void empty() {
        assertEquals(List.of(), solution.levelOrder(null));
    }
}
