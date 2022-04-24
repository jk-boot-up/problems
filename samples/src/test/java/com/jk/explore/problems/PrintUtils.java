package com.jk.explore.problems;

import java.util.stream.IntStream;

public class PrintUtils {

    public static <T> void print(T[][] matrix) {
        IntStream.range(0, matrix.length).forEach(i -> {
            IntStream.range(0, matrix[i].length).forEach(j -> {
                System.out.print(matrix[i][j]);
                System.out.print(" ");
            });
            System.out.println();
        });

    }
}
