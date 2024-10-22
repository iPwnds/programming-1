# More Set Operations

We give a quick overview of what other set operations are provided.

| Syntax | Description |
| ------- | ------- |
| `s1.intersection(s2, s3, ...)` | Returns common elements |
| `s1 & s2`                      | Same as `s1.intersection(s2)` |
| `s1.union(s2, s3, ...)`        | Returns union of all sets |
| `s1 \| s2`                     | Same as `s1.union(s2)` |
| `s1.difference(s2, s3, ...)`   | Returns the elements of `s1` not present in `s2`, `s3`, ... |
| `s1 - s2`                      | Same as `s1.difference(s2)` |
| `s1.isdisjoint(s2)`            | Checks if the intersection is empty |
| `s1.issuperset(s2)`            | Checks if `s1` contains all elements of `s2` |
| `s1 >= s2`                     | Same as `s1.issuperset(s2)` |
| `s1 > s2`                      | Same as `s1 >= s2 and s1 != s2` |
| `s1.issubset(s2)`              | Checks if `s2` contains all elements of `s1` |
| `s1 <= s2`                     | Same as `s1.issubset(s2)` |
| `s1 < s2`                      | Same as `s1 <= s2 and s1 != s2` |
