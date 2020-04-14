package com.company;

import java.util.Arrays;

/**
 * reference: https://www.youtube.com/watch?v=t0Cq6tVNRBA
 */

public class Heap {
    private int size = 0;
    private int capacity = 10;
    private int[] items = new int[capacity];

    private boolean hasLeftChild(int index) { return getLeftChildIndex(index) < size; }
    private boolean hasRightChild(int index) { return getRightChildIndex(index) < size; }
    private boolean hasParent(int index) { return getParentIndex(index) >= 0; }

    private int getLeftChildIndex(int parentIndex) { return 2 * parentIndex + 1 ; }
    private int getRightChildIndex(int parentIndex) { return 2 * parentIndex + 2; }
    private int getParentIndex(int childIndex) { return (childIndex - 1) / 2; }

    private int leftChild(int index) { return items[getLeftChildIndex(index)]; }
    private int rightChild(int index) { return items[getRightChildIndex(index)]; }
    private int parent(int index) { return items[getParentIndex(index)]; }

    private void swap(int index1, int index2) {
        int temp = items[index1];
        items[index1] = items[index2];
        items[index2] = temp;
    }

    private void ensureCapacity() {
        if (size == capacity) {
            items = Arrays.copyOf(items, capacity * 2);
            capacity *= 2;
        }
    }

    public int peek() {
        if (size == 0) {
            throw new IllegalStateException();
        }
        return items[0];
    }

    public int pop() {
        if (size == 0) {
            throw new IllegalStateException();
        }
        int item = items[0];
        items[0] = items[size - 1];
        size--;
        heapifyDown();
        return item;
    }

    public void add(int item) {
        ensureCapacity();
        items[size] = item;
        size++;
        heapifyUp();
    }

    private void heapifyUp() {
        int childIndex = size - 1;
        while (hasParent(childIndex) && parent(childIndex) > items[childIndex]) {
            int parentIndex = getParentIndex(childIndex);
            swap(childIndex, parentIndex);
            childIndex = parentIndex;
        }
    }

    private void heapifyDown() {
        int parentIndex = 0;
        while (hasLeftChild(parentIndex)) {
            int smallestIndex = getLeftChildIndex(parentIndex);
            if (hasRightChild(parentIndex) && leftChild(parentIndex) > rightChild(parentIndex)) {
                smallestIndex = getRightChildIndex(parentIndex);
            }

             if (items[parentIndex] < items[smallestIndex]) {
                 break;
             } else {
                 swap(smallestIndex, parentIndex);
             }
             parentIndex = smallestIndex;
        }
    }
}
