Question: In the image on the left, the model is barefoot for certain.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/3d/43/1f/3d431ffa81ac8f5f2eb6395050bf1c62--bed-heads-mom-day.jpg

Right image URL: https://i.pinimg.com/736x/58/64/54/586454d1f7509c5249e56533da3c541f--coffee-in-bed-a-love.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In the image on the left, the model is barefoot for certain.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In the image on the left, the model is barefoot for certain.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

