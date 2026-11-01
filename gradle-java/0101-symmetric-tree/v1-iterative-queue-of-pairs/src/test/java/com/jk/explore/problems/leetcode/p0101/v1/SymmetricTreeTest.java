package com.jk.explore.problems.leetcode.p0101.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SymmetricTreeTest {

    private final SymmetricTree solution = new SymmetricTree();

    @Test
    void symmetric() {
        assertTrue(solution.isSymmetric(TreeNode.of(1, 2, 2, 3, 4, 4, 3)));
    }

    @Test
    void notSymmetric() {
        assertFalse(solution.isSymmetric(TreeNode.of(1, 2, 2, null, 3, null, 3)));
    }

    @Test
    void single() {
        assertTrue(solution.isSymmetric(TreeNode.of(1)));
    }
}
