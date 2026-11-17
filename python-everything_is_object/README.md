# python-everything_is_object

Python exercises on objects, identity, mutability and how arguments are passed to functions, from the ALU Higher Level Programming curriculum.

## Files

| File | Content |
| --- | --- |
| `0-answer.txt` - `18-answer.txt` | Answers about `type`, `id`, `is` vs `==`, aliases, and mutable / immutable behaviour |
| `19-copy_list.py` | `copy_list(l)`: returns a (shallow) copy of a list, in 3 lines |
| `20-answer.txt` - `28-answer.txt` | Answers about tuples and whether `id` changes (`+` vs `+=` on lists) |
| `100-magic_string.py` | `magic_string()`: returns `BestSchool` repeated once more on every call, in 4 lines |
| `101-locked_class.py` | Advanced: `LockedClass` only accepts the instance attribute `first_name` (uses `__slots__`) |
| `103-line1.txt` - `106-line5.txt` | Advanced: how many `int` / `str` objects CPython creates (small-int cache of 262 integers, string interning) |

Each answer file holds a single answer on one line. Answers were checked by running the code, and compared with what the course review expects. Note: `"Best School" is "Best School"` (task 9) is `True` and `(1, 2) is (1, 2)` (task 25) is `False`.
