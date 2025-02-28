Question: An image shows a trio of side-by-side rectangular dispensers, each filled with a colored substance, but none containing a lavender substance.

Reference Answer: False

Left image URL: https://static.petersofkensington.com.au/images/ProductImages/951848-Zoom.jpg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/41K5urydKlL._SL500_AC_SS350_.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Does the image show a trio of side-by-side rectangular dispensers?')
ANSWER1=VQA(image=RIGHT,question='Does the image show a trio of side-by-side rectangular dispensers?')
ANSWER2=VQA(image=LEFT,question='Are the dispensers filled with a colored substance?')
ANSWER3=VQA(image=RIGHT,question='Are the dispensers filled with a colored substance?')
ANSWER4=VQA(image=LEFT,question='Are none of the dispensers containing a lavender substance?')
ANSWER5=VQA(image=RIGHT,question='Are none of the dispensers containing a lavender substance?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows a trio of side-by-side rectangular dispensers, each filled with a colored substance, but none containing a lavender substance.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows a trio of side-by-side rectangular dispensers, each filled with a colored substance, but none containing a lavender substance.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

