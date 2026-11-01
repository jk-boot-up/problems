package com.jk.explore.problems.leetcode.p0387.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FirstUniqueCharacterTest {

    private final FirstUniqueCharacter solution = new FirstUniqueCharacter();

    @ParameterizedTest
    @CsvSource({"leetcode,0", "loveleetcode,2", "aabb,-1"})
    void finds(String s, int expected) {
        assertEquals(expected, solution.firstUniqChar(s));
    }
}
