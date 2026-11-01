package com.jk.explore.problems.leetcode.p0098.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ValidateBSTTest {

    private final ValidateBST solution = new ValidateBST();

    @Test
    void valid() {
        assertTrue(solution.isValidBST(TreeNode.of(2, 1, 3)));
    }

    @Test
    void deepViolation() {
        assertFalse(solution.isValidBST(TreeNode.of(5, 1, 4, null, null, 3, 6)));
        assertFalse(solution.isValidBST(TreeNode.of(5, 4, 6, null, null, 3, 7)));
    }

    @Test
    void duplicatesAndExtremes() {
        assertFalse(solution.isValidBST(TreeNode.of(2, 2, 2)));
        assertTrue(solution.isValidBST(TreeNode.of(2147483647)));
    }
}
