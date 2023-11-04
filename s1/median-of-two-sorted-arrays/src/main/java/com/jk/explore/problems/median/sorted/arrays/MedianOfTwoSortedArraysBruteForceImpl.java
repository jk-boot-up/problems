package com.jk.explore.problems.median.sorted.arrays;

public class MedianOfTwoSortedArraysBruteForceImpl implements MedianOfTwoSortedArrays {
    @Override
    public double median(int[] sortedArrayA, int[] sortedArrayB) {
        if(isNullOrEmpty(sortedArrayA) || isNullOrEmpty(sortedArrayB)) {
            throw new IllegalArgumentException("Sorted array(s) cannot be null or empty");
        }
        int[] mergedArray = mergeSortedArrays(sortedArrayA, sortedArrayB);

        return median(mergedArray);
    }

    protected int[] mergeSortedArrays(int[] a, int[] b) {
        if(isNullOrEmpty(a) || isNullOrEmpty(b)) {
            throw new IllegalArgumentException("Sorted array(s) cannot be null or empty");
        }
        int mergedArraySize = a.length + b.length;
        int[] mergedArray = new int[mergedArraySize];
        int aPointer = 0;
        int bPointer = 0;
        int mergedArrayPointer = 0;
        while (aPointer < a.length && bPointer < b.length) {
            if(a[aPointer] < b[bPointer]) {
                mergedArray[mergedArrayPointer++] = a[aPointer++];
            } else {
                mergedArray[mergedArrayPointer++] = b[bPointer++];
            }
        }
        while (aPointer < a.length) {
            mergedArray[mergedArrayPointer++] = a[aPointer++];
        }
        while(bPointer < b.length) {
            mergedArray[mergedArrayPointer++] = b[bPointer++];
        }
        return mergedArray;
    }

    protected boolean isNullOrEmpty(int [] array) {
        return array == null || array.length == 0;
    }

    protected double median(int[] elements) {
        if(isNullOrEmpty(elements)) {
            throw new IllegalArgumentException("Elements cannot be null or empty");
        }
        int length = elements.length;
        int index = length / 2;
        if(length % 2 == 0) {
            return (double) (elements[index] + elements[index - 1]) / 2;
        } else {
            return  elements[index];
        }
    }


}
