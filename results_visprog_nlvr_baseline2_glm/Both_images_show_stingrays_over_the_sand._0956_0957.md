Question: Both images show stingrays over the sand.

Reference Answer: False

Left image URL: http://pellagofio.es/wp-content/uploads/2016/04/tiburon-martillo-4116-1.jpg

Right image URL: http://www.lacasadeloscoroneles.org/xtras/2015/05/fotosTIBURONES01-620x413.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Both images show stingrays over the sand.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAjAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDjY3q1HMBWOs52nBGe2adBe+ZkMrIy9Qen519h7WKdmz5GVBtXN6OcetWkmGOtYEdyp6MD+NWFuigz1rRTVrnJPDs3lkqUTMB1rLhmLjKBmwMnAzirCzAjrVaM5J0Wt0cb4z3Pran/AKYL/M1gCM7N2CR644rofFBD6yhwSPKXp9TTIrVryBI47aQI2VUg5A55/nXmYrGShJxTskfU4OUlh4JLoYQyB0FKGBHvW+NIiid43YAhcjPeqD26RfutpZmfCla4qePm37sjrejs0UQxHNWYJ8Ukto6ruCNjPPFQRKz7mRT8h+Yele1hM3qUpqM9iHyyjc2EnO0c0VnJP8tFfURxuHkr3OZ0dS0s/vU8N08P+rkZSTkkHGTWcuP7wH4UokIr4KNa+5pOjY6m28T3EZxcW1ndJ6SwjP5jmtFdW8MXCbptCvFn7LbXA2k/iOPyriVlqZJiCDmrSi/Iyaa8z0eLU/DGmOI59F1YXIALI12oCnqOR1rEudT+2XLzC3jt1JICoxJI9T71zhunlkMkjlnY5LE8mpluOOtdNGMYvmu7+pzVk5R5bK3oQau4k1QMf+eY/rWhpGpJYZWQExk7ht6hsfyrn9TuP9PBz/AP60xbzAxmvHxtpVJXPVwkeWlFI6e+1O1ulHliRn2gMQnf6msS6s5bq2dQ2xiMjBqqLwnvU8V2QeorjglFWR1Na3NTQ7k6vJa2anMzD99nooHXn3OPzqbxFok2ny/a7RT9lkXDggfKw9ceoqr4e32GoTS28iRknOJOm3qMH168fStnUNYaeylV04bkfNj8xiuuFaTSjJ3OadKKbkkcJkjIoqOWQtM5Hc9qK7FXdiuUnUmn0UVwwNpig08E0UV1QOOe5IpPrUysfWiiuiLOeRhay7C+GGI+Qf1rP82T++350UV5GIb9rI9agv3cQ86X/no350v2ib/nq/50UVgbD1vbpPu3Eo+jGnNqN44w11MR6FzRRTuxWRD5sn99vzoooo5n3CyP/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both images show stingrays over the sand.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

