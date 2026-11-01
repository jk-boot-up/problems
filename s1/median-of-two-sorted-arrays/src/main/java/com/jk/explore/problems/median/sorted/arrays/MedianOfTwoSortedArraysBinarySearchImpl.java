package com.jk.explore.problems.median.sorted.arrays;

import static java.lang.Math.max;

public class MedianOfTwoSortedArraysBinarySearchImpl implements MedianOfTwoSortedArrays {
    @Override
    public double median(int[] sortedArrayOne, int[] sortedArrayTwo) {
        if(isNullOrEmpty(sortedArrayOne) || isNullOrEmpty(sortedArrayTwo)) {
            throw new IllegalArgumentException("sortedArrayOne or sortedArrayTwo cannot be null or empty.");
        }
        int [] arrayA = null;
        int [] arrayB = null;
        if(sortedArrayOne.length > sortedArrayTwo.length) {
            arrayA = sortedArrayTwo;
            arrayB = sortedArrayOne;
        } else {
            arrayA = sortedArrayOne;
            arrayB = sortedArrayTwo;
        }
        int aLength = arrayA.length;
        int bLength = arrayB.length;
        int startOfA = 0;
        int endOfA = aLength;
        int sizeOfMerged = aLength + bLength;
        int sizeOfLeftPartitionOfA = 0;
        int sizeOfRightPartitionOfA = 0;
        int sizeOfLeftPartitionOfB = 0;
        int sizeOfRightPartitionOfB = 0;
        int midOfA = 0;
        int maxInLeftPartitionOfA = 0;
        int maxInLeftPartitionOfB = 0;
        int minInRightPartitionOfA = 0;
        int minInRightPartitionOfB = 0;

        // this is just an approximate midOfA element index in the merged array, need not be exact midOfA index, adding
        // 1 to the total size of A and B to make the first half partition bigger than second half partition if the
        // total length of merged is odd.
        // For example if A size is 4 and B size is 5 then (4+5+1)/2=5; so the first half partition of merged array will
        // be 5 and the other half will be 4.
        int sizeOfHalfPartitionOfMerged = (sizeOfMerged + 1) / 2;
        while (startOfA <= endOfA) {
            midOfA = (startOfA + endOfA) / 2;
            sizeOfLeftPartitionOfA = midOfA;
            sizeOfRightPartitionOfA = aLength - sizeOfLeftPartitionOfA;
            sizeOfLeftPartitionOfB = sizeOfHalfPartitionOfMerged - midOfA;
            sizeOfRightPartitionOfB = bLength - sizeOfLeftPartitionOfB;
            maxInLeftPartitionOfA = sizeOfLeftPartitionOfA > 0 ? arrayA[sizeOfLeftPartitionOfA - 1] : Integer.MIN_VALUE;
            maxInLeftPartitionOfB = sizeOfLeftPartitionOfB > 0 ? arrayB[sizeOfLeftPartitionOfB -1] : Integer.MIN_VALUE;
            minInRightPartitionOfA = sizeOfLeftPartitionOfA < aLength ? arrayA[sizeOfLeftPartitionOfA] : Integer.MAX_VALUE;
            minInRightPartitionOfB = sizeOfLeftPartitionOfB < bLength ? arrayB[sizeOfLeftPartitionOfB] : Integer.MAX_VALUE;
            printPartitions(arrayA, sizeOfLeftPartitionOfA, sizeOfRightPartitionOfA, arrayB, sizeOfLeftPartitionOfB, sizeOfRightPartitionOfB);
            if(maxInLeftPartitionOfA <= minInRightPartitionOfB && maxInLeftPartitionOfB <= minInRightPartitionOfA) {
                if((bLength + aLength) % 2 == 0) {
                    return (max(maxInLeftPartitionOfA, maxInLeftPartitionOfB) + Math.min(minInRightPartitionOfA, minInRightPartitionOfB))/2.0;
                } else {
                    return max(maxInLeftPartitionOfA, maxInLeftPartitionOfB);
                }
            } else if (maxInLeftPartitionOfA > minInRightPartitionOfB) {
                endOfA = midOfA -1;
            } else {
                startOfA = midOfA + 1;
            }
        }
        return 0;
    }

    private void printPartitions(int[] arrayA, int sizeOfLeftPartitionOfA, int sizeOfRightPartitionOfA, int[] arrayB, int sizeOfLeftPartitionOfB, int sizeOfRightPartitionOfB) {
        if(sizeOfLeftPartitionOfA > 0) {
            print(arrayA, 0, sizeOfLeftPartitionOfA, "left - partition - of - A");
        }
        if(sizeOfRightPartitionOfA > 0) {
            print(arrayA, sizeOfLeftPartitionOfA, arrayA.length, "right - partition - of - A");
        }
        if(sizeOfLeftPartitionOfB > 0) {
            print(arrayB, 0, sizeOfLeftPartitionOfB, "left - partition - of - B");
        }
        if(sizeOfRightPartitionOfB > 0) {
            print(arrayB, sizeOfLeftPartitionOfB, arrayB.length, "right - partition - of - B");
        }
    }

    protected void print(int[] x, int startIndex, int endIndex, String title) {
        System.out.println("---------------");
        System.out.println(title);
        for(int i=startIndex; i < endIndex; i++) {
            System.out.print(x[i] + ", ");
        }
        System.out.println("---------------");
    }

    protected boolean isNullOrEmpty(int [] array) {
        return array == null || array.length == 0;
    }

}
