Question: At least one sail boat is sitting in the sand next to the water.

Reference Answer: True

Left image URL: https://antoniodiasdesign.files.wordpress.com/2010/12/beach-point-18-woodwind-profile1.jpg?w=700

Right image URL: https://s-media-cache-ak0.pinimg.com/236x/72/a0/87/72a0871fec8f8d1e199011f7ac70236c.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'At least one sail boat is sitting in the sand next to the water.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one sail boat is sitting in the sand next to the water.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

