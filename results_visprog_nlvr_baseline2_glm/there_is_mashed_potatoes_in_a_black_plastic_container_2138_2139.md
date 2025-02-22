Question: there is mashed potatoes in a black plastic container

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/6e/66/3b/6e663b6982575451fb49aecfec4c37ea--idahoan-mashed-potatoes-green-bean-casserole.jpg

Right image URL: https://i.pinimg.com/736x/15/2b/41/152b413d659b99c29079332f69585f57--potato-dishes-potato-recipes.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAqAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDori7lW8fTZ9UAuC+0wWUZLp6bmweQOScirNmbi5t0lBWOJ/lt3my0kuB94rxjJ7VvLa2/h3TYLGBN6yRHfMR80jEncSTz1P61wb6zdwXLwEwzSZUwsqsBtyeD2zxj865q05pe6zaEY31NrU4Y50SKSS3eQ8bZuMn0H+FeceMtLv7K4RoLWa3YjDKDhCO2AK7q01PzLdY7xITEWyWDBj9eKvSyS3Fm6lUkmVQwR02hkXqu7s2Mn6isIYid7TNJU1a6OF0xHFlFCkVw4xy0jHdnvkmuj0vQ7C70rUZNRtzL5QTaRkMmd2cMOnQVA1wIr4265RiN0aN/y0X1U9/cdQRU0cUUsNxJM8mfIcLGBlZX7Bh6YyPxrvck4XRjGL5x3h+aznt7a00XyoIPMka4aOQyfOOqhjjccY56Y6VoeM9dW28D6wuokojW7QxRyEbjL/yzK+4bBz9a5Ozvv7OuWhsEleQ7UNtZxNKI2I6HHQ5zjJrK8S6Jc3GoImvPfRSuvmRxXIwCPwyPwzXm1MtrSxCr87Ud7f10Oz6zB0/Z2V+5DpHxj8RR6RFYCytZ54V2rcO5Bx7jua6C0+EureKimv8AijWzb3t0okFvHBkxoR8oOSMH2/XNZPhfS7Cy8R6PsjjaP7dEZC2MEZ7/AI4r2zWGmfTBN56RhTukmztG3ngH2rtnJRimlqc6T5rHgGveBtX8Oh5J4Umt1k8sSo+OcZ5HUfyrFS3kZci0z9Gr3iG/069XUkRvtFnDpjtcyS5+8ythcnocfyFeD6ZPIZQrFsEd6hSco8xalrYPsVy2CtqcfWiungj/AHKkuORnGOlFF2XoesQ+JbfxN4blmhiEN3FlZ7Zmy0MuO3qCM4Pce4rxeO+sGhvPt09xIGkfyUEZx5meG3jp3GRz7VEvj+xsNSTU9Pe5NwMJNG8eFnT0PPUdQfWrDeNvC5vZnWG5WC5+eRPJGFk9QM9/5/WtnE5E0T2+pSQxxLayK8KJtWOZ9rYzyCwGGHOecV02neMruK9iiS1t5YSwBjmuUwTjqDkn8MV5zda7oElwWtbi7gBOSfIGD+G6rFn4l8O2NzFcmS7nnU5DC3VAD6/eOazdGL6Fc77npGqWtjJaiC7mVBbAsblB5fluWLEr7AnGPaqdzql1qeiWtlph8+/fESXCxbHk3n77AegGa4TX/GtjqsXki6u2jzkD7Oq4/HJ596v+GfEMTzLJYhkFoYyVYY3Y6A+vQ59c1cfd1Y4+87I+g7fRIPDvh+30vTEZRGo/fZ5Zs5LOe+ef5VgStK2pxWlzKt7b38EkRDYV0YYLKT/dYHr24qIfFLSJ9Hke4lS11CNchJlYoxyB8pHXj1rg/E3j5vDOsyjTYFvLma2WSG8fqocZGOOnfHfjNYyUva3b3KStGxwSLOPE15p8U0cSW8r75JXwkaKcEk9/w5NdXc/ES5WL7PIG1K1CKm6YlC2O4UDA9Bnn1z28xRLi6vmmlV5JJHLu3cknJNd/4Q8Jx+Kr2W0NxPDFFAZJCFXcTkAAexycntVz5XO8n7vYaT5PMmXWfE3inS7jS9F0l1sS++7+zAu8h6gO3YcdO+KwdPiVXZjOqlcrtOcg+hr6IsreDTk3lY7e1CokaRoFDYGFYkDk9cAdB9a57x1pOm6loEl7LAqXvlOYzbou+ZlyQu4joayeJpN8lrdv+CUqclrueaRyBIlVHUKBgcUVzENwfKByATyfl/8Ar0Um7M0Rx9FFFdpwBRRRQAV23w/t/tH9ojy2bHl9DjH3q4mu++GhIGqYPaP/ANmrOs7QbNaCvUSN+70VJd2RKAwxw/SmeILKDVNUa5RJo4ljjhRTydqKFH8q13ZsD5j09apXRPz8mvNdT31O2qv+Nv8AI9H2atYybHw6jySOLkW8SAF5JD0B9B1J9hWxpeqWmharbS2to720b5uJJAPNnXuB2Ud8e3NZNwxDHBPT1rPuHYxDLH86fNKU+aT07dPn3E4JRsj22DxHp+tSLLHq9t5RwyQyusbR8YIIPQ+361z3xA8aaJaQbLC8W9vxHshjiIKRnBAdyO4zkD1ryI/Mh3c/WoEUegrSFKEfftcyk5fCUgkhGcZ/GitZQAOgorXnZPIj/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

