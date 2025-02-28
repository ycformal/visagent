Question: In one image, there's a jellyfish moving to the right.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/7f/a7/16/7fa716c2b206dc5d1dc661118d156fee--white-lace-fried-eggs.jpg

Right image URL: https://i.pinimg.com/736x/9c/1c/52/9c1c5287a505c66b8645ad534130c3c7--cool-tattoos-jellyfish-tattoo.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In one image, there's a jellyfish moving to the right.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one image, there's a jellyfish moving to the right.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

