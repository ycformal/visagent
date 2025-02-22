Question: The image on the right shows some of the trees surrounding the yurt.

Reference Answer: False

Left image URL: https://howardmeyerson.files.wordpress.com/2015/01/084-craig-lake-yurt-m.jpg

Right image URL: http://media.mlive.com/muskegonchronicle/photo/12514938-large.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image show some of the trees surrounding the yurt?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image show some of the trees surrounding the yurt?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABCAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDyiC7+ceTEXNdBY2uo3nDTJbR98daxbFzEnyeWOwycV01lpUlzFbz6jeYtpGwIY/lGfc9+orByi9LmsU97Fuz02yaXyrK3k1S87u5/dofUnpWkdIdpvImZLy6jGTCnyW9sPVz/AE61q6TFJeQ/ZdNT7Dp0eRLd7drPjqIwenux/CteO2sjp6+VAU0xWAhiH3ryQ9Cc8lSfXr1PFZygbRkck2jJOu4neHXJkZcbkH8W3+FB0Vf4jXU6L4s17w6os5V/tOBUCxpNJh4sdt38QHIz/snrTmQwySFyskwZWkI6NL/Ag/2VzmqLFS0jg5AEgVvUINgP4s7mslzRd0aO0lZmrqvxJ1q6tDFZaRFZyv8AL508ocJzjIA/rXnkllLLdS3FxIZ7qdg8skpx5jE8ZP8ADkggH+FgQeDXTXoImjBjdofMkEwBAwgdlJ9+H6f4VWkt5WJRo1kmBcBT0kYcSxn/AHgA49+aKjlLdigox2RhsPLVpCZAqttaULh4m/uyr/7MOtZ95DGBvuIVCtytxbng/XFb8se54pIJf3zJ/o079JkHWKQf3h0z1/WsWUFTI1mnlSKf31k/QH/Z9P5GlFBJmNNFOi7oLhZk7B+tY9zcMMiWBlIPUcitiSKO5ffBut5C+0qwxg+mP8KXxDpyaRfx2TXDTSNGrcpgknsMVvFpGMlc5hp4ichhRS3BhjndJFw6nDAryDRWvMZ2OitbOVPD0dsktmkkczymRnJXBHQY710OpyPB4asUVYJpBsYrIxVGJx37dK4rwtdGGcqTvSVtkkJHBHr+FehpaNe39taxJGRGu7Eh+VcDg47844rmnzxmk9TaPK43Q3S9UDWFtvMlul1OYTZzu0sTEFcfOv3VJJHOQcYruHt9UuV+3wJ51wu+KCyI2OpXG5lDY39RyOi9ua4HUvDetWMc1+bmKQJh3Ns7IVHrt6YFXfD3j2/0xY4byK2vrVgQUlwjKOMnI4GR7c1anrZqwnHTQ07nU2tC8bBxJaKWYOCGaZumR+J/MUkVwFR4gciOOKDPqS2Wqpq/iGHXblrgRzf61MrOQx/iPBHbpz6LUrpa2sU9xOJFhR/NcoOSAoPy59e31WpupXSNLNK7LzSrJNtbG15p4j9GGf6VCZGniQhtssqBlP8Admj4z+IH6GpHhgbDR+YVM6yAEYIyoOD9M4NMe02FEWIh2nDpvzjDdG4529elS0NGZfSwCNpJcpa3OXYZwYZR1I9On5j3rm9Ruria3NxFD5l1bzralkU7mZlJGQO2Bk5710epabdXs18NO0n7VEkjxPIZgkb7gFYLzkj5l+hIrn9cstattPELQCK/uLpgyWZyFQAD5iO+T39KUbrUHYqX+nKPFwMN6hsobhRACxZ5emefrmjx55KeMheSSgPEqYj9gTW/4guI7b4g6ZpwtYTbWy28PzIAVkHO4H8vrmuW+I0Bk8Uli3WJevbr+laRu5JMzla1zl70wXV7NcGQgyMWIAoqiUO4gAnBx0orpS8zBtdjW0SYW1wHwQxb5uMjGf8AGvRP7Zh0fVPtE5yAmwc9+tefeVa20kIuftO6RVkXa4PXBGa3/FV3HBfN/o6XA3gKpPA+Uc1zz96cTWOkWdk3j6wngmii3NLKhjAUFuSMdvrXL2sipcQRzGJDH93eSCPTII55JqpeafNf6bpb2vk248gyXD5CKmTwp+g/GqKLo1pIE3z6tcA/6uH5Is+7Hr+ArRcjV29Re8nbod5ZR28YitwgQi53MzMCoBXgk9uB/OrGq6be6zaPbafeQRIXDyuz5RkxjggdM4/T0rlEvZ5IVYrFBKkhPlRLlQNoABz1IA710ngK6mOr3KSn5NihVwAB15AFYNuEXKxqrSfLch0abU7AXtlqhaW4t7oLgNkY2ZBBxyppza+srI1jcweZHJ5sxlfeYo1HYAjvgAcDJrJ8VXLxeL9Q8qWXy5Cm5VYY+6BnrWNaw2VnNNMC2Xj8raR8pGQcZ7dO9Ve8eawtny3PSIfF2m20GDHsLXBmcIRhcnOMY92z65X0rJu5YtZ+IVogkXCyIrQM2HAB3fjgYrm7IRBo7m1ndbeJwZoh/Bz0ZeqZ9RlfpV/S5I7bxI+qzNOlyYXIVsEfMQN0bDg4z061nLltv0KV+wuoF9R8ZX15GNsFvd4d24VUTGBn14rH8aSCbWzKpI82BNwI5VfX9ava1dJPJDbWElta2MUu+RJZP3kzZySfrXP+I5ptU1R7qOaBFKhQnmZPFXB+8mTLRGCN6MyooI3UU8QzrwJYcezUV0XRjqap1HRbooZLa5adQqRktwPTPNWtQ1KW0n8yGGOaVyQpkXdsOByB61iW1updSAMg5rYwrSB2OSOgFZySuiovQgFtf6q4k1G6kcdRHnj8ulacUCWw8i2Xa4GWKjJQf1P/AOun27KmCAM/yqwllp7vue1QsxySSeT69anm11HbTQrz6fJOqIhKKnbsfr6/WpIYdTsVkNhcpE8oALwkxtgH6VpJp+lsAPscRJOOp6fnVpdP0gBCbCDlu4odWO1hKi73uc/c217dXRln8lnKqGkkJcnAAyeOTxVVbQW87MbiM7hgrwFP4V1hstKzj+z7bAyMeWKrtb2ABAtbdex/dD/CkqytZIPYu92zkpZjY3C3VpdrFLH91lcEj2x/EvqD+taVlq9vdSopAtbgsC0CDMM3un90+3Sr8iwKSBDGpHpGPz6VnzQp9ojuEQbozngVM3Ga2NIpx6mXqFp9o1QXIfBVl+Qj096pzKq6qbsNlS+cY9qfqsMkl4zo5XPXBrMeKdeshP41rBXS16Gc3q9BJIsyMQy4JJoqIh88k0VvqZ6djVtz8oq5AeaKKzZSNCL7lX7fox+lFFYyNEXh/rV/3al/gSiisjQQE+aef4jUL/fb/PaiigCpN95f901TJO4c0UVSJZQv+qnuRWQ/3jRRW0TKRWPWiiitkSf/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image show some of the trees surrounding the yurt?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

