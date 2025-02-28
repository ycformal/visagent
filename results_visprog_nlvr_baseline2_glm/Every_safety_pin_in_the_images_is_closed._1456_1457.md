Question: Every safety pin in the images is closed.

Reference Answer: False

Left image URL: https://static1.squarespace.com/static/527afe11e4b06f059b9c5bbe/599f1c90e3df28be468c330e/5928aa5b2994ca7baf9170d4/1504047908544/_DSC9764.jpg?format=500w

Right image URL: https://static1.squarespace.com/static/527afe11e4b06f059b9c5bbe/599f1c90e3df28be468c330e/5928aa5c46c3c4128b9f260d/1504047908539/_DSC9765.jpg?format=500w

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
ANSWER0=VQA(image=IMAGE,question="Is 'Every safety pin in the images is closed.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAhAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzgMMc4+tSwwSzAlFJUdWPAH4nio45IYdzzHAx8rYzzRPqNvdNGsFvIVXqxO0N+fP6Vk5HQkTGOKPh7hSfSJd36nAqxJHBOgkgR4igBljPzvGMfeZeuM9x61Uhbcx8yZLWILlmQYPUD7xOe/qKaYDaPHc2s3ysSYriLI3EdfcH1B5qW22UkTPGyY3BSGGVZTlWHqCOoqLG7K5A/u1bstZ06O6A1e1xHJxI8WVUn+8QOAfcD61XvDYvcMdPuDcWxAKsRgg+h9SKE+4yIbt3zDmgjkUttKIJUkdQyA8jJ6ev9afPcXKzFL6COUgAAocNjHBDfxZHOT6076isW7G0tbkjzLpVY5DKrjep/wB08miex8mQqYr0xdVl+yMVP4g1QNpbXvMBWZu8UqgSD8Oh/D8qbD5kAKwSywlTyEcr+lK40tS0ywY2i8gz2D7o2/JgKa1rdpIyRpuIG4iMhuPXj6VKt/erY3E893LKgHlxpI24Fz9fQZP5Vnfab5I4xHMill3P8gyMng/XH86SbGyYMGGSgOe4FFRB5EAVWUACimO6EYhoyCM4wcUgKoOAKYpyMA89qVipfOMg8EehqiC9aASySRH/AJaROo+uMj9RUEVwYdw2eZDJjzIs43ehHow7H8OlFhcLFdwTuuVSRSw9QDz+maaJTb3BaBh8jkxlhkEA8Z/CoZQ66tigXepKONyFlxuH07GmIPLXaFwPTFb2q67aajpscH2aY3DICPl4jbuN3esNkKrls8e/UVKlpqUkxhfacYzVqKQXNskEh/fRj9wx7jqUP8x75HeqTOM5Xhl/Wmq7eY2W6cg1o9UR1LJtZJ4TMsLFB/EB/Kpo7+VrXyLhI7hR9yRxiWP/AIEOSPY5qxF4g+y2Txzo7yN8pRU4b0bPY1kxSF382RApY7tg6D2qQV76ouvE87W8LApApZy+OPVj+Q/Sq5fzJS4GAxyB6DsPyp91creMsUBYJwpU9hnJJ/QUyQhB1G4cGi62Q43auxuR/k0VCz4Yg0UWHcRPv/jTv4n+oooq2Qtgi6n61IfvH6UUVL3LjsTwfdX60XfX8KKKx+0bP4Sm3Rf9yhf9f+f9aKK36HP1JG/1f4D+VM/gNFFSX1H2/wDx8N9DTLr/AF5/z2oorOluXV2In6j6CiiitkYPc//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Every safety pin in the images is closed.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

