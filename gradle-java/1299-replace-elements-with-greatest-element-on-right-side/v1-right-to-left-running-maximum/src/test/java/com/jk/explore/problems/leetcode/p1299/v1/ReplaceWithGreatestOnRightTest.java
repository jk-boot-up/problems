package com.jk.explore.problems.leetcode.p1299.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReplaceWithGreatestOnRightTest {

    private final ReplaceWithGreatestOnRight solution = new ReplaceWithGreatestOnRight();

    @Test
    void examples() {
        assertArrayEquals(new int[]{18, 6, 6, 6, 1, -1}, solution.replaceElements(new int[]{17, 18, 5, 4, 6, 1}));
        assertArrayEquals(new int[]{-1}, solution.replaceElements(new int[]{400}));
    }
}
