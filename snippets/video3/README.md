# Unpacking

In this video we look at several forms of "unpacking" in Python—pulling values out of a sequence (or other iterable) into individual variables in a single, readable statement.

## Basic tuple / list unpacking

```python
coordinates = (40.650002, -73.949997)
lat, lon = coordinates  # two variables in one shot
```

## Ignoring values with _

```python
full_name = 'gwen pena'.split()  # ['gwen', 'pena']
_, last_name = full_name  # underscore means: we intentionally ignore the first value
```

`_` is just a normal variable name, but by convention it signals "unused here." (In other contexts, like translation libraries, `_` can mean something else, so use judgement.)

## Extended (starred) unpacking

You can capture a “middle” (or “rest”) portion using a single starred target.

```python
colors = ['blue', 'red', 'orange', 'brown', 'pink', 'purple']
first, *middle, last = colors
# first -> 'blue'
# middle -> ['red', 'orange', 'brown', 'pink']  # always a new list
# last -> 'purple'
```

Why a list? Starred assignment always builds a list so you can safely modify it regardless of the original iterable type.

## *args in a function definition

```python
def average_numbers(*nums):
    print(f"the average is: {sum(nums)/len(nums)}")

average_numbers(1, 58, 56, 58)
```

`*nums` packs any number of positional arguments into a tuple named `nums`. (If you call it with no numbers, this version would raise a ZeroDivisionError—left that out for brevity.)

## Putting it together

All of these patterns appear in `unpacking.py` in this folder. Open it and tweak values to see how each piece behaves.

## Try it yourself

1. Add a new color to the list and see how `middle` changes.
2. Change the name split to three parts (e.g. `'gwen marie pena'.split()`) and adjust the unpacking with a starred variable to capture the middle name(s):

   ```python
   first, *middles, last = full_name
   ```

3. Add a guard to `average_numbers` so it returns 0 if called with no values.

Happy experimenting!
