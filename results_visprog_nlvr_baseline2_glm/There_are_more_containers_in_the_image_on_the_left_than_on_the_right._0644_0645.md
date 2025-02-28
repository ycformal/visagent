Question: There are more containers in the image on the left than on the right.

Reference Answer: True

Left image URL: https://s2.thcdn.com/productimg/0/600/600/77/10026477-1277464755-752000.jpg

Right image URL: https://i.pinimg.com/736x/45/b3/eb/45b3eba274a5f13a27e5d293c091965d--stella-perfume-parfumerie.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are more containers in the image on the left than on the right.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are more containers in the image on the left than on the right.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

