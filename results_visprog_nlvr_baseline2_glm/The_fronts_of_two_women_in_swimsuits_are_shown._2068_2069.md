Question: The fronts of two women in swimsuits are shown.

Reference Answer: True

Left image URL: https://qph.fs.quoracdn.net/main-qimg-ba9443ee2e471a77b7501614f123cd4b

Right image URL: https://hitchfit.com/wp-content/uploads/2013/12/Sonya-Front-Shot-790x1024.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The fronts of two women in swimsuits are shown.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The fronts of two women in swimsuits are shown.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

