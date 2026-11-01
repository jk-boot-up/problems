package com.jk.explore.problems.leetcode.p0442.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindAllDuplicatesTest {

    private final FindAllDuplicates solution = new FindAllDuplicates();

    @Test
    void examples() {
        assertEquals(List.of(2, 3), solution.findDuplicates(new int[]{4, 3, 2, 7, 8, 2, 3, 1}));
        assertEquals(List.of(1), solution.findDuplicates(new int[]{1, 1, 2}));
        assertEquals(List.of(), solution.findDuplicates(new int[]{1}));
    }
}
