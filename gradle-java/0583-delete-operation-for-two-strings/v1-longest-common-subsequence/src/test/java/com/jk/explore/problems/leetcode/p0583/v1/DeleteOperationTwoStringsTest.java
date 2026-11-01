package com.jk.explore.problems.leetcode.p0583.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DeleteOperationTwoStringsTest {

    private final DeleteOperationTwoStrings solution = new DeleteOperationTwoStrings();

    @ParameterizedTest
    @CsvSource({"sea,eat,2", "leetcode,etco,4", "a,a,0", "abc,def,6", "abcde,ace,2"})
    void deletions(String a, String b, int expected) {
        assertEquals(expected, solution.minDistance(a, b));
    }
}
