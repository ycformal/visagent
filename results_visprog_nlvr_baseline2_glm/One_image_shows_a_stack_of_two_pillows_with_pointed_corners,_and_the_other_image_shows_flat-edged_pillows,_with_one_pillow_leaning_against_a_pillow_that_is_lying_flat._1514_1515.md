Question: One image shows a stack of two pillows with pointed corners, and the other image shows flat-edged pillows, with one pillow leaning against a pillow that is lying flat.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/71sAACnwdyL._SX355_.jpg

Right image URL: https://sc01.alicdn.com/kf/HTB1e18WLXXXXXagXFXXq6xXFXXXd/QUILTED-MICROFIBER-PILLOW-100-DOWN-AND-FEATHER.jpg_350x350.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a stack of two pillows with pointed corners, and the other image shows flat-edged pillows, with one pillow leaning against a pillow that is lying flat.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAsAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDw9JCn3icDgk1ZS6iAxvX869j+D/hrU7fS9TutRtDa2d95Rt/PQZkC7skKeccjk8GvQ20/TbI7otPtWlP/AC0aFM/yokuo4s+a7LRNW1gbtO0m8ul/vxwsV/766frWu3w+8XYOdHwB13XEY/8AZq94mnkZcyOdo6DsPpVFCbiQGTiPPyoOrf8A1qzuaXPne507ULG4lt7iyuA8TFG2xswyPQgYI96ltNG1bUDi00u9m4zlYGx+eK+kNsxHDED61WljuVR3Vg7BG2gNyTg4HPvTTEzj/h9E3/CCiQ3AVQ837sJlvvV2NpptwFjMAuHGMhpiIkH4YLGuA8C65ceF449J1iwa2dWYs0g+dCxzn/d9xXrtrfQXGxVlQu6llG4ZYdyPUciumEUzJsdFa3LDMlxCh9I4yf5mphZKf9ZeTn2Xav8AIVVur2O2BDMB7Vi3OsSM21HIHOa05ETc3pNLiMgZNWv4ABjYjptPvyppVsJwcQ+Ips+ksMb/AMgK5Vr+Vl5kPPHWmRXL53M5496PZoLnUPaeJ1bEOq6TInZpIGU/kCaK5xr+dDtSY4+tFL2Y7l5NRlml3SOTn1qa8uF8tWHIAyTXKKL2MZ2Qn/dbB/lRJfajsKG2jYHs0hx+grGVmrDWhp317HbwPPcsFijGT/h/n6VLpUonthdsP9ZyPYelcZq+m3+ssjXt0USM5SGIbUB9ff8AGtayvPItI4LrKGMY3gMVf3x2NYuKsWpanSTXqKSDIo/Gs64voxz5nPtVL7XBIP3aTyD1VCq/0qBzO/8AqbSNB/ekOf5UJIbZnTaTd61rck1pbmQYUb24UYHcmuq0bwlNp94l/JdRvdJGUjxHkID1AJ7fhWbZaZqPkXE6a0bR5VKoEiBRCP4sMetdBperbES1urlJ7pFG+RBgSf7QH+FdULWMmZmpPNBOTfeZvPcISD9MVQF5Cx+VZD9UNdzKkN3CVkUEH1rlL+xSCYiMHFaaiKouARwjUvmt2T9ahd0hxv4zWfe6/p+npvuZhGucZYd6TaCxreY/otFcv/wnuiZIEkzY7iI4opc0e4+Vnl3/AAmvib/oOX3/AH+NIfGniU9dcvv+/wAawqK57so2z4v8RE5Os3v/AH9NIPF3iEHP9sXn/f01i0UgNw+MfEZ661e/9/TR/wAJj4j/AOg1e/8Af01h0UAe5eB7m51Xwpb3N7cPPMZZAZJWycA1vz2QcZDsAOmDgj6HtXPfDRQfBcGf+ekv/oVdUWOwDNbx2JYlnq2o6YdsiG9hHYkCQD69D+NcZ4m8c3yTyLZ2E6HJ+aY4x+ArsXRcA4yaz7yyt7gEyxKxHfvTd7WBM8nn1fXtTc79Qn552oxUfpUZhumTbdSSOD2diQfx/wAa9A1LS7OOzeWKFY2Xn5eM1xd47FnXPA6VyzunZnRCzVyO10+KSHPmlcHGOKKpTyFSnA5UE5oqdStD/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a stack of two pillows with pointed corners, and the other image shows flat-edged pillows, with one pillow leaning against a pillow that is lying flat.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

