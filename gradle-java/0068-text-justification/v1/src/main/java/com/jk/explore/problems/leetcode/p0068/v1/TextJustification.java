package com.jk.explore.problems.leetcode.p0068.v1;

import java.util.*;

public class TextJustification {

    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> lines = new ArrayList<>();
        int i = 0;
        while (i < words.length) {
            int j = i, letters = 0;
            while (j < words.length && letters + words[j].length() + (j - i) <= maxWidth) {
                letters += words[j].length();
                j++;
            }
            StringBuilder sb = new StringBuilder();
            int gaps = j - i - 1;
            if (j == words.length || gaps == 0) {
                for (int k = i; k < j; k++) {
                    if (k > i) sb.append(' ');
                    sb.append(words[k]);
                }
                sb.append(" ".repeat(maxWidth - sb.length()));
            } else {
                int spaces = maxWidth - letters;
                for (int k = i; k < j; k++) {
                    sb.append(words[k]);
                    if (k < j - 1) {
                        int g = k - i;
                        sb.append(" ".repeat(spaces / gaps + (g < spaces % gaps ? 1 : 0)));
                    }
                }
            }
            lines.add(sb.toString());
            i = j;
        }
        return lines;
    }
}
