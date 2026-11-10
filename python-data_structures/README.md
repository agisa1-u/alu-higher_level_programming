# python-data_structures

Python exercises on lists, tuples and basic data structures, from the ALU Higher Level Programming curriculum.

All files are written for Python 3, start with `#!/usr/bin/python3`, are PEP8 (pycodestyle) compliant, and are executable.

## Tasks

| File | Description |
| --- | --- |
| `0-print_list_integer.py` | Prints all integers of a list, one per line |
| `1-element_at.py` | Retrieves an element from a list like in C (returns `None` if out of range) |
| `2-replace_in_list.py` | Replaces an element of a list at a specific position |
| `3-print_reversed_list_integer.py` | Prints all integers of a list in reverse order |
| `4-new_in_list.py` | Replaces an element in a copy of a list, leaving the original unchanged |
| `5-no_c.py` | Removes all characters `c` and `C` from a string |
| `6-print_matrix_integer.py` | Prints a matrix of integers |
| `7-add_tuple.py` | Adds 2 tuples (first two elements, missing values count as 0) |
| `8-multiple_returns.py` | Returns a tuple with the length of a string and its first character |
| `9-max_integer.py` | Finds the biggest integer of a list without using `max()` |
| `10-divisible_by_2.py` | Returns a list of booleans: is each integer a multiple of 2 |
| `11-delete_at.py` | Deletes the item at a specific position in a list without `pop()` |
| `12-switch.py` | Switches the values of `a` and `b` |

## Usage

```python
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

print_list_integer([1, 2, 3])
```
