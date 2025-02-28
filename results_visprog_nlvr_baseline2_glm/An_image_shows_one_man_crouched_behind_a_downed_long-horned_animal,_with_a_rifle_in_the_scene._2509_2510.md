Question: An image shows one man crouched behind a downed long-horned animal, with a rifle in the scene.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/cd/c1/37/cdc137a00b11aa0e6f38c5036edad343.jpg

Right image URL: https://3.bp.blogspot.com/-Ww_KeyWkbwM/UX0qED3YsGI/AAAAAAAAAsA/wQ3YcgR5vqM/s1600/400px-Capra_ibex.jpg

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

