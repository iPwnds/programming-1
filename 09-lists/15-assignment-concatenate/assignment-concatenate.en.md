# Concatenation

Given two lists `xs` and `ys`, we wish to add all elements from `ys` to `xs`.

### `TASK`

Write a function `concatenate(xs, ys)` that adds all elements from `ys` to `xs`.
The function must modify `xs` in place.

Be warned: there's a tricky corner case you'll have to take into account.

#### `IMPORTANT`

The easy solution would be to use `xs += ys`.
However, for this exercise, we want you to to manually append the items one by one.

#### USAGE

```python
>>> xs = [1, 2, 3]
>>> concatenate(xs, [4, 5, 6])
>>> xs
[1, 2, 3, 4, 5, 6]
```
