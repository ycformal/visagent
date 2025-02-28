Question: The fragrance bottle on the left is green with a silver cylindrical cap, and the bottle on the right is an upright rectangle with rounded edges.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/92/51/e0/9251e0ab7b3893663137211fae42bd33--perfumes-for-men-eau-de-cologne.jpg

Right image URL: https://fimgs.net/images/perfume/375x500.2736.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The fragrance bottle on the left is green with a silver cylindrical cap, and the bottle on the right is an upright rectangle with rounded edges.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA5AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigCGWZo5Yo1QMXJ6nGMVnN4ht0hlmMUpjiWZmYDtEcPgfUfjWhMoa4hBGfvfyrz+41zS4ba/tZdUs47lY9QQxNOocOZDtGM5z6CgDv4rnzWjwvySJvVs9uO341YqjZLtW0BGD9nGfyWr1ABRRRQAHpXM33iG6VpjZRROsRQHe+M7iAOx9eT2rpHZUQszBVHUk4Arz3WJNOtpNSjuL/wAt3ni2q5GTH8pLg45A59uKTdhpHW6LrX9qxgPD5cmzccNuU84OD+X51r1yfgl7f+zpDFdGWPzmjicnAcDHIHTNdZRF3QPfQKKKKYgooooAgk/4+ofo38q+aPFI1E+OtVMUt2kbXUpXbsAC5bpmvpWc7biE9gHP6V4l4uureTUjslRt6yOmDncCx5HqKwxFX2aTtc58TW9lDmSue02p3fZT62+f5VdrN024iuY7OaCRZInttyOhyCMjvWlW50BRRRQBWvhutiBjO4YJGcc1HP8AZmIE/lEjkeYAcfnS6pIIrF3PReaqC2t2TcVJLgE5cn+tJrqZubUrIsylHt+CpQkYxyOvar1YswjgCBARufH3iexNbVCVkOM+ZtMKKKKZYUUUUAYfiiVotN+Ryu87GI67SQD+leaXWkayNUhX+z7Z4mXCyC6YOAOmAFxivR/FbqtjGGIGXHX/AHlrzefVp95zOh2nCk4OBXFiqtOD/eK+hz1JQjL31c7zwXLK9r5UsLQGJdvks4cxkhSwyODzmusri/AtyszXC+YHfG4857LXaV00Zc1NSXU1pu8bhRRRWhZm69zo9wM4ypH6VRhula1hYMPmjU/oKm8Vy+R4duZB2x/OvMNO8WeZp9sCeVjVGwehAwf5V1UcPKrC6PJx+Ljh6iv1X+Z397dr59mmeWkP6Ka6qvGY/EIu/EmnwK2doZmHpkqo/rXs1RXpOlZM1y+uqylNd/0CiiisD0QooooA5rxloV9r2nRwWE6QyqxO9u3T/CvNZfhL4vZyya1Z49CW/wDia9voqJQjL4kZypRk7s4PwD4R1jw5c3EmqXMM2+PYpjb3B9Pau8ooqkklZFxioqyCiiimM5rx6XXwbfMisxGzO0Z43AE14c2nwySF3tQWPU7CCfyr6WporuwuN9hBx5bnm4zLvrM1NT5bKx896PZi31W0FtbFWe4jGEjOT8wr6GpB1pazxWJ+sNO1rGuCwX1WLXNzXCiiiuU7T//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The fragrance bottle on the left is green with a silver cylindrical cap, and the bottle on the right is an upright rectangle with rounded edges.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

