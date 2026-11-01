package com.jk.explore.problems.leetcode.p0701.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class InsertIntoBSTTest {

    private final InsertIntoBST solution = new InsertIntoBST();

    @Test
    void examples() {
        assertEquals(List.of(4, 2, 7, 1, 3, 5), TreeNode.toList(solution.insertIntoBST(TreeNode.of(4, 2, 7, 1, 3), 5)));
        assertEquals(List.of(5), TreeNode.toList(solution.insertIntoBST(null, 5)));
    }
}
