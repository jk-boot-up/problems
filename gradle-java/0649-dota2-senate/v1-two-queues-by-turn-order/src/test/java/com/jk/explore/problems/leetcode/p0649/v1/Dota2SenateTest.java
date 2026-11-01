package com.jk.explore.problems.leetcode.p0649.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class Dota2SenateTest {

    private final Dota2Senate solution = new Dota2Senate();

    @ParameterizedTest
    @CsvSource({"RD,Radiant", "RDD,Dire", "DDRRR,Dire", "RRDDD,Radiant"})
    void predicts(String s, String expected) {
        assertEquals(expected, solution.predictPartyVictory(s));
    }
}
