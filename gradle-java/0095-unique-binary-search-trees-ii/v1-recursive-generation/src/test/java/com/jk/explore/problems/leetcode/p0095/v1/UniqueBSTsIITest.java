package com.jk.explore.problems.leetcode.p0095.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class UniqueBSTsIITest {

    private final UniqueBSTsII solution = new UniqueBSTsII();

    @Test
    void three() {
        Set<List<Integer>> shapes = new HashSet<>();
        for (TreeNode t : solution.generateTrees(3)) shapes.add(TreeNode.toList(t));
        assertEquals(Set.of(Arrays.asList(1, null, 2, null, 3), Arrays.asList(1, null, 3, 2), Arrays.asList(2, 1, 3),
                Arrays.asList(3, 1, null, null, 2), Arrays.asList(3, 2, null, 1)), shapes);
    }

    @Test
    void catalanCounts() {
        assertEquals(1, solution.generateTrees(1).size());
        assertEquals(14, solution.generateTrees(4).size());
    }
}
