Question: No image shows broccoli in a container, and the right image contains exactly two cut pieces of broccoli.

Reference Answer: True

Left image URL: https://st2.depositphotos.com/1901991/7537/i/450/depositphotos_75371995-stock-photo-broccoli.jpg

Right image URL: https://st2.depositphotos.com/3337459/9114/i/450/depositphotos_91145336-stock-photo-broccoli-on-a-black-background.jpg

Original program:

```
Statement: No image shows broccoli in a container, and the right image contains exactly two cut pieces of broccoli.
Program:
ANSWER0=VQA(image=LEFT,question='Is the broccoli in a container?')
ANSWER1=VQA(image=RIGHT,question='Is the broccoli in a container?')
ANSWER2=VQA(image=LEFT,question='How many pieces of broccoli are there?')
ANSWER3=VQA(image=RIGHT,question='How many pieces of broccoli are there?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER1}')
ANSWER5=EVAL(expr='{ANSWER2} == 0 and {ANSWER3} == 2')
ANSWER6=EVAL(expr='{ANSWER4} and {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'No image shows broccoli in a container, and the right image contains exactly two cut pieces of broccoli.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAhAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDiVFSKpJAAJJ6AUwdKdBeLFc7R94d/SplPlRRoW9oYmRp4CQxwAwyP0rZTT9LugI2tzE+PvISMH3rGiv3EzEbgq4xgHH+eta0cizRGdiVYkZB6dhxXLKUm73M22V7jw05B+ys3mY3LFJj5h7MK5xjXoEVy0cdq20MN5zj8P8f0ritZtTZarcRZypYuh9VPIrpw85PSQJ3OUvwP7QlJ9v5CrtppVxcAFVUD/aPI/CpIo4Rq5L4LyLld3IXGK6jTkMyqkK739FHOKyrV+VtI1Rz8mjXMEQk2iRO+zt+FVjHgkEYI6g9q75YF2SQzrKkiELjGD+vaua1WykuPEFvKY82n3XcnAJ6gHv8AnWcMUvtFXMqKwnuQTFEWA5J7VTntnQ7ShU+hGK7eOeKRgsJAcDDEDH4VSvGgnZ7aQqyqu4EHleucmhYrXVaBocU0WGoqS4dYbiSPOdpxn1orsTTVxG+DVG4tn+0mRX+V8cH1q72rO1C7MK4HXrWco3Ey/b3pkKFsqwGBj2711EBD26kfe24GOorz+w1GEyIkkscY3Z+cHAHcV2On6laRxs/2mIQIM794OP8APpWTizNnRRxgw/ZwwBjw+TxjA7/h/KuR1u9S91AvF/qkURofUDvVe68Si+823t4ikLNzIx+Zx9OwqmWzXRShbVgkczqVzNBrkkkTkMu3H5Cug8IapdyT3FsfOmZl8xVUE4C5Lfh3rIvrdJNQlYjk4/kK1vD97LoepJe2o+YKUdCeHQ8FTjsazxEHKEuVa9DRI39X8SDT7O1nCThpGwy7cfLgnjPfOK5O/wDFtxcxGOBGj3SB2Jx2OR0rb8RX58SXlvM1pBbRQR+WkUWSAM9ST1NZyaZH1EQx7isaFD3E6i1G1qaXhjVb/XJn09YVeR23khSercnHtkfhWLq9lNpGsXlhG8m6F9khJ5JHXNaWnyzaZOLm0doJl4DxjBHtVe/uJLu4luJ2Mk0rF3durE9SacKEo1nLTltt5jtoYTJITnB/OirLt8x/worqJOj7Vj6n940UUkJmG3Wlh++PrRRVkGpZ/eFag6UUVSGYl7/yEJPw/kKWPr+FFFQ9ykWV6CrEf+qaiigpEbfdqnN3oopAysaKKKYj/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'No image shows broccoli in a container, and the right image contains exactly two cut pieces of broccoli.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

