package com.jk.explore.problems.leetcode.p0515.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LargestValuePerRowTest {

    private final LargestValuePerRow solution = new LargestValuePerRow();

    @Test
    void examples() {
        assertEquals(List.of(1, 3, 9), solution.largestValues(TreeNode.of(1, 3, 2, 5, 3, null, 9)));
        assertEquals(List.of(1, 3), solution.largestValues(TreeNode.of(1, 2, 3)));
        assertEquals(List.of(), solution.largestValues(null));
        assertEquals(List.of(Integer.MIN_VALUE), solution.largestValues(TreeNode.of(Integer.MIN_VALUE)));
    }
}
