Question: At most 2 upright trumpet vases shown.

Reference Answer: True

Left image URL: https://img1.etsystatic.com/033/0/6357465/il_340x270.567377193_rt8a.jpg

Right image URL: http://www.antiques.com/vendor_item_images/ori_1127_277718916_1137490_8306_cobalt_blue_cornucopia_mantel_vases_8.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>vase</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>vase</span></b></div><hr>

Answer: vase

