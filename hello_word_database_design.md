# hello_word Database Design



## word

| field_name  |   type   | comment |
| :---------: | :------: | :-----: |
|     id      |   int    |         |
|     en      | varchar  |         |
|     ch      | varchar  |         |
|    stage    |  double  |         |
|  is_master  | boolean  |         |
| next_review | datetime |         |



## review

|  field_name  |   type   | comment |
| :----------: | :------: | :-----: |
|      id      |   int    |         |
|   word_id    |   int    |         |
|  review_at   | datetime |         |
| error_count  |   int    |         |
| stage_before |   int    |         |
| stage_after  |   int    |         |



