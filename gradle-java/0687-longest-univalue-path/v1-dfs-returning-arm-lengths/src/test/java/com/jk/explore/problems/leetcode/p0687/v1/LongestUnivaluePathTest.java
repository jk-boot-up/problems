package com.jk.explore.problems.leetcode.p0687.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestUnivaluePathTest {

    private final LongestUnivaluePath solution = new LongestUnivaluePath();

    @Test
    void examples() {
        assertEquals(2, solution.longestUnivaluePath(TreeNode.of(5, 4, 5, 1, 1, null, 5)));
        assertEquals(2, solution.longestUnivaluePath(TreeNode.of(1, 4, 5, 4, 4, null, 5)));
        assertEquals(0, solution.longestUnivaluePath(null));
        assertEquals(4, solution.longestUnivaluePath(TreeNode.of(1, 1, 1, 1, 1, 1)));
    }
}
