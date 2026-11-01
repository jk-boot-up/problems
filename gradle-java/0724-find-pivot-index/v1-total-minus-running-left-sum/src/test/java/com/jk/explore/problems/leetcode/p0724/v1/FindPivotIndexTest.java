package com.jk.explore.problems.leetcode.p0724.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindPivotIndexTest {

    private final FindPivotIndex solution = new FindPivotIndex();

    @Test
    void examples() {
        assertEquals(3, solution.pivotIndex(new int[]{1, 7, 3, 6, 5, 6}));
        assertEquals(-1, solution.pivotIndex(new int[]{1, 2, 3}));
        assertEquals(0, solution.pivotIndex(new int[]{2, 1, -1}));
    }
}
