package com.jk.explore.problems.leetcode.p1110.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DeleteNodesForestTest {

    private final DeleteNodesForest solution = new DeleteNodesForest();

    private Set<String> shapes(List<TreeNode> roots) {
        Set<String> out = new TreeSet<>();
        for (TreeNode r : roots) out.add(TreeNode.toList(r).toString());
        return out;
    }

    @Test
    void examples() {
        assertEquals(new TreeSet<>(List.of("[1, 2, null, 4]", "[6]", "[7]")), shapes(solution.delNodes(TreeNode.of(1, 2, 3, 4, 5, 6, 7), new int[]{3, 5})));
        assertEquals(new TreeSet<>(List.of("[1, 2, 4]")), shapes(solution.delNodes(TreeNode.of(1, 2, 4, null, 3), new int[]{3})));
        assertEquals(new TreeSet<>(List.of("[2]", "[3]")), shapes(solution.delNodes(TreeNode.of(1, 2, 3), new int[]{1})));
    }
}
