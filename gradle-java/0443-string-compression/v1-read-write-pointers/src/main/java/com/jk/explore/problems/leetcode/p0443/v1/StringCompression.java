package com.jk.explore.problems.leetcode.p0443.v1;

import java.util.*;

public class StringCompression {

    public int compress(char[] chars) {
        int write = 0;
        for (int read = 0; read < chars.length; ) {
            char c = chars[read];
            int start = read;
            while (read < chars.length && chars[read] == c) read++;
            chars[write++] = c;
            if (read - start > 1) {
                for (char d : String.valueOf(read - start).toCharArray()) chars[write++] = d;
            }
        }
        return write;
    }
}
