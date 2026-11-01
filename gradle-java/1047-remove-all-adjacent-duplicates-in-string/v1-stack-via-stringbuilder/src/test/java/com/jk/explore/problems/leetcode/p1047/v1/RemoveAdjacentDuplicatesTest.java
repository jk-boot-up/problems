package com.jk.explore.problems.leetcode.p1047.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RemoveAdjacentDuplicatesTest {

    private final RemoveAdjacentDuplicates solution = new RemoveAdjacentDuplicates();

    @ParameterizedTest
    @CsvSource({"abbaca,ca", "azxxzy,ay", "aa,''", "abc,abc"})
    void removes(String s, String expected) {
        assertEquals(expected, solution.removeDuplicates(s));
    }
}
