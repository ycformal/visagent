Question: Each image shows one vase with an open top, a short base, a tear-drop shape, and no handles.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/7c/f2/96/7cf2962c8e7205b73366df544c7d955e--antique-vases-roof-tiles.jpg

Right image URL: http://www.christies.com/lotfinderimages/D57196/a_rare_doucai_pear-shaped_bottle_vase_yuhuchunping_kangxi_yongzheng_pe_d5719627g.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows one vase with an open top, a short base, a tear-drop shape, and no handles.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows one vase with an open top, a short base, a tear-drop shape, and no handles.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

