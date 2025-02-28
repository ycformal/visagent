Question: All of the dogs are standing up.

Reference Answer: False

Left image URL: https://retrieverman.files.wordpress.com/2011/10/long-haired-bassets.jpg

Right image URL: https://i.pinimg.com/236x/ff/8a/e4/ff8ae477ece09b344d37c3fed1d3d915--gene-long-hair.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All of the dogs are standing up.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All of the dogs are standing up.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

