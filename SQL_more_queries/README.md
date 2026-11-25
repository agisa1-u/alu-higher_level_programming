# SQL_more_queries

Users and privileges, constraints, foreign keys, subqueries and joins. Scripts are run with:

```
cat <script>.sql | mysql -hlocalhost -uroot -p [database]
```

Scripts 10 to 16 use the `hbtn_0d_tvshows` database (tables `tv_shows`, `tv_genres` and `tv_show_genres`), which must be imported from the project's dump first.

| File | Description |
| --- | --- |
| `0-privileges.sql` | List the privileges of `user_0d_1` and `user_0d_2` (localhost) |
| `1-create_user.sql` | Create `user_0d_1` (password `user_0d_1_pwd`) with all privileges |
| `2-create_read_user.sql` | Create `hbtn_0d_2` and `user_0d_2` with only SELECT on it |
| `3-force_name.sql` | Table `force_name` (`name` can't be null) |
| `4-never_empty.sql` | Table `id_not_null` (`id` defaults to 1) |
| `5-unique_id.sql` | Table `unique_id` (`id` defaults to 1 and is unique) |
| `6-states.sql` | Database `hbtn_0d_usa` and table `states` |
| `7-cities.sql` | Table `cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Cities of California, using a subquery |
| `9-cities_by_state_join.sql` | All cities with their state |
| `10-genre_id_by_show.sql` | Shows with at least one genre linked |
| `11-genre_id_all_shows.sql` | All shows, `NULL` when no genre |
| `12-no_genre.sql` | Shows without a genre |
| `13-count_shows_by_genre.sql` | Number of shows by genre |
| `14-my_genres.sql` | Genres of the show Dexter |
| `15-comedy_only.sql` | All Comedy shows |
| `16-shows_by_genre.sql` | All shows with all their genres |
