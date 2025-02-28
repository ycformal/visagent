Question: At least one image features an upright towel holder designed with an animal shape.

Reference Answer: False

Left image URL: https://img0.etsystatic.com/105/0/9384327/il_570xN.880536088_9mvw.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/9b/58/1a/9b581a7256f20872053ad156f53f1c73.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least one image features an upright towel holder designed with an animal shape.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one image features an upright towel holder designed with an animal shape.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

