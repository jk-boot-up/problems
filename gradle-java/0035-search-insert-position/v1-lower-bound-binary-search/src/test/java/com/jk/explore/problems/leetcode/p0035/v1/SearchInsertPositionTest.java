package com.jk.explore.problems.leetcode.p0035.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SearchInsertPositionTest {

    private final SearchInsertPosition solution = new SearchInsertPosition();

    @ParameterizedTest
    @CsvSource({"5,2", "2,1", "7,4", "0,0", "1,0", "6,3"})
    void finds(int target, int expected) {
        assertEquals(expected, solution.searchInsert(new int[]{1, 3, 5, 6}, target));
    }
}
