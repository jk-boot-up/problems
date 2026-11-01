package com.jk.explore.problems.leetcode.p0700.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SearchInBSTTest {

    private final SearchInBST solution = new SearchInBST();

    @Test
    void examples() {
        assertEquals(List.of(2, 1, 3), TreeNode.toList(solution.searchBST(TreeNode.of(4, 2, 7, 1, 3), 2)));
        assertNull(solution.searchBST(TreeNode.of(4, 2, 7, 1, 3), 5));
    }
}
