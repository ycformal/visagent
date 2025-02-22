Question: An image shows a trio of side-by-side rectangular dispensers, each filled with a colored substance, but none containing a lavender substance.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/2b/c3/a4/2bc3a463a2ccc7d88d03e0732f038fda--shower-accessories-soap-dispenser.jpg

Right image URL: https://i.ebayimg.com/thumbs/images/g/86UAAOSwlQ9Zohnh/s-l225.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Does the image show a trio of side-by-side rectangular dispensers?')
ANSWER1=VQA(image=RIGHT,question='Does the image show a trio of side-by-side rectangular dispensers?')
ANSWER2=VQA(image=LEFT,question='Are the dispensers filled with a colored substance?')
ANSWER3=VQA(image=RIGHT,question='Are the dispensers filled with a colored substance?')
ANSWER4=VQA(image=LEFT,question='Does any of the dispensers contain a lavender substance?')
ANSWER5=VQA(image=RIGHT,question='Does any of the dispensers contain a lavender substance?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and not {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and not {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSW
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

