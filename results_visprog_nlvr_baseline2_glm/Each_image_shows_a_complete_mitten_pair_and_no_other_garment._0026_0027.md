Question: Each image shows a complete mitten pair and no other garment.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/0e/8c/66/0e8c66f63ca99664a9f14a6de36682d6.jpg

Right image URL: http://knitty.com/ISSUEsummer05/images/manlymittsBEAUTY.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows a complete mitten pair and no other garment.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows a complete mitten pair and no other garment.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

