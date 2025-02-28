Question: There are crabs inside an enclosed cage.

Reference Answer: True

Left image URL: http://www.ilovecrabs.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/_/2/_2_hardshell_jimmies.jpg

Right image URL: http://www.crab-o-licious.com/images/xcrab-pot-full-crabolicious.jpg.pagespeed.ic.2JuGS9Fwik.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are crabs inside an enclosed cage.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are crabs inside an enclosed cage.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

