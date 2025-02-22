Question: Both images show stingrays over the sand.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/Iu8q1buU2p8/maxresdefault.jpg

Right image URL: http://pellagofio.es/wp-content/uploads/2016/04/chucho-negro-4116-1.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAhAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDhYoG9Ktx27VehtlGKW9lWwtvOKFucAA19e6qSuz4yddzlyxIEt2p/ktU1jf2t3GhOY2bgqx6VpCCNlBWRSD0II5oVa5zVKkoO0kYrRMKryIRW5NAkUbSSMFRRkk1gNqlqWIYEDOAQc8Ue2SNqMpVNYq5C69apNbSSTFkUkYA6Vs7IJv8AVSox9jVpdKvLrRJRZumUcl03AOwPp3rkxlZez36nq4GfNPl6nJTxOrNgfdOMCoJYpTEWV0Rh0+cAn8KuTQTWshjmhaN142uKqmN3mUAqCa832lkesolCGa4W6InPb8BV9bjHfIqaXT5Idsc4UNnHTn61nSwSKzcEEHFa0sQ4qzFKNy8bgetFZJLZ5zmitfrSFyHpkH0Jqnq0F9cJiLyzGOgJqJNVTy1bdjd69qbcyzXAxGWx61o6itY+Yp0akKnM195gyQXMT/vOMenStnw/bpLIs0oyqfdVjkGqf9n3TTBuOD61v2cKQBFGCW7+9ZxZ14uv+65U9X2LtxbeZA6wts4wV6qfwrl5tJmWTDQKVz1FdYpII5wMVFJOigll4HU1TZ5mHr1KWkdShawrawBFi2+vPU1s2+nznR11KBwUjnKyxqcMRx+Y5zVB4mIyqSYPONp6flWtoniLStKs5LG/uI452k3hJpFQIP73PfGa5cY70reZ62VXeIcn2ZTvY/t5TYVZwobIz8x6dD2rEl023YyM8IVh93y8qK6u68S6I7MV1exLYwpMynJ9T6Vz11qmkzTiZdUtMk4OJhx3zya44LTc99mfCrksM+cuPl8xQ2APQjFFxp5ky8sK+U3Hyfw/WrVreaPFdFxqlqEOThpR1/OrN5q+l4RotStM4P8Ay3U9OlbKfKtTNxu9DjLuwMVwyoNy9jRWxcarp0kxb7Tbfg4orPn8yrMgsfvn/cH8621+7RRXoRPncX8Qg/1wqaD/AFZ/3qKKFuclT4fuLY6j6VF2k+tFFUcsTpE+7F/1zrx/4i/8jbJ/1xT+VFFefW+E+nwH8Q5OiiiuM9kKKKKACiiigD//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

