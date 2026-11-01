package com.jk.explore.problems.leetcode.p0028.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class StrStrTest {

    private final StrStr solution = new StrStr();

    @ParameterizedTest
    @CsvSource({"sadbutsad,sad,0", "leetcode,leeto,-1", "aaaaab,aab,3", "abc,c,2", "mississippi,issip,4"})
    void finds(String haystack, String needle, int expected) {
        assertEquals(expected, solution.strStr(haystack, needle));
    }
}
