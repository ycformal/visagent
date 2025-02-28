Question: An image shows multiple rectangular ends of boxes side-by-side, showing different colored makeups.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/15/96/a5/1596a57e827ca3e5003a6decedae7efe--kylie-jenner-kristen-lip-kit-kylie-jenner-lip-kits.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/4c/da/0e/4cda0e4c331f7eb6c730a827ad54d92c.jpg

Original program:

```
Statement: An image shows multiple rectangular ends of boxes side-by-side, showing different colored makeups.
Program:
ANSWER0=VQA(image=LEFT,question='Are there multiple rectangular ends of boxes side-by-side?')
ANSWER1=VQA(image=RIGHT,question='Are there multiple rectangular ends of boxes side-by-side?')
ANSWER2=VQA(image=LEFT,question='Are the boxes showing different colored makeups?')
ANSWER3=VQA(image=RIGHT,question='Are the boxes showing different colored makeups?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows multiple rectangular ends of boxes side-by-side, showing different colored makeups.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows multiple rectangular ends of boxes side-by-side, showing different colored makeups.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

