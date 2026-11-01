package com.jk.explore.problems.leetcode.p0087.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ScrambleStringTest {

    @ParameterizedTest
    @CsvSource({"great,rgeat,true", "abcde,caebd,false", "a,a,true", "abcdbdacbdac,bdacabcdbdac,true"})
    void checks(String a, String b, boolean expected) {
        assertEquals(expected, new ScrambleString().isScramble(a, b));
    }
}
