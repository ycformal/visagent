Question: Both staircases have vertical post designed railings.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/57/32/4e/57324e6bbecd915e2b047ed7ccfdd46f.jpg

Right image URL: https://st.hzcdn.com/simgs/fb02834b077ef9c8_8-9280/home-design.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Both staircases have vertical post designed railings.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both staircases have vertical post designed railings.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

