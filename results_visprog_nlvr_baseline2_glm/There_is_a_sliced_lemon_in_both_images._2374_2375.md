Question: There is a sliced lemon in both images.

Reference Answer: True

Left image URL: http://i2.wp.com/www.largerfamilylife.com/wp-content/uploads/2013/11/Fotolia_54761966_XS.jpg?resize=420%2C286

Right image URL: http://images.wisegeek.com/group-of-lemons-together-against-white-background.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There is a sliced lemon in both images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAfAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD32kZlRSzEBR1JrJ1CfdO0e7BU8DOM1VMxdfJcyL7EdDXDPGfEoK7X5m8aN0mzRbWIBJtRHf36VbhnSdcrkEdQeorkYDLcTyYIVY3KF+uSDg49a1EZljKhnyATuPfHNeTgcxxk5ylXXu/d/wAH7zoq4aEVaL1N+lZgoyxwKy9JuGmTJJKtyuar63evHKIlVwoHLEcH6V6tXHRhQ9skcyov2nIaL6nbI2NxP0FWIp45kDo2QfXiuY0uRJ53ZxuEeOPUmr11OjyFDKVK8dOK4MPmVeUHUkk122/E2qUIRfKjS1C+WwtjL5bSt0WNSAT+dRQarHIQJEMefU5Arnr27kEkNuMySO4RUPv3+lWTdxxkRIqykfeY56+3tUxzKvVqNw0iu5Tw8IRXNq2b9xeJBxjcfrVaLWYXk2SKUz36isC9kfyPPjZgqsFdCc4z0I9qZ5uyzklKmQqpO1Rkn6VjXzXERrcq+7oXDC03DmZ2gORkdKKpaS0r6XA0qlWK52ntRX0dOfPBSta558lZtFPWLCWUieBd7dGQd/es+DT9TuYpAXktRtIXnLZ9h0rwn/hozxZ/0DtH/wC/Un/xdH/DRniz/oHaP/36k/8Ai64KuV0KtX2sr+l9P8zojipxhyo9ytLCaxtIreSGUvGoBZFyG9/xq9Lb3zwDyYV+fqGb5sV8/wD/AA0Z4s/6B2j/APfqT/4uj/hozxZ/0DtH/wC/Un/xdDy2DTjzO3lYHiZN3tqfR2mWklvHumwH6ADsKuzwR3ETRyKGU+tfNlj+0L4qub+3gfT9ICySqhIikzgkD+/X0uK7KWHhSp+yitDGU3KXMzkv7EudHe6lW78y3mxtjK4KH2P0pqMbgLIBulHDxn+L3FdTdW0d3btDJnaw6g4I9xWEvhidJAf7UZkH96EbvzB/pXmYnBVIzTw6Vux0060JRtUepWRYUK3NxiNo/kjkfjGeKh8i6iZtkbkn5cheG/8ArVvPoNlPGq3Qa429DI3Soj4atBIGjuLuJf8Anmkvy/kRVfUqiirJX9f+AL2sHuzPWwkns5rVGQzSEEkDIXHTNT2GgXUbD7XNEUH8Meefzrct7aK1j2RLgevc1NW1PLqWkqqvL8CJYiSuovQQAKAAMAcAUUtFeic5/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a sliced lemon in both images.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

