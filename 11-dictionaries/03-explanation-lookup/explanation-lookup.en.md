# Lookup

In the previous explanation, you were shown how to define a new `dict`:

```python
translating_dictionary = {"cat": "kat", "dog": "hond"}
```

We now turn our attention to actually making use of this `dict`.
The most common operation is to, given a key, _look up_ the associated value.

For example, say we want the translation of `cat`.
Here, `cat` is the key, and `kat` is the value we wish to look up in our dictionary.
We can do this as follows:

```python
translation = translating_dictionary["cat"]
```

After executing this statement, `translation` is equal to `"kat"`.
