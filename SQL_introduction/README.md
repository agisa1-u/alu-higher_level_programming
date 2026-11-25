# SQL_introduction

Introduction to SQL: databases, tables and basic queries. Scripts are run with:

```
cat <script>.sql | mysql -hlocalhost -uroot -p [database]
```

| File | Description |
| --- | --- |
| `0-list_databases.sql` | List all databases of the MySQL server |
| `1-create_database_if_missing.sql` | Create the database `hbtn_0c_0` if missing |
| `2-remove_database.sql` | Delete the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | List all the tables of a database |
| `4-first_table.sql` | Create `first_table` (`id` INT, `name` VARCHAR(256)) if missing |
| `5-full_table.sql` | Print the full description of `first_table` |
| `6-list_values.sql` | List all rows of `first_table` |
| `7-insert_value.sql` | Insert `(89, 'Best School')` in `first_table` |
| `8-count_89.sql` | Count the records with `id = 89` in `first_table` |
| `9-full_creation.sql` | Create `second_table` and add 4 rows |
| `10-top_score.sql` | List score and name, best score first |
| `11-best_score.sql` | List records with a score >= 10, best score first |
| `12-no_cheating.sql` | Update Bob's score to 10 (by name) |
| `13-change_class.sql` | Remove all records with a score <= 5 |
| `14-average.sql` | Score average (column `average`) |
| `15-groups.sql` | Number of records per score (column `number`), most first |
| `16-no_link.sql` | List score and name, skipping rows without a name |
