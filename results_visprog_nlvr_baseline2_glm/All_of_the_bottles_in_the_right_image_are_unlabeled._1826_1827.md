Question: All of the bottles in the right image are unlabeled.

Reference Answer: False

Left image URL: https://i.pinimg.com/564x/7a/02/e2/7a02e2c191710fa728af2540b96e4bbf--fine-art-gallery-hyperrealism.jpg

Right image URL: https://i.pinimg.com/736x/c3/c6/d1/c3c6d18bc9c62ee1dceab1533706b0b9--pop-bottles-still-life-art.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All of the bottles in the right image are unlabeled.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All of the bottles in the right image are unlabeled.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

