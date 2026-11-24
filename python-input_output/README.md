# python-input_output

Reading and writing files, JSON serialization and a technical interview exercise.

| File | Description |
| --- | --- |
| `0-read_file.py` | `read_file(filename="")`: print a UTF-8 text file to stdout |
| `1-write_file.py` | `write_file(filename="", text="")`: write (overwrite) a file, return characters written |
| `2-append_write.py` | `append_write(filename="", text="")`: append to a file, return characters added |
| `3-to_json_string.py` | `to_json_string(my_obj)`: JSON string of an object |
| `4-from_json_string.py` | `from_json_string(my_str)`: object from a JSON string |
| `5-save_to_json_file.py` | `save_to_json_file(my_obj, filename)`: write an object as JSON to a file |
| `6-load_from_json_file.py` | `load_from_json_file(filename)`: object from a JSON file |
| `7-add_item.py` | Script that adds its arguments to the list saved in `add_item.json` |
| `8-class_to_json.py` | `class_to_json(obj)`: dictionary description of an object |
| `9-student.py` | `Student` with `to_json()` |
| `10-student.py` | `Student` with `to_json(attrs=None)` (attribute filter) |
| `11-student.py` | `Student` with `to_json()` and `reload_from_json()` |
| `12-pascal_triangle.py` | `pascal_triangle(n)`: Pascal's triangle as a list of lists |

### Advanced tasks

| File | Description |
| --- | --- |
| `100-append_after.py` | `append_after(filename="", search_string="", new_string="")`: insert a text after each line containing a string |
| `101-stats.py` | Script that reads log lines from stdin and prints the total file size and status code counts every 10 lines and on CTRL + C |
