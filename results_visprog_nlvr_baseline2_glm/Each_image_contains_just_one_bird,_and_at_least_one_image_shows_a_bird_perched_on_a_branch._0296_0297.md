Question: Each image contains just one bird, and at least one image shows a bird perched on a branch.

Reference Answer: True

Left image URL: https://st2.depositphotos.com/3759125/5292/i/950/depositphotos_52925935-stock-photo-bright-rainbow-lorikeet-parrot.jpg

Right image URL: http://www.peterfuller.com.au/birds/essays/lorikeets/lorikeethybrid_sm.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains just one bird, and at least one image shows a bird perched on a branch.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains just one bird, and at least one image shows a bird perched on a branch.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

