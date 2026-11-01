package com.jk.explore.problems.leetcode.p1189.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumBalloonsTest {

    private final MaximumBalloons solution = new MaximumBalloons();

    @ParameterizedTest
    @CsvSource({"nlaebolko,1", "loonbalxballpoon,2", "leetcode,0"})
    void counts(String text, int expected) {
        assertEquals(expected, solution.maxNumberOfBalloons(text));
    }
}
