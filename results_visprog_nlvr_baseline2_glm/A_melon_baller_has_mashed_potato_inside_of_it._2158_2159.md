Question: A melon baller has mashed potato inside of it.

Reference Answer: True

Left image URL: http://farm3.static.flickr.com/2434/3713289932_48a1abfa81_o.jpg

Right image URL: http://www.southernfatty.com/wp-content/uploads/2016/01/Fried-Mashed-Potato-Balls-2085.jpg

Original program:

```
Statement: A melon baller has mashed potato inside of it.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a melon baller in the image?')
ANSWER1=VQA(image=RIGHT,question='Is there a melon baller in the image?')
ANSWER2=VQA(image=LEFT,question='Is there mashed potato inside the melon baller?')
ANSWER3=VQA(image=RIGHT,question='Is there mashed potato inside the melon baller?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

