Question: In the left image, an adult holding a toddler is standing in frontof a wood rail fence extending a hand with something to eat for a llama on the other side of the fence.

Reference Answer: True

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/0a/be/93/87/feeding-the-llamas.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/564x/a6/62/9f/a6629fad53df5810563ae7fc0be17828.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In the left image, an adult holding a toddler is standing in frontof a wood rail fence extending a hand with something to eat for a llama on the other side of the fence.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAmAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD2lYbS5hEkFzFIjrlWVgQVPp7VnXMWmJcpam+t0uXHETyruP0HWvnnRLfzLUArIZS5GAxGBj2+tO1OGW0Es6RwTStIqK0mGZI1HHBHHPfOa0jWk5OMehn7OLV2eza7oLCA3SXsccaAsRIvp6GuEkk3SwwiRZCjPuKoAeQADx2IOfwNcwAzWoZri4cFckLMcE47Zqpez6zc2qlN1vDBEFW3gYp8g5ORnLd85/lQsU2xKkjtbae+VJ57K4BfAaZ8YwO3J46Gq1pr9zHrJgu717lHP+rbGVz0x/P8q8+OpwyQEXEs6sTgrG2Qc98E/pVu20+G4dLiO5mQ4DAsDn259fxoeJaY/Zq1i54jto18UamrNhvtDY47cViGMMp3ttIOMEckVvt4b1O5/wBLjWSVX5V8Eg/jVKfR9SJw+0MP9rmuWVS7vcVraXKsM8SlGjzEygqG3cjOc/zqoLJmfEkink4AbNdh4K8EXOp6g0+poE02MFZNw5lJH3V9++e1T6h4VtZPFVp/Z7KmmIcXTtKB5SqcHrznH1z1ovZbmlODclYydL0K0s7S4v8AU7pLWKN1iKyRMzZYZHA9atpqHhpJFjinvLhmwR5VsEH5nPpXY/ETQbS3+H4ntp2cNNERvOSQOB9ep5ryOxttRhnimCFYVIBOQARg4zWsdtTWp8TtsdoNQ0sj91p13Iv95rjafy4orlBdyY5lhBPYbaKeorIvwPcw3DfPCYGOSckEcdfyFYyapPaTSxTFpN3zBt3IzWmytMrp0BGP/wBVc/qlu8FyrFtwdRg/Tis6Et09zKx0KXTz2kUMjqY5FJILbFwR1J7fj0/OrtiLq0WOK1uJoZEbPlzAFgpPUDlX46Y61lacGjgt5JWJUIMFeHH0P+RWlL5RjW0Nv50bHdGinbvGclojzsYd4+R6cYrKUrsuJzOqWws9TuokO9Y5mQMe+PaptP1q/wBPI+y3Lxd8KxA/KpNbZZLiFEmaUheWYc89M++OOpqCKxDYLOB046ZrZNON2F7PQ9t0nWbybw3o8slw5mlhVmbP3jyT/KrcUqXEp+0RQTeYcZdFbn6kV5/PeS6Va6FCLpGW3hBliU5OMEY+tdB4e1eDVtSWKFvkQNuLdjjg/wA6xbLUlsdRcyOlpLa6eiCURYjVcKFJ/QdzXNQ+GdQS7DXUMBhQ5clwwP5c1Th8UW0q6lfS7xbxbY4+h5yVI69SefpViLxTYS3KW4uNzMpZtnRQBkk/lUSTYckW07jfFdhd61dT28aQW0IKOHLF3kAXt2UZ7e1cgbW1WEwm+k3EbSfs/wD9etSbxHJK1zPDDIArrDGu4Y285J/Gq2laXZ6vc4uJLmymlkIH3SpY88e1bq6WxreL+JmOPD+nLx/aF0fpbr/8VRWjNomrR3MsccDyojlRIo4YDuKKrml2HyUe5yA8QWxyDHOBnnaBz+tR32t21zGiLDICuTuYDPsOvSiiphFKRyk0fiC0jXAim4AHb/Gpo/Elj5bwzQ3JilwW243Kw6MpzwR+vQ0UVm4rcEZ11rSzXIkkDMy8FggXdg9SM9T3qaDXoYyCqyhxgjKqw4+tFFbNKwHTzahFfafp7rbiPECR8HGR7+/XmrmiXB0rUFvLbcGUYKk9RRRWD3Mb6lWaOJvtNpCg8i6m8xd/BQgkjp7cVWhthaXbbDlsNG2fcEH+dFFNNjTZN9taW3eDyIh5ZM5cDBJAxxVW3bbIjQkgRncM8Y5B/pRRVD55dy+yfb5ZLnz54y7ZKrI2P0NFFFF2bLY//9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In the left image, an adult holding a toddler is standing in frontof a wood rail fence extending a hand with something to eat for a llama on the other side of the fence.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

