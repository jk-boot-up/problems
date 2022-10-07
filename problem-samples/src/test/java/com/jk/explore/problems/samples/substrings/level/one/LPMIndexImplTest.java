package com.jk.explore.problems.samples.substrings.level.one;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class LPMIndexImplTest {

    @Test
    public void lpm() {
        LPMIndexImpl cut = new LPMIndexImpl();
        int[] results = cut.getLPMIndexArray("ABABAC");
        System.out.println(results);
        Arrays.stream(results).forEach(System.out::println);
    }
}
