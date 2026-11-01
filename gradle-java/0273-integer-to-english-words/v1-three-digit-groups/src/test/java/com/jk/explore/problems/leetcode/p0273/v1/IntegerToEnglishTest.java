package com.jk.explore.problems.leetcode.p0273.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IntegerToEnglishTest {

    private final IntegerToEnglish solution = new IntegerToEnglish();

    @ParameterizedTest
    @CsvSource(delimiter = '|', value = {
            "0|Zero", "5|Five", "13|Thirteen", "20|Twenty", "100|One Hundred", "123|One Hundred Twenty Three",
            "12345|Twelve Thousand Three Hundred Forty Five",
            "1234567|One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
            "1000000|One Million", "1000010|One Million Ten",
            "2147483647|Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"})
    void words(int num, String expected) {
        assertEquals(expected, solution.numberToWords(num));
    }
}
