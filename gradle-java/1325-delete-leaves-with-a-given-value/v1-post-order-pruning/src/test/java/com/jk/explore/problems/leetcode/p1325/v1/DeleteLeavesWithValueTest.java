package com.jk.explore.problems.leetcode.p1325.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DeleteLeavesWithValueTest {

    private final DeleteLeavesWithValue solution = new DeleteLeavesWithValue();

    @Test
    void examples() {
        assertEquals(Arrays.asList(1, null, 3, null, 4), TreeNode.toList(solution.removeLeafNodes(TreeNode.of(1, 2, 3, 2, null, 2, 4), 2)));
        assertEquals(Arrays.asList(1, 3, null, null, 2), TreeNode.toList(solution.removeLeafNodes(TreeNode.of(1, 3, 3, 3, 2), 3)));
        assertEquals(List.of(1), TreeNode.toList(solution.removeLeafNodes(TreeNode.of(1, 2, null, 2, null, 2), 2)));
        assertNull(solution.removeLeafNodes(TreeNode.of(1, 1, 1), 1));
    }
}
