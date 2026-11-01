package com.jk.explore.problems.leetcode.p0383.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RansomNoteTest {

    private final RansomNote solution = new RansomNote();

    @ParameterizedTest
    @CsvSource({"a,b,false", "aa,ab,false", "aa,aab,true", "abc,cbaxyz,true"})
    void checks(String note, String magazine, boolean expected) {
        assertEquals(expected, solution.canConstruct(note, magazine));
    }
}
