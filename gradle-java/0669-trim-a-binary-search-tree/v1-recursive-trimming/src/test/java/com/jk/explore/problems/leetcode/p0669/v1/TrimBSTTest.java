package com.jk.explore.problems.leetcode.p0669.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TrimBSTTest {

    private final TrimBST solution = new TrimBST();

    @Test
    void examples() {
        assertEquals(Arrays.asList(1, null, 2), TreeNode.toList(solution.trimBST(TreeNode.of(1, 0, 2), 1, 2)));
        assertEquals(Arrays.asList(3, 2, null, 1), TreeNode.toList(solution.trimBST(TreeNode.of(3, 0, 4, null, 2, null, null, 1), 1, 3)));
    }
}
