Question: One image depicts two overlapping oranges without leaves, and the other image features some type of vessel next to at least one intact orange.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/a7/2b/6c/a72b6c2abf7c09c6dbf3fb40177b8abd--fruit-art-art-auction.jpg

Right image URL: https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/two-oranges-pepe-romero.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image depicts two overlapping oranges without leaves, and the other image features some type of vessel next to at least one intact orange.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image depicts two overlapping oranges without leaves, and the other image features some type of vessel next to at least one intact orange.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

