# Coding Interview University

## Table of Contents

### Topics of Study

- [Algorithmic complexity / Big-O / Asymptotic analysis](#algorithmic-complexity--big-o--asymptotic-analysis)
- [Data Structures](#data-structures)
    - [Arrays](#arrays)
    - [Linked Lists](#linked-lists)
    - [Stack](#stack)
    - [Queue](#queue)
    - [Hash table](#hash-table)
- [More Knowledge](#more-knowledge)
    - [Binary search](#binary-search)
    - [Bitwise operations](#bitwise-operations)
- [Trees](#trees)
    - [Trees - Intro](#trees---intro)
    - [Binary search trees: BSTs](#binary-search-trees-bsts)
    - [Heap / Priority Queue / Binary Heap](#heap--priority-queue--binary-heap)
    - balanced search trees (general concept, not details)
    - traversals: preorder, inorder, postorder, BFS, DFS
- [Sorting](#sorting)
    - selection
    - insertion
    - heapsort
    - quicksort
    - mergesort
- [Graphs](#graphs)
    - directed
    - undirected
    - adjacency matrix
    - adjacency list
    - traversals: BFS, DFS
- [Even More Knowledge](#even-more-knowledge)
    - [Recursion](#recursion)
    - [Dynamic Programming](#dynamic-programming)
    - [Design Patterns](#design-patterns)
    - [Combinatorics (n choose k) & Probability](#combinatorics-n-choose-k--probability)
    - [NP, NP-Complete and Approximation Algorithms](#np-np-complete-and-approximation-algorithms)
    - [How computers process a program](#how-computers-process-a-program)
    - [Caches](#caches)
    - [Processes and Threads](#processes-and-threads)
    - [Testing](#testing)
    - [String searching & manipulations](#string-searching--manipulations)
    - [Tries](#tries)
    - [Floating Point Numbers](#floating-point-numbers)
    - [Unicode](#unicode)
    - [Endianness](#endianness)
    - [Networking](#networking)
- [Final Review](#final-review)

## Let's Get Started

Alright, enough talk, let's learn!

But don't forget to do coding problems from above while you learn!

## Algorithmic complexity / Big-O / Asymptotic analysis

- Nothing to implement here, you're just watching videos and taking notes! Yay!
- There are a lot of videos here. Just watch enough until you understand it. You can always come back and review.
- Don't worry if you don't understand all the math behind it.
- You just need to understand how to express the complexity of an algorithm in terms of Big-O.
- [x] [Harvard CS50 - Asymptotic Notation (video)](https://www.youtube.com/watch?v=iOq5kSKqeR4)
- [x] [Big O Notations (general quick tutorial) (video)](https://www.youtube.com/watch?v=V6mKVRU1evU)
- [X] [Big O Notation (and Omega and Theta) - best mathematical explanation (video)](https://www.youtube.com/watch?v=ei-A_wy5Yxw&index=2&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [x] [Skiena (video)](https://www.youtube.com/watch?v=z1mkCe3kVUA)
- [x] [UC Berkeley Big O (video)](https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98)
- [x] [Amortized Analysis (video)](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [x] TopCoder (includes recurrence relations and master theorem):
    - [Computational Complexity: Section 1](https://www.topcoder.com/thrive/articles/Computational%20Complexity%20part%20one)
    - [Computational Complexity: Section 2](https://www.topcoder.com/thrive/articles/Computational%20Complexity%20part%20two)
- [ ] [Cheat sheet](http://bigocheatsheet.com/)
- [X] [[Review] Big-O notation in 5 minutes (video)](https://youtu.be/__vX2sjlpXU)
- [ ] [[Review] Analyzing Algorithms (playlist) in 18 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZMxejjIyFHWa-4nKg6sdoIv)

Well, that's about enough of that.

When you go through "Cracking the Coding Interview", there is a chapter on this, and at the end there is a quiz to see
if you can identify the runtime complexity of different algorithms. It's a super review and test.

## Data Structures

- ### Arrays
    - [ ] About Arrays:
    	- [x] [Arrays CS50 Harvard University](https://www.youtube.com/watch?v=tI_tIZFyKBw&t=3009s)
        - [x] [Arrays (video)](https://www.coursera.org/lecture/data-structures/arrays-OsBSF)
        - [x] [UC Berkeley CS61B - Linear and Multi-Dim Arrays (video)](https://archive.org/details/ucberkeley_webcast_Wp8oiO_CZZE) (Start watching from 15m 32s)
        - [x] [Dynamic Arrays (video)](https://www.coursera.org/lecture/data-structures/dynamic-arrays-EwbnV)
        - [x] [Jagged Arrays (video)](https://www.youtube.com/watch?v=1jtrQqYpt7g)
    - [ ] Implement a vector (mutable array with automatic resizing):
        - [ ] Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
        - [ ] New raw data array with allocated memory
            - can allocate int array under the hood, just not use its features
            - start with 16, or if the starting number is greater, use power of 2 - 16, 32, 64, 128
        - [ ] size() - number of items
        - [ ] capacity() - number of items it can hold
        - [ ] is_empty()
        - [ ] at(index) - returns the item at a given index, blows up if index out of bounds
        - [ ] push(item)
        - [ ] insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
        - [ ] prepend(item) - can use insert above at index 0
        - [ ] pop() - remove from end, return value
        - [ ] delete(index) - delete item at index, shifting all trailing elements left
        - [ ] remove(item) - looks for value and removes index holding it (even if in multiple places)
        - [ ] find(item) - looks for value and returns first index with that value, -1 if not found
        - [ ] resize(new_capacity) // private function
            - when you reach capacity, resize to double the size
            - when popping an item, if the size is 1/4 of capacity, resize to half
    - [ ] Time
        - O(1) to add/remove at end (amortized for allocations for more space), index, or update
        - O(n) to insert/remove elsewhere
    - [ ] Space
        - contiguous in memory, so proximity helps performance
        - space needed = (array capacity, which is >= n) * size of item, but even if 2n, still O(n)

- ### Linked Lists
    - [ ] Description:
    	- [x] [Linked Lists CS50 Harvard University](https://www.youtube.com/watch?v=2T-A_GFuoTo&t=650s) - this builds the intuition.
        - [x] [Singly Linked Lists (video)](https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK)
        - [x] [CS 61B - Linked Lists 1 (video)](https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0)
        - [x] [CS 61B - Linked Lists 2 (video)](https://archive.org/details/ucberkeley_webcast_-c4I3gFYe3w)
        - [x] [[Review] Linked lists in 4 minutes (video)](https://youtu.be/F8AbOfQwl1c)
    - [x] [C Code (video)](https://www.youtube.com/watch?v=QN6FPiD0Gzo)
            - not the whole video, just portions about Node struct and memory allocation
    - [x] Linked List vs Arrays:
        - [Core Linked Lists Vs Arrays (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-linked-lists-vs-arrays-rjBs9)
        - [In The Real World Linked Lists Vs Arrays (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/in-the-real-world-lists-vs-arrays-QUaUd)
    - [x] [Why you should avoid linked lists (video)](https://www.youtube.com/watch?v=YQs6IC-vgmo)
    - [x] Gotcha: you need pointer to pointer knowledge:
        (for when you pass a pointer to a function that may change the address where that pointer points)
        This page is just to get a grasp on ptr to ptr. I don't recommend this list traversal style. Readability and maintainability suffer due to cleverness.
        - [Pointers to Pointers](https://www.eskimo.com/~scs/cclass/int/sx8.html)
    - [ ] Implement (I did with tail pointer & without):
        - [ ] size() - returns the number of data elements in the list
        - [ ] empty() - bool returns true if empty
        - [ ] value_at(index) - returns the value of the nth item (starting at 0 for first)
        - [ ] push_front(value) - adds an item to the front of the list
        - [ ] pop_front() - remove the front item and return its value
        - [ ] push_back(value) - adds an item at the end
        - [ ] pop_back() - removes end item and returns its value
        - [ ] front() - get the value of the front item
        - [ ] back() - get the value of the end item
        - [ ] insert(index, value) - insert value at index, so the current item at that index is pointed to by the new item at the index
        - [ ] erase(index) - removes node at given index
        - [ ] value_n_from_end(n) - returns the value of the node at the nth position from the end of the list
        - [ ] reverse() - reverses the list
        - [ ] remove_value(value) - removes the first item in the list with this value
    - [x] Doubly-linked List
        - [Description (video)](https://www.coursera.org/lecture/data-structures/doubly-linked-lists-jpGKD)
        - No need to implement

- ### Stack
    - [x] [Stacks (video)](https://www.coursera.org/lecture/data-structures/stacks-UdKzQ)
    - [x] [[Review] Stacks in 3 minutes (video)](https://youtu.be/KcT3aVgrrpU)
    - [ ] Will not implement. Implementing with array is trivial

- ### Queue
    - [x] [Queue (video)](https://www.coursera.org/lecture/data-structures/queues-EShpq)
    - [x] [Circular buffer/FIFO](https://en.wikipedia.org/wiki/Circular_buffer)
    - [x] [[Review] Queues in 3 minutes (video)](https://youtu.be/D6gu-_tmEpQ)
    - [ ] Implement using linked-list, with tail pointer:
        - enqueue(value) - adds value at a position at the tail
        - dequeue() - returns value and removes least recently added element (front)
        - empty()
    - [ ] Implement using a fixed-sized array:
        - enqueue(value) - adds item at end of available storage
        - dequeue() - returns value and removes least recently added element
        - empty()
        - full()
    - [ ] Cost:
        - a bad implementation using a linked list where you enqueue at the head and dequeue at the tail would be O(n)
            because you'd need the next to last element, causing a full traversal of each dequeue
        - enqueue: O(1) (amortized, linked list and array [probing])
        - dequeue: O(1) (linked list and array)
        - empty: O(1) (linked list and array)

- ### Hash table
    - [ ] Videos:
        - [x] [Hashing with Chaining (video)](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8)
        - [x] [Table Doubling, Karp-Rabin (video)](https://www.youtube.com/watch?v=BRO7mVIFt08&index=9&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
        - [x] [Open Addressing, Cryptographic Hashing (video)](https://www.youtube.com/watch?v=rvdJDijO2Ro&index=10&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
        - [x] [PyCon 2010: The Mighty Dictionary (video)](https://www.youtube.com/watch?v=C4Kc8xzcA68)
        - [x] [PyCon 2017: The Dictionary Even Mightier (video)](https://www.youtube.com/watch?v=66P5FMkWoVU)
        - [x] [(Advanced) Randomization: Universal & Perfect Hashing (video)](https://www.youtube.com/watch?v=z0lJ2k0sl1g&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=11)
        - [X] [(Advanced) Perfect hashing (video)](https://www.youtube.com/watch?v=N0COwN14gt0&list=PL2B4EEwhKD-NbwZ4ezj7gyc_3yNrojKM9&index=4)
        - [X] [[Review] Hash tables in 4 minutes (video)](https://youtu.be/knV86FlSXJ8)

    - [ ] Online Courses:
        - [x] [Core Hash Tables (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-hash-tables-m7UuP)
        - [x] [Data Structures (video)](https://www.coursera.org/learn/data-structures/home/week/4)
        - [x] [Phone Book Problem (video)](https://www.coursera.org/lecture/data-structures/phone-book-problem-NYZZP)
        - [x] distributed hash tables:
            - [Instant Uploads And Storage Optimization In Dropbox (video)](https://www.coursera.org/lecture/data-structures/instant-uploads-and-storage-optimization-in-dropbox-DvaIb)
            - [Distributed Hash Tables (video)](https://www.coursera.org/lecture/data-structures/distributed-hash-tables-tvH8H)

    - [ ] Implement with array using linear probing
        - hash(k, m) - m is the size of the hash table
        - add(key, value) - if the key already exists, update value
        - exists(key)
        - get(key)
        - remove(key)

## More Knowledge

- ### Binary search
    - [x] [Binary Search (video)](https://www.youtube.com/watch?v=D5SrAga1pno)
    - [x] [Binary Search (video)](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
    - [x] [detail](https://www.topcoder.com/thrive/articles/Binary%20Search)
    - [x] [blueprint](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)
    - [x] [[Review] Binary search in 4 minutes (video)](https://youtu.be/fDKIpRe8GW4)
    - [ ] Implement:
        - binary search (on a sorted array of integers)
        - binary search using recursion

- ### Bitwise operations
    - [x] [Bits cheat sheet](https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/bits-cheat-sheet.pdf) - you should know many of the powers of 2 from (2^1 to 2^16 and 2^32)
    - [ ] Get a really good understanding of manipulating bits with: &, |, ^, ~, >>, <<
        - [x] [words](https://en.wikipedia.org/wiki/Word_(computer_architecture))
        - [x] Good intro:
            [Bit Manipulation (video)](https://www.youtube.com/watch?v=7jkIUgLC29I)
        - [x] [C Programming Tutorial 2-10: Bitwise Operators (video)](https://www.youtube.com/watch?v=d0AwjSpNXR0)
        - [x] [Bit Manipulation](https://en.wikipedia.org/wiki/Bit_manipulation)
        - [x] [Bitwise Operation](https://en.wikipedia.org/wiki/Bitwise_operation)
        - [ ] [Bithacks](https://graphics.stanford.edu/~seander/bithacks.html)
        - [ ] [The Bit Twiddler](https://bits.stephan-brumme.com/)
        - [ ] [The Bit Twiddler Interactive](https://bits.stephan-brumme.com/interactive.html)
        - [x] [Bit Hacks (video)](https://www.youtube.com/watch?v=ZusiKXcz_ac)
		- [ ] [Practice Operations](https://pconrad.github.io/old_pconrad_cs16/topics/bitOps/)
    - [x] 2s and 1s complement
        - [Binary: Plusses & Minuses (Why We Use Two's Complement) (video)](https://www.youtube.com/watch?v=lKTsv6iVxV4)
        - [1s Complement](https://en.wikipedia.org/wiki/Ones%27_complement)
        - [2s Complement](https://en.wikipedia.org/wiki/Two%27s_complement)
    - [x] Count set bits
        - [4 ways to count bits in a byte (video)](https://youtu.be/Hzuzo9NJrlc)
        - [Count Bits](https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan)
        - [How To Count The Number Of Set Bits In a 32 Bit Integer](http://stackoverflow.com/questions/109023/how-to-count-the-number-of-set-bits-in-a-32-bit-integer)
    - [x] Swap values:
        - [Swap](https://bits.stephan-brumme.com/swap.html)
    - [x] Absolute value:
        - [Absolute Integer](https://bits.stephan-brumme.com/absInteger.html)

## Trees

- ### Trees - Intro
    - [x] [Intro to Trees (video)](https://www.coursera.org/lecture/data-structures/trees-95qda)
    - [x] [Tree Traversal (video)](https://www.coursera.org/lecture/data-structures/tree-traversal-fr51b)
    - [x] [BFS(breadth-first search) and DFS(depth-first search) (video)](https://www.youtube.com/watch?v=uWL6FJhq5fM)
        - BFS notes:
           - level order (BFS, using queue)
           - time complexity: O(n)
           - space complexity: best: O(1), worst: O(n/2)=O(n)
        - DFS notes:
            - time complexity: O(n)
            - space complexity:
                best: O(log n) - avg. height of tree
                worst: O(n)
            - inorder (DFS: left, self, right)
            - postorder (DFS: left, right, self)
            - preorder (DFS: self, left, right)
    - [x] [[Review] Breadth-first search in 4 minutes (video)](https://youtu.be/HZ5YTanv5QE)
    - [x] [[Review] Depth-first search in 4 minutes (video)](https://youtu.be/Urx87-NMm6c)
    - [x] [[Review] Tree Traversal (playlist) in 11 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZO1JC2RgEi04nLy6D-rKk6b)

- ### Binary search trees: BSTs
    - [x] [Binary Search Tree Review (video)](https://www.youtube.com/watch?v=x6At0nzX92o&index=1&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)    
    - [ ] [Introduction (video)](https://www.coursera.org/learn/data-structures/lecture/E7cXP/introduction)
    - [x] [MIT (video)](https://www.youtube.com/watch?v=76dhtgZt38A&ab_channel=MITOpenCourseWare)
    - C/C++:
        - [x] [Binary search tree - Implementation in C/C++ (video)](https://www.youtube.com/watch?v=COZK7NATh4k&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=28)
        - [x] [BST implementation - memory allocation in stack and heap (video)](https://www.youtube.com/watch?v=hWokyBoo0aI&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=29)
        - [x] [Find min and max element in a binary search tree (video)](https://www.youtube.com/watch?v=Ut90klNN264&index=30&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [x] [Find height of a binary tree (video)](https://www.youtube.com/watch?v=_pnqMz5nrRs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=31)
        - [x] [Binary tree traversal - breadth-first and depth-first strategies (video)](https://www.youtube.com/watch?v=9RHO6jU--GU&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=32)
        - [x] [Binary tree: Level Order Traversal (video)](https://www.youtube.com/watch?v=86g8jAQug04&index=33&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [x] [Binary tree traversal: Preorder, Inorder, Postorder (video)](https://www.youtube.com/watch?v=gm8DUJJhmY4&index=34&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [x] [Check if a binary tree is binary search tree or not (video)](https://www.youtube.com/watch?v=yEwSGhSsT0U&index=35&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [x] [Delete a node from Binary Search Tree (video)](https://www.youtube.com/watch?v=gcULXE7ViZw&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=36)
        - [x] [Inorder Successor in a binary search tree (video)](https://www.youtube.com/watch?v=5cPbNCrdotA&index=37&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [ ] Implement:
        - [ ] [insert    // insert value into tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/987660183/)
        - [ ] get_node_count // get count of values stored
        - [ ] print_values // prints the values in the tree, from min to max
        - [ ] delete_tree
        - [ ] is_in_tree // returns true if a given value exists in the tree
        - [ ] [get_height // returns the height in nodes (single node's height is 1)](https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/)
        - [ ] get_min   // returns the minimum value stored in the tree
        - [ ] get_max   // returns the maximum value stored in the tree
        - [ ] [is_binary_search_tree](https://leetcode.com/problems/validate-binary-search-tree/)
        - [ ] delete_value
        - [ ] get_successor // returns the next-highest value in the tree after given value, -1 if none

- ### Heap / Priority Queue / Binary Heap
    - visualized as a tree, but is usually linear in storage (array, linked list)
    - [X] [Heap](https://en.wikipedia.org/wiki/Heap_(data_structure))
    - [X] [Introduction (video)](https://www.coursera.org/lecture/data-structures/introduction-2OpTs)
    - [X] [Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/GRV2q/binary-trees)
    - [X] [Tree Height Remark (video)](https://www.coursera.org/learn/data-structures/supplement/S5xxz/tree-height-remark)
    - [X] [Basic Operations (video)](https://www.coursera.org/learn/data-structures/lecture/0g1dl/basic-operations)
    - [X] [Complete Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/gl5Ni/complete-binary-trees)
    - [X] [Pseudocode (video)](https://www.coursera.org/learn/data-structures/lecture/HxQo9/pseudocode)
    - [x] [Heap Sort - jumps to start (video)](https://youtu.be/odNJmw5TOEE?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3291)
    - [x] [Heap Sort (video)](https://www.coursera.org/lecture/data-structures/heap-sort-hSzMO)
    - [x] [Building a heap (video)](https://www.coursera.org/lecture/data-structures/building-a-heap-dwrOS)
    - [x] [MIT: Heaps and Heap Sort (video)](https://www.youtube.com/watch?v=B7hVxCmfPtM&index=4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [x] [CS 61B Lecture 24: Priority Queues (video)](https://archive.org/details/ucberkeley_webcast_yIUFT6AKBGE)
    - [x] [Linear Time BuildHeap (max-heap)](https://www.youtube.com/watch?v=MiyLo8adrWw)
    - [x] [[Review] Heap (playlist) in 13 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZNsyqgPW-DNwUeT8F8uhWc6)
    - [x] Implement a max-heap:
        - [ ] insert
        - [ ] sift_up - needed for insert
        - [ ] get_max - returns the max item, without removing it
        - [ ] get_size() - return number of elements stored
        - [ ] is_empty() - returns true if the heap contains no elements
        - [ ] extract_max - returns the max item, removing it
        - [ ] sift_down - needed for extract_max
        - [ ] remove(x) - removes item at index x
        - [ ] heapify - create a heap from an array of elements, needed for heap_sort
        - [ ] heap_sort() - take an unsorted array and turn it into a sorted array in place using a max heap or min heap

## Sorting

- [ ] Notes:
    - Implement sorts & know best case/worst case, average complexity of each:
        - no bubble sort - it's terrible - O(n^2), except when n <= 16
    - [x] Stability in sorting algorithms ("Is Quicksort stable?")
        - [Sorting Algorithm Stability](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability)
        - [Stability In Sorting Algorithms](http://stackoverflow.com/questions/1517793/stability-in-sorting-algorithms)
        - [Stability In Sorting Algorithms](http://www.geeksforgeeks.org/stability-in-sorting-algorithms/)
        - [Sorting Algorithms - Stability](http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/stability.pdf)
    - [x] Which algorithms can be used on linked lists? Which on arrays? Which on both?
        - I wouldn't recommend sorting a linked list, but merge sort is doable.
        - [Merge Sort For Linked List](http://www.geeksforgeeks.org/merge-sort-for-linked-list/)

- For heapsort, see the Heap data structure above. Heap sort is great, but not stable

- [ ] [Sedgewick - Mergesort (5 videos)](https://www.coursera.org/learn/algorithms-part1/home/week/3)
    - [x] [1. Mergesort](https://www.coursera.org/lecture/algorithms-part1/mergesort-ARWDq)
    - [x] [2. Bottom up Mergesort](https://www.coursera.org/learn/algorithms-part1/lecture/PWNEl/bottom-up-mergesort)
    - [x] [3. Sorting Complexity](https://www.coursera.org/lecture/algorithms-part1/sorting-complexity-xAltF)
    - [x] [4. Comparators](https://www.coursera.org/lecture/algorithms-part1/comparators-9FYhS)
    - [x] [5. Stability](https://www.coursera.org/learn/algorithms-part1/lecture/pvvLZ/stability)

- [ ] [Sedgewick - Quicksort (4 videos)](https://www.coursera.org/learn/algorithms-part1/home/week/3)
    - [x] [1. Quicksort](https://www.coursera.org/lecture/algorithms-part1/quicksort-vjvnC)
    - [x] [2. Selection](https://www.coursera.org/lecture/algorithms-part1/selection-UQxFT)
    - [x] [3. Duplicate Keys](https://www.coursera.org/lecture/algorithms-part1/duplicate-keys-XvjPd)
    - [x] [4. System Sorts](https://www.coursera.org/lecture/algorithms-part1/system-sorts-QBNZ7)

- [ ] UC Berkeley:
    - [x] [CS 61B Lecture 29: Sorting I (video)](https://archive.org/details/ucberkeley_webcast_EiUvYS2DT6I)
    - [x] [CS 61B Lecture 30: Sorting II (video)](https://archive.org/details/ucberkeley_webcast_2hTY3t80Qsk)
    - [x] [CS 61B Lecture 32: Sorting III (video)](https://archive.org/details/ucberkeley_webcast_Y6LOLpxg6Dc)
    - [x] [CS 61B Lecture 33: Sorting V (video)](https://archive.org/details/ucberkeley_webcast_qNMQ4ly43p4)
    - [x] [CS 61B 2014-04-21: Radix Sort(video)](https://archive.org/details/ucberkeley_webcast_pvbBMd-3NoI)

- [x] [Bubble Sort (video)](https://www.youtube.com/watch?v=P00xJgWzz2c&index=1&list=PL89B61F78B552C1AB)
- [x] [Analyzing Bubble Sort (video)](https://www.youtube.com/watch?v=ni_zk257Nqo&index=7&list=PL89B61F78B552C1AB)
- [x] [Insertion Sort, Merge Sort (video)](https://www.youtube.com/watch?v=Kg4bqzAqRBM&index=3&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
- [x] [Insertion Sort (video)](https://www.youtube.com/watch?v=c4BRHC7kTaQ&index=2&list=PL89B61F78B552C1AB)
- [x] [Merge Sort (video)](https://www.youtube.com/watch?v=GCae1WNvnZM&index=3&list=PL89B61F78B552C1AB)
- [x] [Quicksort (video)](https://www.youtube.com/watch?v=y_G9BkAm6B8&index=4&list=PL89B61F78B552C1AB)
- [x] [Selection Sort (video)](https://www.youtube.com/watch?v=6nDMgr0-Yyo&index=8&list=PL89B61F78B552C1AB)

- [ ] Merge sort code:
    - [ ] [Using output array (C)](http://www.cs.yale.edu/homes/aspnes/classes/223/examples/sorting/mergesort.c)
    - [x] [Using output array (Python)](https://github.com/jwasham/practice-python/blob/master/merge_sort/merge_sort.py)
    - [ ] [In-place (C++)](https://github.com/jwasham/practice-cpp/blob/master/merge_sort/merge_sort.cc)
- [ ] Quick sort code:
    - [ ] [Implementation (C)](http://www.cs.yale.edu/homes/aspnes/classes/223/examples/randomization/quick.c)
    - [ ] [Implementation (C)](https://github.com/jwasham/practice-c/blob/master/quick_sort/quick_sort.c)
    - [x] [Implementation (Python)](https://github.com/jwasham/practice-python/blob/master/quick_sort/quick_sort.py)

- [x] [[Review] Sorting (playlist) in 18 minutes](https://www.youtube.com/playlist?list=PL9xmBV_5YoZOZSbGAXAPIq1BeUf4j20pl)
    - [ ] [Quick sort in 4 minutes (video)](https://youtu.be/Hoixgm4-P4M)
    - [ ] [Heap sort in 4 minutes (video)](https://youtu.be/2DmK_H7IdTo)
    - [ ] [Merge sort in 3 minutes (video)](https://youtu.be/4VqmGXwpLqc)
    - [ ] [Bubble sort in 2 minutes (video)](https://youtu.be/xli_FI7CuzA)
    - [ ] [Selection sort in 3 minutes (video)](https://youtu.be/g-PGLbMth_g)
    - [ ] [Insertion sort in 2 minutes (video)](https://youtu.be/JU767SDMDvA)

- [x] Implement:
    - [x] Mergesort: O(n log n) average and worst case
    - [x] Quicksort O(n log n) average case
    - [x] Selection sort and insertion sort are both O(n^2) average and worst-case
    - [x] For heapsort, see Heap data structure above

- [ ] Not required, but I recommended them:
    - [ ] [Sedgewick - Radix Sorts (6 videos)](https://www.coursera.org/learn/algorithms-part2/home/week/3)
        - [ ] [1. Strings in Java](https://www.coursera.org/learn/algorithms-part2/lecture/vGHvb/strings-in-java)
        - [ ] [2. Key Indexed Counting](https://www.coursera.org/lecture/algorithms-part2/key-indexed-counting-2pi1Z)
        - [ ] [3. Least Significant Digit First String Radix Sort](https://www.coursera.org/learn/algorithms-part2/lecture/c1U7L/lsd-radix-sort)
        - [ ] [4. Most Significant Digit First String Radix Sort](https://www.coursera.org/learn/algorithms-part2/lecture/gFxwG/msd-radix-sort)
        - [ ] [5. 3 Way Radix Quicksort](https://www.coursera.org/lecture/algorithms-part2/3-way-radix-quicksort-crkd5)
        - [ ] [6. Suffix Arrays](https://www.coursera.org/learn/algorithms-part2/lecture/TH18W/suffix-arrays)
    - [ ] [Radix Sort](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#radixSort)
    - [ ] [Radix Sort (video)](https://www.youtube.com/watch?v=xhr26ia4k38)
    - [ ] [Radix Sort, Counting Sort (linear time given constraints) (video)](https://www.youtube.com/watch?v=Nz1KZXbghj8&index=7&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [ ] [Randomization: Matrix Multiply, Quicksort, Freivalds' algorithm (video)](https://www.youtube.com/watch?v=cNB2lADK3_s&index=8&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
    - [ ] [Sorting in Linear Time (video)](https://www.youtube.com/watch?v=pOKy3RZbSws&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf&index=14)

As a summary, here is a visual representation of [15 sorting algorithms](https://www.youtube.com/watch?v=kPRA0W1kECg).
If you need more detail on this subject, see the "Sorting" section in [Additional Detail on Some Subjects](#additional-detail-on-some-subjects)

## Graphs

Graphs can be used to represent many problems in computer science, so this section is long, like trees and sorting.

- Notes:
    - There are 4 basic ways to represent a graph in memory:
        - objects and pointers
        - adjacency matrix
        - adjacency list
        - adjacency map
    - Familiarize yourself with each representation and its pros & cons
    - BFS and DFS - know their computational complexity, their trade-offs, and how to implement them in real code
    - When asked a question, look for a graph-based solution first, then move on if none

- [ ] MIT(videos):
    - [x] [Breadth-First Search](https://www.youtube.com/watch?v=oFVYVzlvk9c&t=14s&ab_channel=MITOpenCourseWare)
    - [x] [Depth-First Search](https://www.youtube.com/watch?v=IBfWDYSffUU&t=32s&ab_channel=MITOpenCourseWare)

- [ ] Skiena Lectures - great intro:
    - [x] [CSE373 2020 - Lecture 10 - Graph Data Structures (video)](https://www.youtube.com/watch?v=Sjk0xqWWPCc&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=10)
    - [x] [CSE373 2020 - Lecture 11 - Graph Traversal (video)](https://www.youtube.com/watch?v=ZTwjXj81NVY&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=11)
    - [x] [CSE373 2020 - Lecture 12 - Depth First Search (video)](https://www.youtube.com/watch?v=KyordYB3BOs&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=12)
    - [x] [CSE373 2020 - Lecture 13 - Minimum Spanning Trees (video)](https://www.youtube.com/watch?v=oolm2VnJUKw&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=13)
    - [x] [CSE373 2020 - Lecture 14 - Minimum Spanning Trees (con't) (video)](https://www.youtube.com/watch?v=RktgPx0MarY&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=14)
    - [x] [CSE373 2020 - Lecture 15 - Graph Algorithms (con't 2) (video)](https://www.youtube.com/watch?v=MUe5DXRhyAo&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=15)

- [ ] Graphs (review and more):

    - [x] [6.006 Single-Source Shortest Paths Problem (video)](https://www.youtube.com/watch?v=Aa2sqUhIn-E&index=15&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [x] [6.006 Dijkstra (video)](https://www.youtube.com/watch?v=NSHizBK9JD8&t=1731s&ab_channel=MITOpenCourseWare)
    - [x] [6.006 Bellman-Ford (video)](https://www.youtube.com/watch?v=f9cVS_URPc0&ab_channel=MITOpenCourseWare)
    - [x] [6.006 Speeding Up Dijkstra (video)](https://www.youtube.com/watch?v=CHvQ3q_gJ7E&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=18)
    - [x] [Aduni: Graph Algorithms I - Topological Sorting, Minimum Spanning Trees, Prim's Algorithm -  Lecture 6 (video)]( https://www.youtube.com/watch?v=i_AQT_XfvD8&index=6&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
    - [x] [Aduni: Graph Algorithms II - DFS, BFS, Kruskal's Algorithm, Union Find Data Structure - Lecture 7 (video)]( https://www.youtube.com/watch?v=ufj5_bppBsA&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=7)
    - [x] [Aduni: Graph Algorithms III: Shortest Path - Lecture 8 (video)](https://www.youtube.com/watch?v=DiedsPsMKXc&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=8)
    - [x] [Aduni: Graph Alg. IV: Intro to geometric algorithms - Lecture 9 (video)](https://www.youtube.com/watch?v=XIAQRlNkJAw&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=9)
    - [x] [CS 61B 2014: Weighted graphs (video)](https://archive.org/details/ucberkeley_webcast_zFbq8vOZ_0k)
    - [x] [Greedy Algorithms: Minimum Spanning Tree (video)](https://www.youtube.com/watch?v=tKwnms5iRBU&index=16&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
    - [x] [Strongly Connected Components Kosaraju's Algorithm Graph Algorithm (video)](https://www.youtube.com/watch?v=RpgcYiky7uw)
    - [x] [[Review] Shortest Path Algorithms (playlist) in 16 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZO-Y-H3xIC9DGSfVYJng9Yw)
    - [x] [[Review] Minimum Spanning Trees (playlist) in 4 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZObEi3Hf6lmyW-CBfs7nkOV)

- Full Coursera Course:
    - [ ] [Algorithms on Graphs (video)](https://www.coursera.org/learn/algorithms-on-graphs/home/welcome)

- I'll implement:
    - [x] [DFS with adjacency list (recursive)](src/Grpahs-DFSWithAdjacencyList(Recursive).py)
    - [x] [DFS with adjacency list (iterative with stack)](src/Graphs-DFSWithAdjacencyList(IterativeWithStack).py)
    - [X] [DFS with adjacency matrix (recursive)](src/Graphs-DFSWithAdjacencyMatrix(Recursive).py)
    - [x] [DFS with adjacency matrix (iterative with stack)](src/Graphs-DFSWithAdjacencyMatrix(IterativeWithStack).py)
    - [x] [BFS with adjacency list](src/Graphs-BFSWithAdjacencyList.py)
    - [x] [BFS with adjacency matrix](src/Graphs-BFSWithAdjacencyMatrix.py)
    - [x] [single-source shortest path (Dijkstra)](src/Graphs-Single-SourceShortestPath(Dijkstra).py)
    - [x] [minimum spanning tree(Prim)](src/Graphs-MinimumSpanningTree.py)
    - [x] [minimum spanning tree(Kruskal)](src/Graphs-MinimumSpanningTree(Kruskal).py)
    - [x] [union-find](src/Graphs-UnionFind.py)
    - DFS-based algorithms (see Aduni videos above):
        - [x] check for a cycle (needed for topological sort, since we'll check for the cycle before starting)
        - [x] [topological sort](src/Graphs-TopologicalSort.py)
        - [x] [count connected components in a graph](src/Graphs-CountConnectedComponentsInAGraph.py)
        - [x] list strongly connected components
        - [x] [check for bipartite graph](src/Graphs-CheckForBipartiteGraph.py)

## Even More Knowledge

- ### Recursion
    - [ ] Stanford lectures on recursion & backtracking:
        - [x] [Lecture 8 | Programming Abstractions (video)](https://www.youtube.com/watch?v=gl3emqCuueQ&list=PLFE6E58F856038C69&index=8)
        - [x] [Lecture 9 | Programming Abstractions (video)](https://www.youtube.com/watch?v=uFJhEPrbycQ&list=PLFE6E58F856038C69&index=9)
        - [x] [Lecture 10 | Programming Abstractions (video)](https://www.youtube.com/watch?v=NdF1QDTRkck&index=10&list=PLFE6E58F856038C69)
        - [x] [Lecture 11 | Programming Abstractions (video)](https://www.youtube.com/watch?v=p-gpaIGRCQI&list=PLFE6E58F856038C69&index=11)
    - When it is appropriate to use it?
    - How is tail recursion better than not?
        - [x] [What Is Tail Recursion Why Is It So Bad?](https://www.quora.com/What-is-tail-recursion-Why-is-it-so-bad)
        - [x] [Tail Recursion (video)](https://www.coursera.org/lecture/programming-languages/tail-recursion-YZic1)
    - [x] [5 Simple Steps for Solving Any Recursive Problem(video)](https://youtu.be/ngCos392W4w)
	
	Backtracking Blueprint: [Java](https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning))
	[Python](https://leetcode.com/problems/combination-sum/discuss/429538/General-Backtracking-questions-solutions-in-Python-for-reference-%3A)
- ### Dynamic Programming
    - You probably won't see any dynamic programming problems in your interview, but it's worth being able to recognize a
    problem as being a candidate for dynamic programming.
    - This subject can be pretty difficult, as each DP soluble problem must be defined as a recursion relation, and coming up with it can be tricky.
    - I suggest looking at many examples of DP problems until you have a solid understanding of the pattern involved.
    - [ ] Videos:
        - [x] [Skiena: CSE373 2020 - Lecture 19 - Introduction to Dynamic Programming (video)](https://www.youtube.com/watch?v=wAA0AMfcJHQ&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=18)
        - [x] [Skiena: CSE373 2020 - Lecture 20 - Edit Distance (video)](https://www.youtube.com/watch?v=T3A4jlHlhtA&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=19)
        - [x] [Skiena: CSE373 2020 - Lecture 20 - Edit Distance (continued) (video)](https://www.youtube.com/watch?v=iPnPVcZmRbE&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=20)
        - [x] [Skiena: CSE373 2020 - Lecture 21 - Dynamic Programming (video)](https://www.youtube.com/watch?v=2xPE4Wq8coQ&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=21)
        - [x] [Skiena: CSE373 2020 - Lecture 22 - Dynamic Programming and Review (video)](https://www.youtube.com/watch?v=Yh3RzqQGsyI&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=22)
        - [X] [Simonson: Dynamic Programming 0 (starts at 59:18) (video)](https://youtu.be/J5aJEcOr6Eo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3558)
        - [X] [Simonson: Dynamic Programming I - Lecture 11 (video)](https://www.youtube.com/watch?v=0EzHjQ_SOeU&index=11&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
        - [x] [Simonson: Dynamic programming II - Lecture 12 (video)](https://www.youtube.com/watch?v=v1qiRwuJU7g&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=12)
        - [x] List of individual DP problems (each is short):
            [Dynamic Programming (video)](https://www.youtube.com/playlist?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr)
    - [ ] Yale Lecture notes:
        - [x] [Dynamic Programming](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#dynamicProgramming)
    - [ ] Coursera:
        - [x] [The RNA secondary structure problem (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/80RrW/the-rna-secondary-structure-problem)
        - [x] [A dynamic programming algorithm (video)](https://www.coursera.org/lecture/algorithmic-thinking-2/a-dynamic-programming-algorithm-PSonq)
        - [x] [Illustrating the DP algorithm (video)](https://www.coursera.org/lecture/algorithmic-thinking-2/illustrating-the-dp-algorithm-oUEK2)
        - [x] [Running time of the DP algorithm (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/nfK2r/running-time-of-the-dp-algorithm)
        - [x] [DP vs. recursive implementation (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/M999a/dp-vs-recursive-implementation)
        - [x] [Global pairwise sequence alignment (video)](https://www.coursera.org/lecture/algorithmic-thinking-2/global-pairwise-sequence-alignment-UZ7o6)
        - [x] [Local pairwise sequence alignment (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/WnNau/local-pairwise-sequence-alignment)

- ### Design patterns
    - [x] [Quick UML review (video)](https://www.youtube.com/watch?v=3cmzqZzwNDM&list=PLGLfVvz_LVvQ5G-LdJ8RLqe-ndo7QITYc&index=3)
    - [ ] Learn these patterns:
        - [ ] strategy
        - [ ] singleton
        - [ ] adapter
        - [ ] prototype
        - [ ] decorator
        - [ ] visitor
        - [ ] factory, abstract factory
        - [ ] facade
        - [ ] observer
        - [ ] proxy
        - [ ] delegate
        - [ ] command
        - [ ] state
        - [ ] memento
        - [ ] iterator
        - [ ] composite
        - [ ] flyweight
    - [x] [Series of videos (27 videos)](https://www.youtube.com/playlist?list=PLF206E906175C7E07)
    - [x] [Book: Head First Design Patterns](https://www.amazon.com/Head-First-Design-Patterns-Freeman/dp/0596007124)
        - I know the canonical book is "Design Patterns: Elements of Reusable Object-Oriented Software", but Head First is great for beginners to OO.
    - [Handy reference: 101 Design Patterns & Tips for Developers](https://sourcemaking.com/design-patterns-and-tips)

- ### Combinatorics (n choose k) & Probability
    - [x] [Math Skills: How to find Factorial, Permutation and Combination (Choose) (video)](https://www.youtube.com/watch?v=8RRo6Ti9d0U)
    - [x] [Make School: Probability (video)](https://www.youtube.com/watch?v=sZkAAk9Wwa4)
    - [x] [Make School: More Probability and Markov Chains (video)](https://www.youtube.com/watch?v=dNaJg-mLobQ)
    - [x] Khan Academy:
        - Course layout:
            - [x] [Basic Theoretical Probability](https://www.khanacademy.org/math/probability/probability-and-combinatorics-topic)
        - Just the videos - 41 (each are simple and each are short):
            - [x] [Probability Explained (video)](https://www.youtube.com/watch?v=uzkc-qNVoOk&list=PLC58778F28211FA19)

- ### NP, NP-Complete and Approximation Algorithms
    - Know about the most famous classes of NP-complete problems, such as the traveling salesman and the knapsack problem,
        and be able to recognize them when an interviewer asks you them in disguise.
    - Know what NP-complete means.
    - [ ] [Computational Complexity (video)](https://www.youtube.com/watch?v=moPtwq_cVH8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=23)
    - [ ] Simonson:
        - [ ] [Greedy Algs. II & Intro to NP-Completeness (video)](https://youtu.be/qcGnJ47Smlo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=2939)
        - [ ] [NP Completeness II & Reductions (video)](https://www.youtube.com/watch?v=e0tGC6ZQdQE&index=16&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
        - [ ] [NP Completeness III (Video)](https://www.youtube.com/watch?v=fCX1BGT3wjE&index=17&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
        - [ ] [NP Completeness IV (video)](https://www.youtube.com/watch?v=NKLDp3Rch3M&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=18)
    - [ ] Skiena:
        - [ ] [CSE373 2020 - Lecture 23 - NP-Completeness (video)](https://www.youtube.com/watch?v=ItHp5laE1VE&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=23)
        - [ ] [CSE373 2020 - Lecture 24 - Satisfiability (video)](https://www.youtube.com/watch?v=inaFJeCzGxU&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=24)
        - [ ] [CSE373 2020 - Lecture 25 - More NP-Completeness (video)](https://www.youtube.com/watch?v=B-bhKxjZLlc&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=25)
        - [ ] [CSE373 2020 - Lecture 26 - NP-Completeness Challenge (video)](https://www.youtube.com/watch?v=_EzetTkG_Cc&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=26)
    - [ ] [Complexity: P, NP, NP-completeness, Reductions (video)](https://www.youtube.com/watch?v=eHZifpgyH_4&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=22)
    - [ ] [Complexity: Approximation Algorithms (video)](https://www.youtube.com/watch?v=MEz1J9wY2iM&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=24)
    - [ ] [Complexity: Fixed-Parameter Algorithms (video)](https://www.youtube.com/watch?v=4q-jmGrmxKs&index=25&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
    - Peter Norvig discusses near-optimal solutions to the traveling salesman problem:
        - [Jupyter Notebook](http://nbviewer.jupyter.org/url/norvig.com/ipython/TSP.ipynb)
    - Pages 1048 - 1140 in CLRS if you have it.

- ### How computers process a program

    - [ ] [How CPU executes a program (video)](https://www.youtube.com/watch?v=XM4lGflQFvA)
    - [ ] [How computers calculate - ALU (video)](https://youtu.be/1I5ZMmrOfnA)
    - [ ] [Registers and RAM (video)](https://youtu.be/fpnE6UAfbtU)
    - [ ] [The Central Processing Unit (CPU) (video)](https://youtu.be/FZGugFqdr60)
    - [ ] [Instructions and Programs (video)](https://youtu.be/zltgXvg6r3k)
- ### Caches
    - [ ] LRU cache:
        - [x] [The Magic of LRU Cache (100 Days of Google Dev) (video)](https://www.youtube.com/watch?v=R5ON3iwx78M)
        - [x] [Implementing LRU (video)](https://www.youtube.com/watch?v=bq6N7Ym81iI)
        - [x] [LeetCode - 146 LRU Cache (C++) (video)](https://www.youtube.com/watch?v=8-FZRAjR7qU)
    - [ ] CPU cache:
        - [ ] [MIT 6.004 L15: The Memory Hierarchy (video)](https://www.youtube.com/watch?v=vjYF_fAZI5E&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-&index=24)
        - [ ] [MIT 6.004 L16: Cache Issues (video)](https://www.youtube.com/watch?v=ajgC3-pyGlk&index=25&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-)

- ### Processes and Threads
    - [ ] Computer Science 162 - Operating Systems (25 videos):
        - for processes and threads see videos 1-11
        - [Operating Systems and System Programming (video)](https://archive.org/details/ucberkeley-webcast-PL-XXv-cvA_iBDyz-ba4yDskqMDY6A1w_c)
    - [What Is The Difference Between A Process And A Thread?](https://www.quora.com/What-is-the-difference-between-a-process-and-a-thread)
    - Covers:
        - Processes, Threads, Concurrency issues
            - Difference between processes and threads
            - Processes
            - Threads
            - Locks
            - Mutexes
            - Semaphores
            - Monitors
            - How do they work?
            - Deadlock
            - Livelock
        - CPU activity, interrupts, context switching
        - Modern concurrency constructs with multicore processors
        - [Paging, segmentation, and virtual memory (video)](https://youtu.be/O4nwUqQodAg)
        - [Interrupts (video)](https://youtu.be/iKlAWIKEyuw)
        - Process resource needs (memory: code, static storage, stack, heap, and also file descriptors, i/o)
        - Thread resource needs (shares above (minus stack) with other threads in the same process but each has its own PC, stack counter, registers, and stack)
        - Forking is really copy on write (read-only) until the new process writes to memory, then it does a full copy.
        - Context switching
            - [How context switching is initiated by the operating system and underlying hardware?](https://www.javatpoint.com/what-is-the-context-switching-in-the-operating-system)
    - [ ] [threads in C++ (series - 10 videos)](https://www.youtube.com/playlist?list=PL5jc9xFGsL8E12so1wlMS0r0hTQoJL74M)
    - [ ] [CS 377 Spring '14: Operating Systems from University of Massachusetts](https://www.youtube.com/playlist?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k)
    - [ ] concurrency in Python (videos):
        - [ ] [Short series on threads](https://www.youtube.com/playlist?list=PL1H1sBF1VAKVMONJWJkmUh6_p8g4F2oy1)
        - [ ] [Python Threads](https://www.youtube.com/watch?v=Bs7vPNbB9JM)
        - [ ] [Understanding the Python GIL (2010)](https://www.youtube.com/watch?v=Obt-vMVdM8s)
            - [reference](http://www.dabeaz.com/GIL)
        - [ ] [David Beazley - Python Concurrency From the Ground Up LIVE! - PyCon 2015](https://www.youtube.com/watch?v=MCs5OvhV9S4)
        - [ ] [Keynote David Beazley - Topics of Interest (Python Asyncio)](https://www.youtube.com/watch?v=ZzfHjytDceU)
        - [ ] [Mutex in Python](https://www.youtube.com/watch?v=0zaPs8OtyKY)

- ### Testing
    - To cover:
        - how unit testing works
        - what are mock objects
        - what is integration testing
        - what is dependency injection
    - [ ] [Agile Software Testing with James Bach (video)](https://www.youtube.com/watch?v=SAhJf36_u5U)
    - [ ] [Open Lecture by James Bach on Software Testing (video)](https://www.youtube.com/watch?v=ILkT_HV9DVU)
    - [ ] [Steve Freeman - Test-Driven Development (that’s not what we meant) (video)](https://vimeo.com/83960706)
        - [slides](http://gotocon.com/dl/goto-berlin-2013/slides/SteveFreeman_TestDrivenDevelopmentThatsNotWhatWeMeant.pdf)
    - [ ] Dependency injection:
        - [ ] [video](https://www.youtube.com/watch?v=IKD2-MAkXyQ)
        - [ ] [Tao Of Testing](http://jasonpolites.github.io/tao-of-testing/ch3-1.1.html)
    - [ ] [How to write tests](http://jasonpolites.github.io/tao-of-testing/ch4-1.1.html)

- ### String searching & manipulations
    - [ ] [Sedgewick - Suffix Arrays (video)](https://www.coursera.org/learn/algorithms-part2/lecture/TH18W/suffix-arrays)
    - [ ] [Sedgewick - Substring Search (videos)](https://www.coursera.org/learn/algorithms-part2/home/week/4)
        - [ ] [1. Introduction to Substring Search](https://www.coursera.org/lecture/algorithms-part2/introduction-to-substring-search-n3ZpG)
        - [ ] [2. Brute-Force Substring Search](https://www.coursera.org/learn/algorithms-part2/lecture/2Kn5i/brute-force-substring-search)
        - [ ] [3. Knuth-Morris Pratt](https://www.coursera.org/learn/algorithms-part2/lecture/TAtDr/knuth-morris-pratt)
        - [ ] [4. Boyer-Moore](https://www.coursera.org/learn/algorithms-part2/lecture/CYxOT/boyer-moore)
        - [ ] [5. Rabin-Karp](https://www.coursera.org/lecture/algorithms-part2/rabin-karp-3KiqT)
    - [ ] [Search pattern in a text (video)](https://www.coursera.org/learn/data-structures/lecture/tAfHI/search-pattern-in-text)

    If you need more detail on this subject, see the "String Matching" section in [Additional Detail on Some Subjects](#additional-detail-on-some-subjects).

- ### Tries
    - Note there are different kinds of tries. Some have prefixes, some don't, and some use strings instead of bits
        to track the path
    - I read through the code, but will not implement
    - [ ] [Sedgewick - Tries (3 videos)](https://www.coursera.org/learn/algorithms-part2/home/week/4)
        - [x] [1. R Way Tries](https://www.coursera.org/learn/algorithms-part2/lecture/CPVdr/r-way-tries)
        - [x] [2. Ternary Search Tries](https://www.coursera.org/learn/algorithms-part2/lecture/yQM8K/ternary-search-tries)
        - [x] [3. Character Based Operations](https://www.coursera.org/learn/algorithms-part2/lecture/jwNmV/character-based-operations)
    - [x] [Notes on Data Structures and Programming Techniques](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#Tries)
    - [x] Short course videos:
        - [x] [Introduction To Tries (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/08Xyf/core-introduction-to-tries)
        - [x] [Performance Of Tries (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/PvlZW/core-performance-of-tries)
        - [x] [Implementing A Trie (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/DFvd3/core-implementing-a-trie)
    - [x] [The Trie: A Neglected Data Structure](https://www.toptal.com/java/the-trie-a-neglected-data-structure)
    - [x] [TopCoder - Using Tries](https://www.topcoder.com/thrive/articles/Using%20Tries)
    - [x] [Stanford Lecture (real-world use case) (video)](https://www.youtube.com/watch?v=TJ8SkcUSdbU)
    - [x] [MIT, Advanced Data Structures, Strings (can get pretty obscure about halfway through) (video)](https://www.youtube.com/watch?v=NinWEPPrkDQ&index=16&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf)

- ### Floating Point Numbers
    - [ ] simple 8-bit: [Representation of Floating Point Numbers - 1 (video - there is an error in calculations - see video description)](https://www.youtube.com/watch?v=ji3SfClm8TU)

- ### Unicode
    - [ ] [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets]( http://www.joelonsoftware.com/articles/Unicode.html)
    - [ ] [What Every Programmer Absolutely, Positively Needs To Know About Encodings And Character Sets To Work With Text](http://kunststube.net/encoding/)

- ### Endianness
    - [ ] [Big And Little Endian](https://web.archive.org/web/20180107141940/http://www.cs.umd.edu:80/class/sum2003/cmsc311/Notes/Data/endian.html)
    - [ ] [Big Endian Vs Little Endian (video)](https://www.youtube.com/watch?v=JrNF0KRAlyo)
    - [ ] [Big And Little Endian Inside/Out (video)](https://www.youtube.com/watch?v=oBSuXP-1Tc0)
        - Very technical talk for kernel devs. Don't worry if most is over your head.
        - The first half is enough.

- ### Networking
    - **If you have networking experience or want to be a reliability engineer or operations engineer, expect questions**
    - Otherwise, this is just good to know
    - [ ] [Khan Academy](https://www.khanacademy.org/computing/code-org/computers-and-the-internet)
    - [ ] [UDP and TCP: Comparison of Transport Protocols (video)](https://www.youtube.com/watch?v=Vdc8TCESIg8)
    - [ ] [TCP/IP and the OSI Model Explained! (video)](https://www.youtube.com/watch?v=e5DEVa9eSN0)
    - [ ] [Packet Transmission across the Internet. Networking & TCP/IP tutorial. (video)](https://www.youtube.com/watch?v=nomyRJehhnM)
    - [ ] [HTTP (video)](https://www.youtube.com/watch?v=WGJrLqtX7As)
    - [ ] [SSL and HTTPS (video)](https://www.youtube.com/watch?v=S2iBR2ZlZf0)
    - [ ] [SSL/TLS (video)](https://www.youtube.com/watch?v=Rp3iZUvXWlM)
    - [ ] [HTTP 2.0 (video)](https://www.youtube.com/watch?v=E9FxNzv1Tr8)
    - [ ] [Video Series (21 videos) (video)](https://www.youtube.com/playlist?list=PLEbnTDJUr_IegfoqO4iPnPYQui46QqT0j)
    - [ ] [Subnetting Demystified - Part 5 CIDR Notation (video)](https://www.youtube.com/watch?v=t5xYI0jzOf4)
    - [ ] Sockets:
        - [ ] [Java - Sockets - Introduction (video)](https://www.youtube.com/watch?v=6G_W54zuadg&t=6s)
        - [ ] [Socket Programming (video)](https://www.youtube.com/watch?v=G75vN2mnJeQ)

---

## Final Review

    This section will have shorter videos that you can watch pretty quickly to review most of the important concepts.
    It's nice if you want a refresher often.

- [ ] Series of 2-3 minutes short subject videos (23 videos)
    - [Videos](https://www.youtube.com/watch?v=r4r1DZcx1cM&list=PLmVb1OknmNJuC5POdcDv5oCS7_OUkDgpj&index=22)
- [ ] Series of 2-5 minutes short subject videos - Michael Sambol (48 videos):
    - [Videos](https://www.youtube.com/@MichaelSambol)
    - [Code Examples](https://github.com/msambol/dsa)
- [ ] [Sedgewick Videos - Algorithms I](https://www.coursera.org/learn/algorithms-part1)
- [ ] [Sedgewick Videos - Algorithms II](https://www.coursera.org/learn/algorithms-part2)

---

## Update Your Resume

- See Resume prep information in the books: "Cracking The Coding Interview" and "Programming Interviews Exposed"
- ["This Is What A GOOD Resume Should Look Like" by Gayle McDowell (author of Cracking the Coding Interview)](https://www.careercup.com/resume),
    - Note by the author: "This is for a US-focused resume. CVs for India and other countries have different expectations, although many of the points will be the same."
- ["Step-by-step resume guide" by Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/guide)
    - Detailed guide on how to set up your resume from scratch, write effective resume content, optimize it, and test your resume

## Interview Process & General Interview Prep

- [ ] [How to Pass the Engineering Interview in 2021](https://davidbyttow.medium.com/how-to-pass-the-engineering-interview-in-2021-45f1b389a1)
- [x] [Demystifying Tech Recruiting](https://www.youtube.com/watch?v=N233T0epWTs)
- [ ] How to Get a Job at the Big 4:
    - [x] [How to Get a Job at the Big 4 - Amazon, Facebook, Google & Microsoft (video)](https://www.youtube.com/watch?v=YJZCUhxNCv8)
    - [x] [How to Get a Job at the Big 4.1 (Follow-up video)](https://www.youtube.com/watch?v=6790FVXWBw8&feature=youtu.be)
- [ ] Cracking The Coding Interview Set 1:
    - [x] [Gayle L McDowell - Cracking The Coding Interview (video)](https://www.youtube.com/watch?v=rEJzOhC5ZtQ)
    - [x] [Cracking the Coding Interview with Author Gayle Laakmann McDowell (video)](https://www.youtube.com/watch?v=aClxtDcdpsQ)
- [ ] Cracking the Facebook Coding Interview:
    - [ ] [The Approach](https://www.youtube.com/watch?v=wCl9kvQGHPI)
    - [ ] [Problem Walkthrough](https://www.youtube.com/watch?v=4UWDyJq8jZg)
- Prep Courses:
    - [Python for Data Structures, Algorithms, and Interviews (paid course)](https://www.udemy.com/python-for-data-structures-algorithms-and-interviews/):
        - A Python-centric interview prep course that covers data structures, algorithms, mock interviews, and much more.
    - [Intro to Data Structures and Algorithms using Python (Udacity free course)](https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513):
        - A free Python-centric data structures and algorithms course.
    - [Data Structures and Algorithms Nanodegree! (Udacity paid Nanodegree)](https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256):
        - Get hands-on practice with over 100 data structures and algorithm exercises and guidance from a dedicated mentor to help prepare you for interviews and on-the-job scenarios.
    - [Grokking the Behavioral Interview (Educative free course)](https://www.educative.io/courses/grokking-the-behavioral-interview):
        - Many times, it’s not your technical competency that holds you back from landing your dream job, it’s how you perform on the behavioral interview.
    - [AlgoMonster (paid course with free content)](https://algo.monster/?utm_campaign=jwasham&utm_medium=referral&utm_content=coding-interview-university&utm_source=github):
      - The crash course for LeetCode. Covers all the patterns condensed from thousands of questions.

Mock Interviews:
- [Gainlo.co: Mock interviewers from big companies](http://www.gainlo.co/#!/) - I used this and it helped me relax for the phone screen and on-site interview
- [Pramp: Mock interviews from/with peers](https://www.pramp.com/) - a peer-to-peer model to practice interviews
- [interviewing.io: Practice mock interview with senior engineers](https://interviewing.io) - anonymous algorithmic/systems design interviews with senior engineers from FAANG anonymously
- [Meetapro: Mock interviews with top FAANG interviewers](https://meetapro.com/?utm_source=ciu) - an Airbnb-style mock interview/coaching platform.
- [Hello Interview: Mock Interviews with Expert Coaches and AI](https://www.hellointerview.com/?utm_source=ciu) - interview directly with AI or with FAANG staff engineers and managers.
- [Codemia: Practice system design problems with AI or community solutions and feedback](https://codemia.io/?utm_source=ciu) - Practice system design problems via AI practice tool. Share your solution with the community to get human feedback as well.

## Be thinking of for when the interview comes

Think of about 20 interview questions you'll get, along with the lines of the items below. Have at least one answer for each.
Have a story, not just data, about something you accomplished.

- Why do you want this job?
- What's a tough problem you've solved?
- Biggest challenges faced?
- Best/worst designs seen?
- Ideas for improving an existing product
- How do you work best, as an individual and as part of a team?
- Which of your skills or experiences would be assets in the role and why?
- What did you most enjoy at [job x / project y]?
- What was the biggest challenge you faced at [job x / project y]?
- What was the hardest bug you faced at [job x / project y]?
- What did you learn at [job x / project y]?
- What would you have done better at [job x / project y]?

## Have questions for the interviewer

Some of mine (I already may know the answers, but want their opinion or team perspective):

- How large is your team?
- What does your dev cycle look like? Do you do waterfall/sprints/agile?
- Are rushes to deadlines common? Or is there flexibility?
- How are decisions made in your team?
- How many meetings do you have per week?
- Do you feel your work environment helps you concentrate?
- What are you working on?
- What do you like about it?
- What is the work life like?
- How is the work/life balance?

## Once You've Got The Job

Congratulations!

Keep learning.

You're never really done.

---

    *****************************************************************************************************
    *****************************************************************************************************

    Everything below this point is optional. It is NOT needed for an entry-level interview.
    However, by studying these, you'll get greater exposure to more CS concepts and will be better prepared for
    any software engineering job. You'll be a much more well-rounded software engineer.

    *****************************************************************************************************
    *****************************************************************************************************

---

## Additional Books

    These are here so you can dive into a topic you find interesting.

- [The Unix Programming Environment](https://www.amazon.com/dp/013937681X)
    - An oldie but a goodie
- [The Linux Command Line: A Complete Introduction](https://www.amazon.com/dp/1593273894/)
    - A modern option
- [TCP/IP Illustrated Series](https://en.wikipedia.org/wiki/TCP/IP_Illustrated)
- [Head First Design Patterns](https://www.amazon.com/gp/product/0596007124/)
    - A gentle introduction to design patterns
- [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)
    - AKA the "Gang Of Four" book or GOF
    - The canonical design patterns book
- [Algorithm Design Manual](http://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/1849967202) (Skiena)
    - As a review and problem-recognition
    - The algorithm catalog portion is well beyond the scope of difficulty you'll get in an interview
    - This book has 2 parts:
        - Class textbook on data structures and algorithms
            - Pros:
                - Is a good review as any algorithms textbook would be
                - Nice stories from his experiences solving problems in industry and academia
                - Code examples in C
            - Cons:
                - Can be as dense or impenetrable as CLRS, and in some cases, CLRS may be a better alternative for some subjects
                - Chapters 7, 8, and 9 can be painful to try to follow, as some items are not explained well or require more brain than I have
                - Don't get me wrong: I like Skiena, his teaching style, and mannerisms, but I may not be Stony Brook material
        - Algorithm catalog:
            - This is the real reason you buy this book.
            - This book is better as an algorithm reference, and not something you read cover to cover.
    - Can rent it on Kindle
    - Answers:
        - [Solutions](https://web.archive.org/web/20150404194210/http://www.algorithm.cs.sunysb.edu/algowiki/index.php/The_Algorithms_Design_Manual_(Second_Edition))
    - [Errata](http://www3.cs.stonybrook.edu/~skiena/algorist/book/errata)
- [Algorithm](http://jeffe.cs.illinois.edu/teaching/algorithms/) (Jeff Erickson)
- [Write Great Code: Volume 1: Understanding the Machine](https://www.amazon.com/Write-Great-Code-Understanding-Machine/dp/1593270038)
    - The book was published in 2004, and is somewhat outdated, but it's a terrific resource for understanding a computer in brief
    - The author invented [HLA](https://en.wikipedia.org/wiki/High_Level_Assembly), so take mentions and examples in HLA with a grain of salt. Not widely used, but decent examples of what assembly looks like
    - These chapters are worth the read to give you a nice foundation:
        - Chapter 2 - Numeric Representation
        - Chapter 3 - Binary Arithmetic and Bit Operations
        - Chapter 4 - Floating-Point Representation
        - Chapter 5 - Character Representation
        - Chapter 6 - Memory Organization and Access
        - Chapter 7 - Composite Data Types and Memory Objects
        - Chapter 9 - CPU Architecture
        - Chapter 10 - Instruction Set Architecture
        - Chapter 11 - Memory Architecture and Organization
- [Introduction to Algorithms](https://www.amazon.com/Introduction-Algorithms-fourth-Thomas-Cormen/dp/026204630X)
    - **Important:** Reading this book will only have limited value. This book is a great review of algorithms and data structures, but won't teach you how to write good code. You have to be able to code a decent solution efficiently
    - AKA CLR, sometimes CLRS, because Stein was late to the game
- [Computer Architecture, Sixth Edition: A Quantitative Approach](https://www.amazon.com/dp/0128119055)
    - For a richer, more up-to-date (2017), but longer treatment

## System Design, Scalability, Data Handling

**You can expect system design questions if you have 4+ years of experience.**

- Scalability and System Design are very large topics with many topics and resources, since
      there is a lot to consider when designing a software/hardware system that can scale.
      Expect to spend quite a bit of time on this
- Considerations:
    - Scalability
        - Distill large data sets to single values
        - Transform one data set to another
        - Handling obscenely large amounts of data
    - System design
        - features sets
        - interfaces
        - class hierarchies
        - designing a system under certain constraints
        - simplicity and robustness
        - tradeoffs
        - performance analysis and optimization
- [ ] **START HERE**: [The System Design Primer](https://github.com/donnemartin/system-design-primer)
- [ ] [System Design from HiredInTech](http://www.hiredintech.com/system-design/)
- [ ] [How Do I Prepare To Answer Design Questions In A Technical Interview?](https://www.quora.com/How-do-I-prepare-to-answer-design-questions-in-a-technical-interview?redirected_qid=1500023)
- [ ] [8 steps guide to ace your system design interview](https://javascript.plainenglish.io/8-steps-guide-to-ace-a-system-design-interview-7a5a797f4d7d)
- [ ] [Database Normalization - 1NF, 2NF, 3NF and 4NF (video)](https://www.youtube.com/watch?v=UrYLYV7WSHM)
- [ ] [System Design Interview](https://github.com/checkcheckzz/system-design-interview) - There are a lot of resources in this one. Look through the articles and examples. I put some of them below
- [ ] [How to ace a systems design interview](https://web.archive.org/web/20120716060051/http://www.palantir.com/2011/10/how-to-rock-a-systems-design-interview/)
- [ ] [Numbers Everyone Should Know](http://everythingisdata.wordpress.com/2009/10/17/numbers-everyone-should-know/)
- [ ] [How long does it take to make a context switch?](http://blog.tsunanet.net/2010/11/how-long-does-it-take-to-make-context.html)
- [ ] [Transactions Across Datacenters (video)](https://www.youtube.com/watch?v=srOgpXECblk)
- [ ] [A plain English introduction to CAP Theorem](http://ksat.me/a-plain-english-introduction-to-cap-theorem)
- [ ] [MIT 6.824: Distributed Systems, Spring 2020 (20 videos)](https://www.youtube.com/watch?v=cQP8WApzIQQ&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB)
- [ ] Consensus Algorithms:
    - [ ] Paxos - [Paxos Agreement - Computerphile (video)](https://www.youtube.com/watch?v=s8JqcZtvnsM)
    - [ ] Raft - [An Introduction to the Raft Distributed Consensus Algorithm (video)](https://www.youtube.com/watch?v=P9Ydif5_qvE)
        - [ ] [Easy-to-read paper](https://raft.github.io/)
        - [ ] [Infographic](http://thesecretlivesofdata.com/raft/)
- [ ] [Consistent Hashing](http://www.tom-e-white.com/2007/11/consistent-hashing.html)
- [ ] [NoSQL Patterns](http://horicky.blogspot.com/2009/11/nosql-patterns.html)
- [ ] Scalability:
    - You don't need all of these. Just pick a few that interest you.
    - [ ] [Great overview (video)](https://www.youtube.com/watch?v=-W9F__D3oY4)
    - [ ] Short series:
        - [Clones](http://www.lecloud.net/post/7295452622/scalability-for-dummies-part-1-clones)
        - [Database](http://www.lecloud.net/post/7994751381/scalability-for-dummies-part-2-database)
        - [Cache](http://www.lecloud.net/post/9246290032/scalability-for-dummies-part-3-cache)
        - [Asynchronism](http://www.lecloud.net/post/9699762917/scalability-for-dummies-part-4-asynchronism)
    - [ ] [Scalable Web Architecture and Distributed Systems](http://www.aosabook.org/en/distsys.html)
    - [ ] [Fallacies of Distributed Computing Explained](https://pages.cs.wisc.edu/~zuyu/files/fallacies.pdf)
    - [ ] [Jeff Dean - Building Software Systems At Google and Lessons Learned (video)](https://www.youtube.com/watch?v=modXC5IWTJI)
    - [ ] [Introduction to Architecting Systems for Scale](http://lethain.com/introduction-to-architecting-systems-for-scale/)
    - [ ] [Scaling mobile games to a global audience using App Engine and Cloud Datastore (video)](https://www.youtube.com/watch?v=9nWyWwY2Onc)
    - [ ] [How Google Does Planet-Scale Engineering for Planet-Scale Infra (video)](https://www.youtube.com/watch?v=H4vMcD7zKM0)
    - [ ] [The Importance of Algorithms](https://www.topcoder.com/thrive/articles/The%20Importance%20of%20Algorithms)
    - [ ] [Sharding](http://highscalability.com/blog/2009/8/6/an-unorthodox-approach-to-database-design-the-coming-of-the.html)
    - [ ] [Engineering for the Long Game - Astrid Atkinson Keynote(video)](https://www.youtube.com/watch?v=p0jGmgIrf_M&list=PLRXxvay_m8gqVlExPC5DG3TGWJTaBgqSA&index=4)
    - [ ] [7 Years Of YouTube Scalability Lessons In 30 Minutes](http://highscalability.com/blog/2012/3/26/7-years-of-youtube-scalability-lessons-in-30-minutes.html)
        - [video](https://www.youtube.com/watch?v=G-lGCC4KKok)
    - [ ] [How PayPal Scaled To Billions Of Transactions Daily Using Just 8VMs](http://highscalability.com/blog/2016/8/15/how-paypal-scaled-to-billions-of-transactions-daily-using-ju.html)
    - [ ] [How to Remove Duplicates in Large Datasets](https://blog.clevertap.com/how-to-remove-duplicates-in-large-datasets/)
    - [ ] [A look inside Etsy's scale and engineering culture with Jon Cowie (video)](https://www.youtube.com/watch?v=3vV4YiqKm1o)
    - [ ] [What Led Amazon to its Own Microservices Architecture](http://thenewstack.io/led-amazon-microservices-architecture/)
    - [ ] [To Compress Or Not To Compress, That Was Uber's Question](https://eng.uber.com/trip-data-squeeze/)
    - [ ] [When Should Approximate Query Processing Be Used?](http://highscalability.com/blog/2016/2/25/when-should-approximate-query-processing-be-used.html)
    - [ ] [Google's Transition From Single Datacenter To Failover, To A Native Multihomed Architecture]( http://highscalability.com/blog/2016/2/23/googles-transition-from-single-datacenter-to-failover-to-a-n.html)
    - [ ] [The Image Optimization Technology That Serves Millions Of Requests Per Day](http://highscalability.com/blog/2016/6/15/the-image-optimization-technology-that-serves-millions-of-re.html)
    - [ ] [A Patreon Architecture Short](http://highscalability.com/blog/2016/2/1/a-patreon-architecture-short.html)
    - [ ] [Tinder: How Does One Of The Largest Recommendation Engines Decide Who You'll See Next?](http://highscalability.com/blog/2016/1/27/tinder-how-does-one-of-the-largest-recommendation-engines-de.html)
    - [ ] [Design Of A Modern Cache](http://highscalability.com/blog/2016/1/25/design-of-a-modern-cache.html)
    - [ ] [Live Video Streaming At Facebook Scale](http://highscalability.com/blog/2016/1/13/live-video-streaming-at-facebook-scale.html)
    - [ ] [A Beginner's Guide To Scaling To 11 Million+ Users On Amazon's AWS](http://highscalability.com/blog/2016/1/11/a-beginners-guide-to-scaling-to-11-million-users-on-amazons.html)
    - [ ] [A 360 Degree View Of The Entire Netflix Stack](http://highscalability.com/blog/2015/11/9/a-360-degree-view-of-the-entire-netflix-stack.html)
    - [ ] [Latency Is Everywhere And It Costs You Sales - How To Crush It](http://highscalability.com/latency-everywhere-and-it-costs-you-sales-how-crush-it)
    - [ ] [What Powers Instagram: Hundreds of Instances, Dozens of Technologies](http://instagram-engineering.tumblr.com/post/13649370142/what-powers-instagram-hundreds-of-instances)
    - [ ] [Salesforce Architecture - How They Handle 1.3 Billion Transactions A Day](http://highscalability.com/blog/2013/9/23/salesforce-architecture-how-they-handle-13-billion-transacti.html)
    - [ ] [ESPN's Architecture At Scale - Operating At 100,000 Duh Nuh Nuhs Per Second](http://highscalability.com/blog/2013/11/4/espns-architecture-at-scale-operating-at-100000-duh-nuh-nuhs.html)
    - [ ] See "Messaging, Serialization, and Queueing Systems" way below for info on some of the technologies that can glue services together
    - [ ] Twitter:
        - [O'Reilly MySQL CE 2011: Jeremy Cole, "Big and Small Data at @Twitter" (video)](https://www.youtube.com/watch?v=5cKTP36HVgI)
        - [Timelines at Scale](https://www.infoq.com/presentations/Twitter-Timeline-Scalability)
    - For even more, see the "Mining Massive Datasets" video series in the [Video Series](#video-series) section
- [ ] Practicing the system design process: Here are some ideas to try working through on paper, each with some documentation on how it was handled in the real world:
    - review: [The System Design Primer](https://github.com/donnemartin/system-design-primer)
    - [System Design from HiredInTech](http://www.hiredintech.com/system-design/)
    - [cheat sheet](https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/system-design.pdf)
    - flow:
        1. Understand the problem and scope:
            - Define the use cases, with the interviewer's help
            - Suggest additional features
            - Remove items that the interviewer deems out of scope
            - Assume high availability is required, add as a use case
        2. Think about constraints:
            - Ask how many requests per month
            - Ask how many requests per second (they may volunteer it or make you do the math)
            - Estimate reads vs. writes percentage
            - Keep the 80/20 rule in mind when estimating
            - How much data is written per second
            - Total storage required over 5 years
            - How much data read per second
        3. Abstract design:
            - Layers (service, data, caching)
            - Infrastructure: load balancing, messaging
            - Rough overview of any key algorithm that drives the service
            - Consider bottlenecks and determine solutions
    - Exercises:
        - [Design a random unique ID generation system](https://blog.twitter.com/2010/announcing-snowflake)
        - [Design a key-value database](http://www.slideshare.net/dvirsky/introduction-to-redis)
        - [Design a picture sharing system](http://highscalability.com/blog/2011/12/6/instagram-architecture-14-million-users-terabytes-of-photos.html)
        - [Design a recommendation system](http://ijcai13.org/files/tutorial_slides/td3.pdf)
        - [Design a URL-shortener system: copied from above](http://www.hiredintech.com/system-design/the-system-design-process/)
        - [Design a cache system](https://web.archive.org/web/20220217064329/https://adayinthelifeof.nl/2011/02/06/memcache-internals/)

## Additional Learning

    I added them to help you become a well-rounded software engineer and to be aware of certain
    technologies and algorithms, so you'll have a bigger toolbox.

- ### Compilers
    - [How a Compiler Works in ~1 minute (video)](https://www.youtube.com/watch?v=IhC7sdYe-Jg)
    - [Harvard CS50 - Compilers (video)](https://www.youtube.com/watch?v=CSZLNYF4Klo)
    - [C++ (video)](https://www.youtube.com/watch?v=twodd1KFfGk)
    - [Understanding Compiler Optimization (C++) (video)](https://www.youtube.com/watch?v=FnGCDLhaxKU)

- ### Emacs and vi(m)
    - Familiarize yourself with a UNIX-based code editor
    - vi(m):
        - [Editing With Vim 01 - Installation, Setup, and The Modes (video)](https://www.youtube.com/watch?v=5givLEMcINQ&index=1&list=PL13bz4SHGmRxlZVmWQ9DvXo1fEg4UdGkr)
        - [VIM Adventures](http://vim-adventures.com/)
        - set of 4 videos:
            - [The vi/vim editor - Lesson 1](https://www.youtube.com/watch?v=SI8TeVMX8pk)
            - [The vi/vim editor - Lesson 2](https://www.youtube.com/watch?v=F3OO7ZIOaJE)
            - [The vi/vim editor - Lesson 3](https://www.youtube.com/watch?v=ZYEccA_nMaI)
            - [The vi/vim editor - Lesson 4](https://www.youtube.com/watch?v=1lYD5gwgZIA)
        - [Using Vi Instead of Emacs](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#Using_Vi_instead_of_Emacs)
    - emacs:
        - [Basics Emacs Tutorial (video)](https://www.youtube.com/watch?v=hbmV1bnQ-i0)
        - set of 3 (videos):
            - [Emacs Tutorial (Beginners) -Part 1- File commands, cut/copy/paste, cursor commands](https://www.youtube.com/watch?v=ujODL7MD04Q)
            - [Emacs Tutorial (Beginners) -Part 2- Buffer management, search, M-x grep and rgrep modes](https://www.youtube.com/watch?v=XWpsRupJ4II)
            - [Emacs Tutorial (Beginners) -Part 3- Expressions, Statements, ~/.emacs file, and packages](https://www.youtube.com/watch?v=paSgzPso-yc)
        - [Evil Mode: Or, How I Learned to Stop Worrying and Love Emacs (video)](https://www.youtube.com/watch?v=JWD1Fpdd4Pc)
        - [Writing C Programs With Emacs](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#Writing_C_programs_with_Emacs)
	- [The Absolute Beginner's Guide to Emacs (video by David Wilson)](https://www.youtube.com/watch?v=48JlgiBpw_I&t=0s)
	- [The Absolute Beginner's Guide to Emacs (notes by David Wilson)](https://systemcrafters.net/emacs-essentials/absolute-beginners-guide-to-emacs/)

- ### Unix command line tools
    - I filled in the list below from good tools.
    - bash
    - cat
    - grep
    - sed
    - awk
    - curl or wget
    - sort
    - tr
    - uniq
    - [strace](https://en.wikipedia.org/wiki/Strace)
    - [tcpdump](https://danielmiessler.com/study/tcpdump/)

- ### Information theory (videos)
    - [Khan Academy](https://www.khanacademy.org/computing/computer-science/informationtheory)
    - More about Markov processes:
        - [Core Markov Text Generation](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/waxgx/core-markov-text-generation)
        - [Core Implementing Markov Text Generation](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/gZhiC/core-implementing-markov-text-generation)
        - [Project = Markov Text Generation Walk Through](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/EUjrq/project-markov-text-generation-walk-through)
    - See more in the MIT 6.050J Information and Entropy series below

- ### Parity & Hamming Code (videos)
    - [Intro](https://www.youtube.com/watch?v=q-3BctoUpHE)
    - [Parity](https://www.youtube.com/watch?v=DdMcAUlxh1M)
    - Hamming Code:
        - [Error detection](https://www.youtube.com/watch?v=1A_NcXxdoCc)
        - [Error correction](https://www.youtube.com/watch?v=JAMLuxdHH8o)
    - [Error Checking](https://www.youtube.com/watch?v=wbH2VxzmoZk)

- ### Entropy
    - Also see the videos below
    - Make sure to watch information theory videos first
    - [Information Theory, Claude Shannon, Entropy, Redundancy, Data Compression & Bits (video)](https://youtu.be/JnJq3Py0dyM?t=176)

- ### Cryptography
    - Also see the videos below
    - Make sure to watch information theory videos first
    - [Khan Academy Series](https://www.khanacademy.org/computing/computer-science/cryptography)
    - [Cryptography: Hash Functions](https://www.youtube.com/watch?v=KqqOXndnvic&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=30)
    - [Cryptography: Encryption](https://www.youtube.com/watch?v=9TNI2wHmaeI&index=31&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)

- ### Compression
    - Make sure to watch information theory videos first
    - Computerphile (videos):
        - [Compression](https://www.youtube.com/watch?v=Lto-ajuqW3w)
        - [Entropy in Compression](https://www.youtube.com/watch?v=M5c_RFKVkko)
        - [Upside Down Trees (Huffman Trees)](https://www.youtube.com/watch?v=umTbivyJoiI)
        - [EXTRA BITS/TRITS - Huffman Trees](https://www.youtube.com/watch?v=DV8efuB3h2g)
        - [Elegant Compression in Text (The LZ 77 Method)](https://www.youtube.com/watch?v=goOa3DGezUA)
        - [Text Compression Meets Probabilities](https://www.youtube.com/watch?v=cCDCfoHTsaU)
    - [Compressor Head videos](https://www.youtube.com/playlist?list=PLOU2XLYxmsIJGErt5rrCqaSGTMyyqNt2H)
    - [(optional) Google Developers Live: GZIP is not enough!](https://www.youtube.com/watch?v=whGwm0Lky2s)

- ### Computer Security
    - [MIT (23 videos)](https://www.youtube.com/playlist?list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [Introduction, Threat Models](https://www.youtube.com/watch?v=GqmQg-cszw4&index=1&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [Control Hijacking Attacks](https://www.youtube.com/watch?v=6bwzNg5qQ0o&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh&index=2)
        - [Buffer Overflow Exploits and Defenses](https://www.youtube.com/watch?v=drQyrzRoRiA&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh&index=3)
        - [Privilege Separation](https://www.youtube.com/watch?v=6SIJmoE9L9g&index=4&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [Capabilities](https://www.youtube.com/watch?v=8VqTSY-11F4&index=5&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [Sandboxing Native Code](https://www.youtube.com/watch?v=VEV74hwASeU&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh&index=6)
        - [Web Security Model](https://www.youtube.com/watch?v=chkFBigodIw&index=7&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [Securing Web Applications](https://www.youtube.com/watch?v=EBQIGy1ROLY&index=8&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [Symbolic Execution](https://www.youtube.com/watch?v=yRVZPvHYHzw&index=9&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [Network Security](https://www.youtube.com/watch?v=SIEVvk3NVuk&index=11&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [Network Protocols](https://www.youtube.com/watch?v=QOtA76ga_fY&index=12&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [Side-Channel Attacks](https://www.youtube.com/watch?v=PuVMkSEcPiI&index=15&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)

- ### Garbage collection
    - [GC in Python (video)](https://www.youtube.com/watch?v=iHVs_HkjdmI)
    - [Deep Dive Java: Garbage Collection is Good!](https://www.infoq.com/presentations/garbage-collection-benefits)
    - [Deep Dive Python: Garbage Collection in CPython (video)](https://www.youtube.com/watch?v=P-8Z0-MhdQs&list=PLdzf4Clw0VbOEWOS_sLhT_9zaiQDrS5AR&index=3)

- ### Parallel Programming
    - [Coursera (Scala)](https://www.coursera.org/learn/parprog1/home/week/1)
    - [Efficient Python for High-Performance Parallel Computing (video)](https://www.youtube.com/watch?v=uY85GkaYzBk)

- ### Messaging, Serialization, and Queueing Systems
    - [Thrift](https://thrift.apache.org/)
        - [Tutorial](http://thrift-tutorial.readthedocs.io/en/latest/intro.html)
    - [Protocol Buffers](https://developers.google.com/protocol-buffers/)
        - [Tutorials](https://developers.google.com/protocol-buffers/docs/tutorials)
    - [gRPC](http://www.grpc.io/)
        - [gRPC 101 for Java Developers (video)](https://www.youtube.com/watch?v=5tmPvSe7xXQ&list=PLcTqM9n_dieN0k1nSeN36Z_ppKnvMJoly&index=1)
    - [Redis](http://redis.io/)
        - [Tutorial](http://try.redis.io/)
    - [Amazon SQS (queue)](https://aws.amazon.com/sqs/)
    - [Amazon SNS (pub-sub)](https://aws.amazon.com/sns/)
    - [RabbitMQ](https://www.rabbitmq.com/)
        - [Get Started](https://www.rabbitmq.com/getstarted.html)
    - [Celery](http://www.celeryproject.org/)
        - [First Steps With Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)
    - [ZeroMQ](http://zeromq.org/)
        - [Intro - Read The Manual](http://zeromq.org/intro:read-the-manual)
    - [ActiveMQ](http://activemq.apache.org/)
    - [Kafka](http://kafka.apache.org/documentation.html#introduction)
    - [MessagePack](http://msgpack.org/index.html)
    - [Avro](https://avro.apache.org/)

- ### A*
    - [A Search Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
    - [A* Pathfinding (E01: algorithm explanation) (video)](https://www.youtube.com/watch?v=-L-WgKMFuhE)

- ### Fast Fourier Transform
    - [An Interactive Guide To The Fourier Transform](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/)
    - [What is a Fourier transform? What is it used for?](http://www.askamathematician.com/2012/09/q-what-is-a-fourier-transform-what-is-it-used-for/)
    - [What is the Fourier Transform? (video)](https://www.youtube.com/watch?v=Xxut2PN-V8Q)
    - [Divide & Conquer: FFT (video)](https://www.youtube.com/watch?v=iTMn0Kt18tg&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=4)
    - [Understanding The FFT](http://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/)

- ### Bloom Filter
    - Given a Bloom filter with m bits and k hashing functions, both insertion and membership testing are O(k)
    - [Bloom Filters (video)](https://www.youtube.com/watch?v=-SuTGoFYjZs)
    - [Bloom Filters | Mining of Massive Datasets | Stanford University (video)](https://www.youtube.com/watch?v=qBTdukbzc78)
    - [Tutorial](http://billmill.org/bloomfilter-tutorial/)
    - [How To Write A Bloom Filter App](http://blog.michaelschmatz.com/2016/04/11/how-to-write-a-bloom-filter-cpp/)

- ### HyperLogLog
    - [How To Count A Billion Distinct Objects Using Only 1.5KB Of Memory](http://highscalability.com/blog/2012/4/5/big-data-counting-how-to-count-a-billion-distinct-objects-us.html)

- ### Locality-Sensitive Hashing
    - Used to determine the similarity of documents
    - The opposite of MD5 or SHA which are used to determine if 2 documents/strings are exactly the same
    - [Simhashing (hopefully) made simple](http://ferd.ca/simhashing-hopefully-made-simple.html)

- ### van Emde Boas Trees
    - [Divide & Conquer: van Emde Boas Trees (video)](https://www.youtube.com/watch?v=hmReJCupbNU&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=6)
    - [MIT Lecture Notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec15.pdf)

- ### Augmented Data Structures
    - [CS 61B Lecture 39: Augmenting Data Structures](https://archive.org/details/ucberkeley_webcast_zksIj9O8_jc)

- ### Balanced search trees
    - Know at least one type of balanced binary tree (and know how it's implemented):
    - "Among balanced search trees, AVL and 2/3 trees are now passé and red-black trees seem to be more popular.
        A particularly interesting self-organizing data structure is the splay tree, which uses rotations
        to move any accessed key to the root." - Skiena
    - Of these, I chose to implement a splay tree. From what I've read, you won't implement a
        balanced search tree in your interview. But I wanted exposure to coding one up
        and let's face it, splay trees are the bee's knees. I did read a lot of red-black tree code
        - Splay tree: insert, search, delete functions
        If you end up implementing a red/black tree try just these:
        - Search and insertion functions, skipping delete
    - I want to learn more about B-Tree since it's used so widely with very large data sets
    - [Self-balancing binary search tree](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree)

    - **AVL trees**
        - In practice:
            From what I can tell, these aren't used much in practice, but I could see where they would be:
            The AVL tree is another structure supporting O(log n) search, insertion, and removal. It is more rigidly
            balanced than red–black trees, leading to slower insertion and removal but faster retrieval. This makes it
            attractive for data structures that may be built once and loaded without reconstruction, such as language
            dictionaries (or program dictionaries, such as the opcodes of an assembler or interpreter)
        - [MIT AVL Trees / AVL Sort (video)](https://www.youtube.com/watch?v=FNeL18KsWPc&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=6)
        - [AVL Trees (video)](https://www.coursera.org/learn/data-structures/lecture/Qq5E0/avl-trees)
        - [AVL Tree Implementation (video)](https://www.coursera.org/learn/data-structures/lecture/PKEBC/avl-tree-implementation)
        - [Split And Merge](https://www.coursera.org/learn/data-structures/lecture/22BgE/split-and-merge)
        - [[Review] AVL Trees (playlist) in 19 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZOUFgdIeOPuH6cfSnNRMau-)

    - **Splay trees**
        - In practice:
            Splay trees are typically used in the implementation of caches, memory allocators, routers, garbage collectors,
            data compression, ropes (replacement of string used for long text strings), in Windows NT (in the virtual memory,
            networking and file system code) etc
        - [CS 61B: Splay Trees (video)](https://archive.org/details/ucberkeley_webcast_G5QIXywcJlY)
        - MIT Lecture: Splay Trees:
            - Gets very mathy, but watch the last 10 minutes for sure.
            - [Video](https://www.youtube.com/watch?v=QnPl_Y6EqMo)

    - **Red/black trees**
        - These are a translation of a 2-3 tree (see below).
        - In practice:
            Red–black trees offer worst-case guarantees for insertion time, deletion time, and search time.
            Not only does this make them valuable in time-sensitive applications such as real-time applications,
            but it makes them valuable building blocks in other data structures that provide worst-case guarantees;
            for example, many data structures used in computational geometry can be based on red-black trees, and
            the Completely Fair Scheduler used in current Linux kernels uses red–black trees. In version 8 of Java,
            the Collection HashMap has been modified such that instead of using a LinkedList to store identical elements with poor
            hashcodes, a Red-Black tree is used
        - [Aduni - Algorithms - Lecture 4 (link jumps to the starting point) (video)](https://youtu.be/1W3x0f_RmUo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3871)
        - [Aduni - Algorithms - Lecture 5 (video)](https://www.youtube.com/watch?v=hm2GHwyKF1o&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=5)
        - [Red-Black Tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
        - [An Introduction To Binary Search And Red Black Tree](https://www.topcoder.com/thrive/articles/An%20Introduction%20to%20Binary%20Search%20and%20Red-Black%20Trees)
        - [[Review] Red-Black Trees (playlist) in 30 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZNqDI8qfOZgzbqahCUmUEin)

    - **2-3 search trees**
        - In practice:
            2-3 trees have faster inserts at the expense of slower searches (since height is more compared to AVL trees).
        - You would use 2-3 trees very rarely because its implementation involves different types of nodes. Instead, people use Red-Black trees.
        - [23-Tree Intuition and Definition (video)](https://www.youtube.com/watch?v=C3SsdUqasD4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=2)
        - [Binary View of 23-Tree](https://www.youtube.com/watch?v=iYvBtGKsqSg&index=3&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [2-3 Trees (student recitation) (video)](https://www.youtube.com/watch?v=TOb1tuEZ2X4&index=5&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)

    - **2-3-4 Trees (aka 2-4 trees)**
        - In practice:
            For every 2-4 trees, there are corresponding red–black trees with data elements in the same order. The insertion and deletion
            operations on 2-4 trees are also equivalent to color-flipping and rotations in red–black trees. This makes 2-4 trees an
            important tool for understanding the logic behind red-black trees, and this is why many introductory algorithm texts introduce
            2-4 trees just before red–black trees, even though **2-4 trees are not often used in practice**.
        - [CS 61B Lecture 26: Balanced Search Trees (video)](https://archive.org/details/ucberkeley_webcast_zqrqYXkth6Q)
        - [Bottom Up 234-Trees (video)](https://www.youtube.com/watch?v=DQdMYevEyE4&index=4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [Top Down 234-Trees (video)](https://www.youtube.com/watch?v=2679VQ26Fp4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=5)

    - **N-ary (K-ary, M-ary) trees**
        - note: the N or K is the branching factor (max branches)
        - binary trees are a 2-ary tree, with branching factor = 2
        - 2-3 trees are 3-ary
        - [K-Ary Tree](https://en.wikipedia.org/wiki/K-ary_tree)

    - **B-Trees**
        - Fun fact: it's a mystery, but the B could stand for Boeing, Balanced, or Bayer (co-inventor).
        - In Practice:
            B-trees are widely used in databases. Most modern filesystems use B-trees (or Variants). In addition to
            its use in databases, the B-tree is also used in filesystems to allow quick random access to an arbitrary
            block in a particular file. The basic problem is turning the file block address into a disk block
            (or perhaps to a cylinder head sector) address
        - [B-Tree](https://en.wikipedia.org/wiki/B-tree)
        - [B-Tree Datastructure](http://btechsmartclass.com/data_structures/b-trees.html)
        - [Introduction to B-Trees (video)](https://www.youtube.com/watch?v=I22wEC1tTGo&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=6)
        - [B-Tree Definition and Insertion (video)](https://www.youtube.com/watch?v=s3bCdZGrgpA&index=7&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [B-Tree Deletion (video)](https://www.youtube.com/watch?v=svfnVhJOfMc&index=8&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [MIT 6.851 - Memory Hierarchy Models (video)](https://www.youtube.com/watch?v=V3omVLzI0WE&index=7&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf)
                - covers cache-oblivious B-Trees, very interesting data structures
                - the first 37 minutes are very technical, and may be skipped (B is block size, cache line size)
        - [[Review] B-Trees (playlist) in 26 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZNFPPv98DjTdD9X6UI9KMHz)


- ### k-D Trees
    - Great for finding a number of points in a rectangle or higher-dimensional object
    - A good fit for k-nearest neighbors
    - [kNN K-d tree algorithm (video)](https://www.youtube.com/watch?v=Y4ZgLlDfKDg)

- ### Skip lists
    - "These are somewhat of a cult data structure" - Skiena
    - [Randomization: Skip Lists (video)](https://www.youtube.com/watch?v=2g9OSRKJuzM&index=10&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
    - [For animations and a little more detail](https://en.wikipedia.org/wiki/Skip_list)

- ### Network Flows
    - [Ford-Fulkerson in 5 minutes — Step by step example (video)](https://www.youtube.com/watch?v=Tl90tNtKvxs)
    - [Ford-Fulkerson Algorithm (video)](https://www.youtube.com/watch?v=v1VgJmkEJW0)
    - [Network Flows (video)](https://www.youtube.com/watch?v=2vhN4Ice5jI)

- ### Disjoint Sets & Union Find
    - [UCB 61B - Disjoint Sets; Sorting & selection (video)](https://archive.org/details/ucberkeley_webcast_MAEGXTwmUsI)
    - [Sedgewick Algorithms - Union-Find (6 videos)](https://www.coursera.org/learn/algorithms-part1/home/week/1)

- ### Math for Fast Processing
    - [Integer Arithmetic, Karatsuba Multiplication (video)](https://www.youtube.com/watch?v=eCaXlAaN2uE&index=11&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [The Chinese Remainder Theorem (used in cryptography) (video)](https://www.youtube.com/watch?v=ru7mWZJlRQg)

- ### Treap
    - Combination of a binary search tree and a heap
    - [Treap](https://en.wikipedia.org/wiki/Treap)
    - [Data Structures: Treaps explained (video)](https://www.youtube.com/watch?v=6podLUYinH8)
    - [Applications in set operations](https://www.cs.cmu.edu/~scandal/papers/treaps-spaa98.pdf)

- ### Linear Programming (videos)
    - [Linear Programming](https://www.youtube.com/watch?v=M4K6HYLHREQ)
    - [Finding minimum cost](https://www.youtube.com/watch?v=2ACJ9ewUC6U)
    - [Finding maximum value](https://www.youtube.com/watch?v=8AA_81xI3ik)
    - [Solve Linear Equations with Python - Simplex Algorithm](https://www.youtube.com/watch?v=44pAWI7v5Zk)

- ### Geometry, Convex hull (videos)
    - [Graph Alg. IV: Intro to geometric algorithms - Lecture 9](https://youtu.be/XIAQRlNkJAw?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3164)
    - [Geometric Algorithms: Graham & Jarvis - Lecture 10](https://www.youtube.com/watch?v=J5aJEcOr6Eo&index=10&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
    - [Divide & Conquer: Convex Hull, Median Finding](https://www.youtube.com/watch?v=EzeYI7p9MjU&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=2)

- ### Discrete math
    - [Computer Science 70, 001 - Spring 2015 - Discrete Mathematics and Probability Theory](http://www.infocobuild.com/education/audio-video-courses/computer-science/cs70-spring2015-berkeley.html)
    - [Discrete Mathematics by Shai Simonson (19 videos)](https://www.youtube.com/playlist?list=PLWX710qNZo_sNlSWRMVIh6kfTjolNaZ8t)
    - [Discrete Mathematics By IIT Ropar NPTEL](https://nptel.ac.in/courses/106/106/106106183/)

---

## Additional Detail on Some Subjects

    I added these to reinforce some ideas already presented above, but didn't want to include them
    above because it's just too much. It's easy to overdo it on a subject.
    You want to get hired in this century, right?

- **SOLID**
    - [ ] [Bob Martin SOLID Principles of Object Oriented and Agile Design (video)](https://www.youtube.com/watch?v=TMuno5RZNeE)
    - [ ] S - [Single Responsibility Principle](http://www.oodesign.com/single-responsibility-principle.html) | [Single responsibility to each Object](http://www.javacodegeeks.com/2011/11/solid-single-responsibility-principle.html)
        - [more flavor](https://docs.google.com/open?id=0ByOwmqah_nuGNHEtcU5OekdDMkk)
    - [ ] O - [Open/Closed Principle](http://www.oodesign.com/open-close-principle.html)  | [On production level Objects are ready for extension but not for modification](https://en.wikipedia.org/wiki/Open/closed_principle)
        - [more flavor](http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgN2M5MTkwM2EtNWFkZC00ZTI3LWFjZTUtNTFhZGZiYmUzODc1&hl=en)
    - [ ] L - [Liskov Substitution Principle](http://www.oodesign.com/liskov-s-substitution-principle.html) | [Base Class and Derived class follow ‘IS A’ Principle](http://stackoverflow.com/questions/56860/what-is-the-liskov-substitution-principle)
        - [more flavor](http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgNzAzZjA5ZmItNjU3NS00MzQ5LTkwYjMtMDJhNDU5ZTM0MTlh&hl=en)
    - [ ] I - [Interface segregation principle](http://www.oodesign.com/interface-segregation-principle.html) | Clients should not be forced to implement interfaces they don't use
        - [Interface Segregation Principle in 5 minutes (video)](https://www.youtube.com/watch?v=3CtAfl7aXAQ)
        - [more flavor](http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgOTViYjJhYzMtMzYxMC00MzFjLWJjMzYtOGJiMDc5N2JkYmJi&hl=en)
    - [ ] D -[Dependency Inversion principle](http://www.oodesign.com/dependency-inversion-principle.html) | Reduce the dependency In composition of objects.
        - [Why Is The Dependency Inversion Principle And Why Is It Important](http://stackoverflow.com/questions/62539/what-is-the-dependency-inversion-principle-and-why-is-it-important)
        - [more flavor](http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgMjdlMWIzNGUtZTQ0NC00ZjQ5LTkwYzQtZjRhMDRlNTQ3ZGMz&hl=en)


- **Union-Find**
    - [Overview](https://www.coursera.org/learn/data-structures/lecture/JssSY/overview)
    - [Naive Implementation](https://www.coursera.org/learn/data-structures/lecture/EM5D0/naive-implementations)
    - [Trees](https://www.coursera.org/learn/data-structures/lecture/Mxu0w/trees)
    - [Union By Rank](https://www.coursera.org/learn/data-structures/lecture/qb4c2/union-by-rank)
    - [Path Compression](https://www.coursera.org/learn/data-structures/lecture/Q9CVI/path-compression)
    - [Analysis Options](https://www.coursera.org/learn/data-structures/lecture/GQQLN/analysis-optional)

- **More Dynamic Programming** (videos)
    - [6.006: Dynamic Programming I: Fibonacci, Shortest Paths](https://www.youtube.com/watch?v=r4-cftqTcdI&ab_channel=MITOpenCourseWare)
    - [6.006: Dynamic Programming II: Text Justification, Blackjack](https://www.youtube.com/watch?v=KLBCUx1is2c&ab_channel=MITOpenCourseWare)
    - [6.006: DP III: Parenthesization, Edit Distance, Knapsack](https://www.youtube.com/watch?v=TDo3r5M1LNo&ab_channel=MITOpenCourseWare)
    - [6.006: DP IV: Guitar Fingering, Tetris, Super Mario Bros.](https://www.youtube.com/watch?v=i9OAOk0CUQE&ab_channel=MITOpenCourseWare)
    - [6.046: Dynamic Programming & Advanced DP](https://www.youtube.com/watch?v=Tw1k46ywN6E&index=14&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
    - [6.046: Dynamic Programming: All-Pairs Shortest Paths](https://www.youtube.com/watch?v=NzgFUwOaoIw&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=15)
    - [6.046: Dynamic Programming (student recitation)](https://www.youtube.com/watch?v=krZI60lKPek&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=12)

- **Advanced Graph Processing** (videos)
    - [Synchronous Distributed Algorithms: Symmetry-Breaking. Shortest-Paths Spanning Trees](https://www.youtube.com/watch?v=mUBmcbbJNf4&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=27)
    - [Asynchronous Distributed Algorithms: Shortest-Paths Spanning Trees](https://www.youtube.com/watch?v=kQ-UQAzcnzA&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=28)

- MIT **Probability** (mathy, and go slowly, which is good for mathy things) (videos):
    - [MIT 6.042J - Probability Introduction](https://www.youtube.com/watch?v=SmFwFdESMHI&index=18&list=PLB7540DEDD482705B)
    - [MIT 6.042J - Conditional Probability](https://www.youtube.com/watch?v=E6FbvM-FGZ8&index=19&list=PLB7540DEDD482705B)
    - [MIT 6.042J - Independence](https://www.youtube.com/watch?v=l1BCv3qqW4A&index=20&list=PLB7540DEDD482705B)
    - [MIT 6.042J - Random Variables](https://www.youtube.com/watch?v=MOfhhFaQdjw&list=PLB7540DEDD482705B&index=21)
    - [MIT 6.042J - Expectation I](https://www.youtube.com/watch?v=gGlMSe7uEkA&index=22&list=PLB7540DEDD482705B)
    - [MIT 6.042J - Expectation II](https://www.youtube.com/watch?v=oI9fMUqgfxY&index=23&list=PLB7540DEDD482705B)
    - [MIT 6.042J - Large Deviations](https://www.youtube.com/watch?v=q4mwO2qS2z4&index=24&list=PLB7540DEDD482705B)
    - [MIT 6.042J - Random Walks](https://www.youtube.com/watch?v=56iFMY8QW2k&list=PLB7540DEDD482705B&index=25)

- [Simonson: Approximation Algorithms (video)](https://www.youtube.com/watch?v=oDniZCmNmNw&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=19)

- **String Matching**
    - Rabin-Karp (videos):
        - [Rabin Karps Algorithm](https://www.coursera.org/lecture/data-structures/rabin-karps-algorithm-c0Qkw)
        - [Precomputing](https://www.coursera.org/learn/data-structures/lecture/nYrc8/optimization-precomputation)
        - [Optimization: Implementation and Analysis](https://www.coursera.org/learn/data-structures/lecture/h4ZLc/optimization-implementation-and-analysis)
        - [Table Doubling, Karp-Rabin](https://www.youtube.com/watch?v=BRO7mVIFt08&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=9)
        - [Rolling Hashes, Amortized Analysis](https://www.youtube.com/watch?v=w6nuXg0BISo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=32)
    - Knuth-Morris-Pratt (KMP):
        - [TThe Knuth-Morris-Pratt (KMP) String Matching Algorithm](https://www.youtube.com/watch?v=5i7oKodCRJo)
    - Boyer–Moore string search algorithm
        - [Boyer-Moore String Search Algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm)
        - [Advanced String Searching Boyer-Moore-Horspool Algorithms (video)](https://www.youtube.com/watch?v=QDZpzctPf10)
    - [Coursera: Algorithms on Strings](https://www.coursera.org/learn/algorithms-on-strings/home/week/1)
        - starts off great, but by the time it gets past KMP it gets more complicated than it needs to be
        - nice explanation of tries
        - can be skipped

- **Sorting**

    - Stanford lectures on sorting:
        - [Lecture 15 | Programming Abstractions (video)](https://www.youtube.com/watch?v=ENp00xylP7c&index=15&list=PLFE6E58F856038C69)
        - [Lecture 16 | Programming Abstractions (video)](https://www.youtube.com/watch?v=y4M9IVgrVKo&index=16&list=PLFE6E58F856038C69)
    - Shai Simonson:
        - [Algorithms - Sorting - Lecture 2 (video)](https://www.youtube.com/watch?v=odNJmw5TOEE&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=2)
        - [Algorithms - Sorting II - Lecture 3 (video)](https://www.youtube.com/watch?v=hj8YKFTFKEE&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=3)
    - Steven Skiena lectures on sorting:
        - [CSE373 2020 - Mergesort/Quicksort (video)](https://www.youtube.com/watch?v=jUf-UQ3a0kg&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=8)
        - [CSE373 2020 - Linear Sorting (video)](https://www.youtube.com/watch?v=0ksyQKmre84&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=9)

- NAND To Tetris: [Build a Modern Computer from First Principles](https://www.coursera.org/learn/build-a-computer)

## Video Series

Sit back and enjoy.

- [List of individual Dynamic Programming problems (each is short)](https://www.youtube.com/playlist?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr)

- [x86 Architecture, Assembly, Applications (11 videos)](https://www.youtube.com/playlist?list=PL038BE01D3BAEFDB0)

- [MIT 18.06 Linear Algebra, Spring 2005 (35 videos)](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8)

- [Excellent - MIT Calculus Revisited: Single Variable Calculus](https://www.youtube.com/playlist?list=PL3B08AE665AB9002A)

- [Skiena lectures from Algorithm Design Manual - CSE373 2020 - Analysis of Algorithms (26 videos)](https://www.youtube.com/watch?v=22hwcnXIGgk&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=1)

- [UC Berkeley 61B (Spring 2014): Data Structures (25 videos)](https://archive.org/details/ucberkeley-webcast-PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd)

- [UC Berkeley 61B (Fall 2006): Data Structures (39 videos)](https://archive.org/details/ucberkeley-webcast-PL4BBB74C7D2A1049C)

- [UC Berkeley 61C: Machine Structures (26 videos)](https://archive.org/details/ucberkeley-webcast-PL-XXv-cvA_iCl2-D-FS5mk0jFF6cYSJs_)

- [OOSE: Software Dev Using UML and Java (21 videos)](https://www.youtube.com/playlist?list=PLJ9pm_Rc9HesnkwKlal_buSIHA-jTZMpO)

- [MIT 6.004: Computation Structures (49 videos)](https://www.youtube.com/playlist?list=PLDSlqjcPpoL64CJdF0Qee5oWqGS6we_Yu)

- [Carnegie Mellon - Computer Architecture Lectures (39 videos)](https://www.youtube.com/playlist?list=PL5PHm2jkkXmi5CxxI7b3JCL1TWybTDtKq)

- [MIT 6.006: Intro to Algorithms (47 videos)](https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&nohtml5=False)

- [MIT 6.033: Computer System Engineering (22 videos)](https://www.youtube.com/watch?v=zm2VP0kHl1M&list=PL6535748F59DCA484)

- [MIT 6.034 Artificial Intelligence, Fall 2010 (30 videos)](https://www.youtube.com/playlist?list=PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi)

- [MIT 6.042J: Mathematics for Computer Science, Fall 2010 (25 videos)](https://www.youtube.com/watch?v=L3LMbpZIKhQ&list=PLB7540DEDD482705B)

- [MIT 6.046: Design and Analysis of Algorithms (34 videos)](https://www.youtube.com/watch?v=2P-yW7LQr08&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)

- [MIT 6.824: Distributed Systems, Spring 2020 (20 videos)](https://www.youtube.com/watch?v=cQP8WApzIQQ&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB)

- [MIT 6.851: Advanced Data Structures (22 videos)](https://www.youtube.com/watch?v=T0yzrZL1py0&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf&index=1)

- [MIT 6.854: Advanced Algorithms, Spring 2016 (24 videos)](https://www.youtube.com/playlist?list=PL6ogFv-ieghdoGKGg2Bik3Gl1glBTEu8c)

- [Harvard COMPSCI 224: Advanced Algorithms (25 videos)](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uP4rJgf5ayhHWgw7akUWSf)

- [MIT 6.858 Computer Systems Security, Fall 2014](https://www.youtube.com/watch?v=GqmQg-cszw4&index=1&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)

- [Stanford: Programming Paradigms (27 videos)](https://www.youtube.com/playlist?list=PL9D558D49CA734A02)

- [Introduction to Cryptography by Christof Paar](https://www.youtube.com/playlist?list=PL6N5qY2nvvJE8X75VkXglSrVhLv1tVcfy)
    - [Course Website along with Slides and Problem Sets](http://www.crypto-textbook.com/)

- [Mining Massive Datasets - Stanford University (94 videos)](https://www.youtube.com/playlist?list=PLLssT5z_DsK9JDLcT8T62VtzwyW9LNepV)

- [Graph Theory by Sarada Herke (67 videos)](https://www.youtube.com/user/DrSaradaHerke/playlists?shelf_id=5&view=50&sort=dd)

## Computer Science Courses

- [Directory of Online CS Courses](https://github.com/open-source-society/computer-science)
- [Directory of CS Courses (many with online lectures)](https://github.com/prakhar1989/awesome-courses)

## Algorithms implementation

- [Multiple Algorithms implementation by Princeton University](https://algs4.cs.princeton.edu/code)


## Papers

- [Love classic papers?](https://www.cs.cmu.edu/~crary/819-f09/)
- [1978: Communicating Sequential Processes](http://spinroot.com/courses/summer/Papers/hoare_1978.pdf)
    - [implemented in Go](https://godoc.org/github.com/thomas11/csp)
- [2003: The Google File System](http://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)
    - replaced by Colossus in 2012
- [2004: MapReduce: Simplified Data Processing on Large Clusters]( http://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)
    - mostly replaced by Cloud Dataflow?
- [2006: Bigtable: A Distributed Storage System for Structured Data](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf)
- [2006: The Chubby Lock Service for Loosely-Coupled Distributed Systems](https://research.google.com/archive/chubby-osdi06.pdf)
- [2007: Dynamo: Amazon’s Highly Available Key-value Store](http://s3.amazonaws.com/AllThingsDistributed/sosp/amazon-dynamo-sosp2007.pdf)
    - The Dynamo paper kicked off the NoSQL revolution
- [2007: What Every Programmer Should Know About Memory (very long, and the author encourages skipping of some sections)](https://www.akkadia.org/drepper/cpumemory.pdf)
- 2012: AddressSanitizer: A Fast Address Sanity Checker:
    - [paper](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37752.pdf)
    - [video](https://www.usenix.org/conference/atc12/technical-sessions/presentation/serebryany)
- 2013: Spanner: Google’s Globally-Distributed Database:
    - [paper](http://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf)
    - [video](https://www.usenix.org/node/170855)
- [2015: Continuous Pipelines at Google](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43790.pdf)
- [2015: High-Availability at Massive Scale: Building Google’s Data Infrastructure for Ads](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44686.pdf)
- [2015: How Developers Search for Code: A Case Study](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43835.pdf)
- More papers: [1,000 papers](https://github.com/0voice/computer_expert_paper)

## LICENSE

[CC-BY-SA-4.0](./LICENSE.txt)
