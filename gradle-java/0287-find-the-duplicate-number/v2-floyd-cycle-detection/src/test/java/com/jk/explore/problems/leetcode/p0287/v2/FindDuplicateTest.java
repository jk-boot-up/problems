package com.jk.explore.problems.leetcode.p0287.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindDuplicateTest {

    private final FindDuplicate solution = new FindDuplicate();

    @Test
    void examples() {
        assertEquals(2, solution.findDuplicate(new int[]{1, 3, 4, 2, 2}));
        assertEquals(3, solution.findDuplicate(new int[]{3, 1, 3, 4, 2}));
        assertEquals(3, solution.findDuplicate(new int[]{3, 3, 3, 3, 3}));
    }
}
