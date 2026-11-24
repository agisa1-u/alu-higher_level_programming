# python-inheritance

Python classes, inheritance and introspection.

| File | Description |
| --- | --- |
| `0-lookup.py` | `lookup(obj)`: list of attributes and methods of an object |
| `1-my_list.py` | `MyList(list)` with `print_sorted()` (tests: `tests/1-my_list.txt`) |
| `2-is_same_class.py` | `is_same_class(obj, a_class)`: exact instance check |
| `3-is_kind_of_class.py` | `is_kind_of_class(obj, a_class)`: instance of the class or a subclass |
| `4-inherits_from.py` | `inherits_from(obj, a_class)`: instance of a strict subclass |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` with `area()` raising an Exception |
| `7-base_geometry.py` | `BaseGeometry` with `integer_validator()` (tests: `tests/7-base_geometry.txt`) |
| `8-rectangle.py` | `Rectangle` inheriting from `BaseGeometry`, private width/height |
| `9-rectangle.py` | `Rectangle` with `area()` and `[Rectangle] <width>/<height>` description |
| `10-square.py` | `Square` inheriting from `Rectangle` |
| `11-square.py` | `Square` with `[Square] <width>/<height>` description |

Run the doctests from this directory:

```
python3 -m doctest -v tests/1-my_list.txt
python3 -m doctest -v tests/7-base_geometry.txt
```
