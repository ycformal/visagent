Question: In one of the pictures there is a white dog, a brown dog, and a black dog next to each other, and in the other picture there is at least one black dog.

Reference Answer: False

Left image URL: http://buzzsharer.com/wp-content/uploads/2015/06/labradors-puppies-pics.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/2a/75/f3/2a75f3345f3d96fe38c2b25b8aa44853.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many white dogs are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many white dogs are in the image?')
ANSWER2=VQA(image=LEFT,question='How many brown dogs are in the image?')
ANSWER3=VQA(image=RIGHT,question='How many brown dogs are in the image?')
ANSWER4=VQA(image=LEFT,question='How many black dogs are in the image?')
ANSWER5=VQA(image=RIGHT,question='How many black dogs are in the image?')
ANSWER6=EVAL(expr='{ANSWER0} == 1 and {ANSWER2} == 1 and {ANSWER4} == 1')
ANSWER7=EVAL(expr='{ANSWER1} == 1 and {ANSWER3} == 1 and {ANSWER5} == 1')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
ANSWER9=
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In one of the pictures there is a white dog, a brown dog, and a black dog next to each other, and in the other picture there is at least one black dog.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one of the pictures there is a white dog, a brown dog, and a black dog next to each other, and in the other picture there is at least one black dog.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

