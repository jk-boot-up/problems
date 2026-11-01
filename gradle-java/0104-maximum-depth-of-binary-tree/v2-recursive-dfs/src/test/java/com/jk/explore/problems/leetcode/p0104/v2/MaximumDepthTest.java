package com.jk.explore.problems.leetcode.p0104.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumDepthTest {

    private final MaximumDepth solution = new MaximumDepth();

    @Test
    void balanced() {
        assertEquals(3, solution.maxDepth(TreeNode.of(3, 9, 20, null, null, 15, 7)));
    }

    @Test
    void rightOnly() {
        assertEquals(2, solution.maxDepth(TreeNode.of(1, null, 2)));
    }

    @Test
    void empty() {
        assertEquals(0, solution.maxDepth(null));
    }
}
