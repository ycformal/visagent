Question: One photo contains exactly six multicolored balls, the other image contains at least seven, and all images contain a yellow, blue, and orange ball.

Reference Answer: True

Left image URL: https://sc02.alicdn.com/kf/HTB1kDVaX7OWBuNjSsppq6xPgpXaE/bulk-colored-driving-range-golf-balls.jpg_220x220.jpg

Right image URL: https://sc01.alicdn.com/kf/HTB1MXMKOVXXXXcbXVXXq6xXFXXXQ/crivit-sport-golf-balls-custom-color-bulk.jpg

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

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA7AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0rXdX+xaitrFfTRyFBKw+QKoPQcqSTwTn3ri/FPji9h1uMRyT21mYVMOxtodujEkfeIbj8Olb3imHSda1TdcJJG9n+5aWKXY8ig8joRwc4qjBrkFldJpyxspt5MWsEozgE5BAPUkc575rhrYTFKbc52g9jvyvHYVT92HNJaO/6HoPh7UJL3Q7KW+2reSRAyKRg59/QkYOPetcdBXA6edWl1NrO3ktpoC5PniXouck4PJP0rvkIKAg5GKeDqV5pqtG1tvM5a6aqO6tfWwtFFcf4u8af2FOtlZwrNdsNzF/uxg9M+9dyV9go0J158lNXZ2FNkkSGJpJHCIoyzMcACvO9D+I0012sOqQxrG52+bGCNp966Hx0Zv+EWm8nJBdd+3+7n/9VRWbpwcuxvPA1aVWNOppcafHui/afKV5mXOPMCfL/jXRwTxXMKTQuHjcZVh3rwaKeNZQGXCivV/A7O2iEnPlmQ7M/rXm4PG1K1TkkjqxuBp0KalFnTUUUV6h5IUUUUAcd4m8I2F1De6tBFO16IWk8iOUhJXA4yvc/TGa4TSdTn1y7SxsbhpLy4jaJ2Y7ti45z3UCvG/+FpeOP+hm1D/v4P8ACo1+JfjJHZ08QXiu33mVgC31IHNYV6Uqsoy5noZKmozU4aM+kvDOkeIF1SA6jZC0htmLM5lVt/HRcHkH3xXfw/6lPpXxiPih43z/AMjLqH/fz/61fU/w21C71X4eaLfX1w9xdTW+6SWQ5ZjuPWt73OzEYideXNM6qvJviLpd3Bq8l4kZaG4UfMB0IGCK9M1K/FhAGC7pG4VawX1a7mOJhDJGesbRgqa4cRmVDDT5JPU0wWKeGq89rnmOhadd6ldR2qRFtzDJxXun2dGtRbyKHTZsYMOCMVTsTaxwq9pZBA458tQOfSrfnPtz5D59OK7lUVSKktUzXH494qSaVkjnn8B6M9z5pSULnOwNxWD431u70ma30fSm+ywJGGkZODz0APb/AOvXfidj1gkH5VxHjvwxeayq31hGxmVdrx92HYirwlKlTqXskeZjatapSsm2cxoevapaXImS7klQH5kdiQwr1+2nW5top16SKGA+teQ+G/Cmsy3ASe2khjB+ZnGAK9fghW3t44U+6ihR+FdeMdNtcu5w4CNVX59iSiiiuE9E+AKKKKAAdRX2Z8J/+SXeH/8Ar2/9mavjMdRX2Z8J/wDkl3h//r2/9magDW8SRSeTHOgJVMhvauWS8IbpzXopAYEEAg9QaqppljHL5q2sQfrnbXjYzKvrFX2kZWuBnW99baH4fa+1SZbaEfMS/b0GO59q522+L/hi4uxCWuo0Y4ErxYX6nnIFYXxslkWPTEkLfZRvYgdC3A/l/OvG7SeGW4w64XoK+ny/L6fsEm9jkq15RlZI+tJ9StINLfUmmVrRIjL5inIK4zkV4lq/xa8QXd6zaaUs7UN8i7FZmHqS39K3/Cenalrfwh1fSwzb2aRLQk/w8MB+eR+NeNzLe2115NxG6SRHaVIwQRXm4tSpTcU9j6LJ6dGqnKorvzPofwD42k8SQNa36Kl/Eu7KjAkX1x2NdtXjvwnsbq51U6i0ZSGGMqWxwSe1exUUm3G7ObMaVOnXcaewUUUVocJ8AUUUUAA6ivsz4T/8ku8P/wDXt/7M1fGY6ivsz4T/APJLvD//AF7f+zNQB2dFFFAGR4j8OWPifSmsb5TtzlHX7yN6ivN7T4GwQ34km1Xfbhs7ViwxH54r1+itYV6lNWiyJU4y1aKun6fbaXYxWdpGI4YhhR/U+9VL/wANaLqlwJ73TbeaX++ycn6+tatFZPXc0i3H4dCK2tYLOBYLaFIol6Ii4AqWiigTdwooooA//9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

