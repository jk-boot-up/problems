package com.jk.explore.problems.leetcode.p1971.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindIfPathExistsTest {

    private final FindIfPathExists solution = new FindIfPathExists();

    @Test
    void examples() {
        assertTrue(solution.validPath(3, new int[][]{{0, 1}, {1, 2}, {2, 0}}, 0, 2));
        assertFalse(solution.validPath(6, new int[][]{{0, 1}, {0, 2}, {3, 5}, {5, 4}, {4, 3}}, 0, 5));
        assertTrue(solution.validPath(1, new int[][]{}, 0, 0));
        assertTrue(solution.validPath(5, new int[][]{{0, 4}, {4, 3}, {3, 1}}, 0, 1));
    }
}
