Question: An image shows one man crouched behind a downed long-horned animal, with a rifle in the scene.

Reference Answer: False

Left image URL: https://www.africahunting.com/attachments/p1000278_zpsqvhcairc-jpg.163288/

Right image URL: https://psearchery.files.wordpress.com/2012/09/himalayan-ibex.jpg

Original program:

```
Statement: An image shows one man crouched behind a downed long-horned animal, with a rifle in the scene.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a man crouched behind a downed long-horned animal?')
ANSWER1=VQA(image=RIGHT,question='Is there a man crouched behind a downed long-horned animal?')
ANSWER2=VQA(image=LEFT,question='Is there a rifle in the scene?')
ANSWER3=VQA(image=RIGHT,question='Is there a rifle in the scene?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows one man crouched behind a downed long-horned animal, with a rifle in the scene.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows one man crouched behind a downed long-horned animal, with a rifle in the scene.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

