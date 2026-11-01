package com.jk.explore.problems.leetcode.p0257.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BinaryTreePathsTest {

    private final BinaryTreePaths solution = new BinaryTreePaths();

    @Test
    void examples() {
        assertEquals(List.of("1->2->5", "1->3"), solution.binaryTreePaths(TreeNode.of(1, 2, 3, null, 5)));
        assertEquals(List.of("1"), solution.binaryTreePaths(TreeNode.of(1)));
        assertEquals(List.of("-1->-2"), solution.binaryTreePaths(TreeNode.of(-1, -2)));
    }
}
