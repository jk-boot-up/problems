package com.jk.explore.problems.leetcode.p1209.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RemoveAdjacentDuplicatesIITest {

    private final RemoveAdjacentDuplicatesII solution = new RemoveAdjacentDuplicatesII();

    @ParameterizedTest
    @CsvSource({"abcd,2,abcd", "deeedbbcccbdaa,3,aa", "pbbcggttciiippooaais,2,ps", "aaaa,2,''", "aaaaa,3,aa"})
    void removes(String s, int k, String expected) {
        assertEquals(expected, solution.removeDuplicates(s, k));
    }
}
