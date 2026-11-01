package com.jk.explore.problems.leetcode.p0273.v1;

import java.util.*;

public class IntegerToEnglish {

    private static final String[] BELOW_20 = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    private static final String[] TENS = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    private static final String[] SCALES = {"", "Thousand", "Million", "Billion"};
    private static final int[] DIVISORS = {1, 1_000, 1_000_000, 1_000_000_000};

    public String numberToWords(int num) {
        if (num == 0) return "Zero";
        List<String> words = new ArrayList<>();
        for (int g = 3; g >= 0; g--) {
            int chunk = num / DIVISORS[g] % 1000;
            if (chunk == 0) continue;
            spell(chunk, words);
            if (g > 0) words.add(SCALES[g]);
        }
        return String.join(" ", words);
    }

    private void spell(int n, List<String> words) {
        if (n >= 100) {
            words.add(BELOW_20[n / 100]);
            words.add("Hundred");
            n %= 100;
        }
        if (n >= 20) {
            words.add(TENS[n / 10]);
            n %= 10;
        }
        if (n > 0) words.add(BELOW_20[n]);
    }
}
