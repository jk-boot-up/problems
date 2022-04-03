package com.jk.explore.problems;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class ZigzagConversionTest {

    @Test
    public void zigzag() {
        ZigzagConversion zigzagConversion = new ZigzagConversion();
        String input = "PAYPALISHIRING";
        String results = zigzagConversion.zigzag(input, 3);
        String expected = "PAHNAPLSIIGYIR";
        Assertions.assertEquals(results, expected);
    }
}
