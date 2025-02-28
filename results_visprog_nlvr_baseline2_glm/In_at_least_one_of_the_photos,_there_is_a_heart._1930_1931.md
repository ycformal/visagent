Question: In at least one of the photos, there is a heart.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/69/65/6d/69656d72e87f0410d5887551f5452174--canda-padlocks.jpg

Right image URL: https://i.pinimg.com/736x/38/36/3e/38363e208de700edfba58ddcce82ff75--canda-padlocks.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one of the photos, there is a heart.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one of the photos, there is a heart.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

