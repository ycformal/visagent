Question: One image shows two pandas sitting on the ground, and the other image shows one panda on a narrow tree limb.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/77/c9/6d/77c96d3f9e719903fb2e49ae23bf3815.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/4b/15/35/4b1535f1dafb0c649e1c70c55c3f7ab0--animal-magnetism-hang-in-there.jpg

Original program:

```
Statement: One image shows two pandas sitting on the ground, and the other image shows one panda on a narrow tree limb.
Program:
ANSWER0=VQA(image=LEFT,question='How many pandas are sitting on the ground?')
ANSWER1=VQA(image=RIGHT,question='How many pandas are sitting on the ground?')
ANSWER2=VQA(image=LEFT,question='Is there a panda on a narrow tree limb?')
ANSWER3=VQA(image=RIGHT,question='Is there a panda on a narrow tree limb?')
ANSWER4=EVAL(expr='{ANSWER0} == 2 and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} == 1 and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows two pandas sitting on the ground, and the other image shows one panda on a narrow tree limb.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows two pandas sitting on the ground, and the other image shows one panda on a narrow tree limb.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

