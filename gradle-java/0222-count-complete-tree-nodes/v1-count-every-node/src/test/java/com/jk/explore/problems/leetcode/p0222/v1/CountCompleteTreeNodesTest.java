package com.jk.explore.problems.leetcode.p0222.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CountCompleteTreeNodesTest {

    private final CountCompleteTreeNodes solution = new CountCompleteTreeNodes();

    @Test
    void lastLevelPartial() {
        assertEquals(6, solution.countNodes(TreeNode.of(1, 2, 3, 4, 5, 6)));
    }

    @Test
    void perfect() {
        assertEquals(7, solution.countNodes(TreeNode.of(1, 2, 3, 4, 5, 6, 7)));
    }

    @Test
    void empty() {
        assertEquals(0, solution.countNodes(null));
    }
}
