package com.jk.explore.problems.leetcode.p1372.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestZigZagTest {

    private final LongestZigZag solution = new LongestZigZag();

    @Test
    void examples() {
        assertEquals(3, solution.longestZigZag(TreeNode.of(1, null, 1, 1, 1, null, null, 1, 1, null, 1, null, null, null, 1)));
        assertEquals(4, solution.longestZigZag(TreeNode.of(1, 1, 1, null, 1, null, null, 1, 1, null, 1)));
        assertEquals(0, solution.longestZigZag(TreeNode.of(1)));
    }
}
