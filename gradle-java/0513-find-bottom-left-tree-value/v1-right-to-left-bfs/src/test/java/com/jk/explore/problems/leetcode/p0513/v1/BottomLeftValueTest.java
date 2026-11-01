package com.jk.explore.problems.leetcode.p0513.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BottomLeftValueTest {

    private final BottomLeftValue solution = new BottomLeftValue();

    @Test
    void examples() {
        assertEquals(1, solution.findBottomLeftValue(TreeNode.of(2, 1, 3)));
        assertEquals(7, solution.findBottomLeftValue(TreeNode.of(1, 2, 3, 4, null, 5, 6, null, null, 7)));
        assertEquals(5, solution.findBottomLeftValue(TreeNode.of(5)));
        assertEquals(3, solution.findBottomLeftValue(TreeNode.of(1, null, 2, null, 3)));
    }
}
