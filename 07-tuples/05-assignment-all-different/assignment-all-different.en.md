<<<<<<< HEAD
# All Different

### `TASK`

Write a function `all_different(xs)` that returns `True` if all elements are distinct, `False` otherwise.

#### `HINT 1`

Contrary to `all_equal`, you will have to compare every pair of elements.

#### `HINT 2`

Say `xs` contains 4 elements, then the checks you will need to perform are

- `xs[0] != xs[1]`
- `xs[0] != xs[2]`
- `xs[0] != xs[3]`
- `xs[1] != xs[2]`
- `xs[1] != xs[3]`
- `xs[2] != xs[3]`

To accomplish this, you will need nested loops, i.e., a loop within a loop.

#### `HINT 3`

You should check all `xs[i] != xs[j]` where both `i` and `j` take on all possible combinations of indices.

- You should skip the cases where `i == j`, as it makes no sense to demand that an element is not equal to itself.
- If `xs[i] != xs[j]`, you don't have to check `xs[j] != xs[i]`.
  You can halve the amount of comparisons by only considering the cases where `i < j`, i.e., only compare elements with elements that occur on the right of them.
=======
# All Different

### `TASK`

Write a function `all_different(xs)` that returns `True` if all elements are distinct, `False` otherwise.

#### Example usage

```python
>>> all_different((1,2,3,4,5))
True
>>> all_different((1,2,3,2,5))
False
>>> all_different((1))
True
>>> all_different(())
True
```

#### `HINT 1`

Contrary to `all_equal`, you will have to compare every pair of elements.

#### `HINT 2`

Say `xs` contains 4 elements, then the checks you will need to perform are

- `xs[0] != xs[1]`
- `xs[0] != xs[2]`
- `xs[0] != xs[3]`
- `xs[1] != xs[2]`
- `xs[1] != xs[3]`
- `xs[2] != xs[3]`

To accomplish this, you will need nested loops, i.e., a loop within a loop.

#### `HINT 3`

You should check all `xs[i] != xs[j]` where both `i` and `j` take on all possible combinations of indices.

- You should skip the cases where `i == j`, as it makes no sense to demand that an element is not equal to itself.
- If `xs[i] != xs[j]`, you don't have to check `xs[j] != xs[i]`.
  You can halve the amount of comparisons by only considering the cases where `i < j`, i.e., only compare elements with elements that occur on the right of them.
>>>>>>> d0ee4a0d3ecca4132dc987a26264480e89ab4952
