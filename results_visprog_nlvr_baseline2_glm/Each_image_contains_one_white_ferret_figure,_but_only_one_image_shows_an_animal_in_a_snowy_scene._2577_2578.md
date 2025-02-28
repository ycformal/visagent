Question: Each image contains one white ferret figure, but only one image shows an animal in a snowy scene.

Reference Answer: False

Left image URL: https://bloximages.chicago2.vip.townnews.com/beatricedailysun.com/content/tncms/assets/v3/editorial/e/9e/e9ee34b5-2f3f-5808-99da-011d8c540eb2/51f077af52bd0.image.jpg

Right image URL: https://www.wish.hr/wp-content/uploads/2013/12/tvor_1.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains one white ferret figure, but only one image shows an animal in a snowy scene.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains one white ferret figure, but only one image shows an animal in a snowy scene.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

