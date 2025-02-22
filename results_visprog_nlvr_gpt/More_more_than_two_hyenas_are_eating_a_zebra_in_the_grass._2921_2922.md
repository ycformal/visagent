Question: More more than two hyenas are eating a zebra in the grass.

Reference Answer: False

Left image URL: http://4.bp.blogspot.com/-yPjHQcH8CDg/UGbQxxdA-4I/AAAAAAAABAU/SvJxVvv4UiA/s1600/DSCN1213.JPG

Right image URL: https://i.ytimg.com/vi/JJVQ0D_kUJM/maxresdefault.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='How many hyenas are eating a zebra in the grass?')
ANSWER1=VQA(image=RIGHT,question='How many hyenas are eating a zebra in the grass?')
ANSWER2=EVAL(expr='{ANSWER0} > 2 or {ANSWER1} > 2')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: '>' not supported between instances of 'str' and 'int'

