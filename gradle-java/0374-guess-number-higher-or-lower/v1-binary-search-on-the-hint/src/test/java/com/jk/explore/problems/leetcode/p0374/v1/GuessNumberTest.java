package com.jk.explore.problems.leetcode.p0374.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class GuessNumberTest {

    @ParameterizedTest
    @CsvSource({"10,6", "1,1", "2,2", "2147483647,2147483647", "2126753390,1702766719"})
    void finds(int n, int pick) {
        assertEquals(pick, new GuessNumber(pick).guessNumber(n));
    }
}
