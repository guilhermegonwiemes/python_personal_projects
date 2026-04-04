# 🎲 D&D Attribute Roller
 
> Part of [python_personal_projects](https://github.com/guilhermegonwiemes/python_personal_projects)
 
A command-line tool that simulates the **5d6 drop two lowest** method for generating Dungeons & Dragons character attributes — rolling 5 dice and keeping only the 3 highest results.
 
---
 
## How it works
 
- Rolls 5 six-sided dice (d6) for each of the 6 D&D attributes
- Selects the 3 highest values using a heap-based algorithm
- Displays both the individual dice results and the final attribute score
- Uses a `while` loop with a counter to iterate through all 6 attributes
 
---
 
## Concepts covered
 
- `random` library — dice simulation
- `heapq` library — efficient selection of top values (`nlargest`)
- `while` loops with counters
- ANSI escape codes for colored terminal output
- List comprehensions with `for _ in range()` — using `_` as a throwaway variable to generate fixed-size collections
- Functions (`def`) — encapsulating the rolling logic into a reusable, callable block instead of writing it directly in the global scope
 
---
 
## Technologies
 
| Library | Purpose |
|---------|---------|
| `random` | Pseudorandom number generation |
| `heapq` | Heap queue — efficient largest/smallest selection |
 
---
 
## Sample output
 
```
=== D&D Attribute Roller ===
 
Attributes to distribute:
 
14
[3, 6, 5, 2, 6]
 
11
[4, 1, 3, 4, 6]
 
...
```
