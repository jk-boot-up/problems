package com.jk.explore.problems.leetcode.p0744.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SmallestLetterGreaterThanTargetTest {

    private final SmallestLetterGreaterThanTarget solution = new SmallestLetterGreaterThanTarget();

    @Test
    void examples() {
        assertEquals('c', solution.nextGreatestLetter(new char[]{'c', 'f', 'j'}, 'a'));
        assertEquals('f', solution.nextGreatestLetter(new char[]{'c', 'f', 'j'}, 'c'));
        assertEquals('x', solution.nextGreatestLetter(new char[]{'x', 'x', 'y', 'y'}, 'z'));
    }
}
