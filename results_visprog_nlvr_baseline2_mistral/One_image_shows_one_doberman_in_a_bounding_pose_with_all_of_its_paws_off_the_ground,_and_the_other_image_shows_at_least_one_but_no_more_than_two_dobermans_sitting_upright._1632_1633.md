Question: One image shows one doberman in a bounding pose with all of its paws off the ground, and the other image shows at least one but no more than two dobermans sitting upright.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/b5/e7/5c/b5e75c345e38c67e87e6a559e7ffb1dd--doberman-love-doberman-pinscher.jpg

Right image URL: https://i.pinimg.com/736x/96/76/4c/96764cdf139e19221aab5dbed7b7c1b3--doberman-pinscher-puppy-year-.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many dobermans are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many dobermans are in the image?')
ANSWER2=VQA(image=LEFT,question='Is the doberman in a bounding pose with all of its paws off the ground?')
ANSWER3=VQA(image=RIGHT,question='Is the doberman in a bounding pose with all of its paws off the ground?')
ANSWER4=VQA(image=LEFT,question='Is the doberman sitting upright?')
ANSWER5=VQA(image=RIGHT,question='Is the doberman sitting upright?')
ANSWER6=EVAL(expr='{ANSWER0} == 1 and {ANSWER2}')
ANSWER7=EVAL(expr='{ANSWER1} >= 1 and {ANSWER1} <= 2 and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows one doberman in a bounding pose with all of its paws off the ground, and the other image shows at least one but no more than two dobermans sitting upright.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows one doberman in a bounding pose with all of its paws off the ground, and the other image shows at least one but no more than two dobermans sitting upright.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

