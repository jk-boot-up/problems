package com.jk.explore.problems.leetcode.p0557.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReverseWordsIIITest {

    private final ReverseWordsIII solution = new ReverseWordsIII();

    @Test
    void examples() {
        assertEquals("s'teL ekat edoCteeL tsetnoc", solution.reverseWords("Let's take LeetCode contest"));
        assertEquals("rM gniD", solution.reverseWords("Mr Ding"));
    }
}
