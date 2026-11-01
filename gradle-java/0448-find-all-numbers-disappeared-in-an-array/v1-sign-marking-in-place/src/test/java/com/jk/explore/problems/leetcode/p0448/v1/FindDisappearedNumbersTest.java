package com.jk.explore.problems.leetcode.p0448.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindDisappearedNumbersTest {

    private final FindDisappearedNumbers solution = new FindDisappearedNumbers();

    @Test
    void examples() {
        assertEquals(List.of(5, 6), solution.findDisappearedNumbers(new int[]{4, 3, 2, 7, 8, 2, 3, 1}));
        assertEquals(List.of(2), solution.findDisappearedNumbers(new int[]{1, 1}));
    }
}
