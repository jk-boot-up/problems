package com.jk.explore.problems.leetcode.p1609.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class EvenOddTreeTest {

    private final EvenOddTree solution = new EvenOddTree();

    @Test
    void examples() {
        assertTrue(solution.isEvenOddTree(TreeNode.of(1, 10, 4, 3, null, 7, 9, 12, 8, 6, null, null, 2)));
        assertFalse(solution.isEvenOddTree(TreeNode.of(5, 4, 2, 3, 3, 7)));
        assertFalse(solution.isEvenOddTree(TreeNode.of(5, 9, 1, 3, 5, 7)));
        assertTrue(solution.isEvenOddTree(TreeNode.of(1)));
        assertTrue(solution.isEvenOddTree(TreeNode.of(11, 8, 6, 1, 3, 9, 11, 30, 20, 18, 16, 12, 10, 4, 2, 17)));
    }
}
