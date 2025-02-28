Question: In one of the images, there is a man with at least one dog.

Reference Answer: True

Left image URL: http://www.milkandhoneyfarm.com/dogs/whois/asher_great_pyr_side3.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/c3/a0/b5/c3a0b52da59e02381cb5d5e0c49ab3e8.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In one of the images, there is a man with at least one dog.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one of the images, there is a man with at least one dog.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

