\# Assignment 5: Quicksort Algorithm



\## Description

This project implements and analyzes the Quicksort algorithm, including:

\- Standard (deterministic) Quicksort

\- Randomized Quicksort



Both implementations demonstrate the divide-and-conquer approach.



\---



\## Files

\- quicksort.py → Deterministic Quicksort implementation

\- randomized\_quicksort.py → Randomized pivot Quicksort implementation

\- report.docx → Detailed analysis of algorithm, complexity, and performance



\---



\## How to Run



\### Run Deterministic Quicksort

python quicksort.py



\### Run Randomized Quicksort

python randomized\_quicksort.py



\---



\## Time Complexity Analysis



\### Best Case:

O(n log n) → when pivot divides array evenly



\### Average Case:

O(n log n) → expected behavior of Quicksort



\### Worst Case:

O(n²) → when pivot creates highly unbalanced partitions



\---



\## Randomized Quicksort

Randomized Quicksort selects a random pivot which:

\- Reduces chance of worst-case performance

\- Improves performance stability

\- Works well even on sorted/reverse-sorted data



\---



\## Key Insight

Randomized Quicksort is more robust than deterministic Quicksort because it avoids predictable pivot patterns.



\---



\## Author

Harika Surineni

