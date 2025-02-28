Question: The dog on the left has a smiling face, and the dog on the right is baring its teeth.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/75/19/dc/7519dc48c8b7bf11880f11fd8d5ce002--my-favorite-things-humor-memes.jpg

Right image URL: https://i.ytimg.com/vi/b5o2_9zFIUs/maxresdefault.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The dog on the left has a smiling face, and the dog on the right is baring its teeth.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The dog on the left has a smiling face, and the dog on the right is baring its teeth.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

