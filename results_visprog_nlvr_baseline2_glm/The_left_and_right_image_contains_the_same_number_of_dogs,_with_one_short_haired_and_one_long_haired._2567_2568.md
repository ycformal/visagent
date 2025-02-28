Question: The left and right image contains the same number of dogs, with one short haired and one long haired.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/93/c4/d4/93c4d4ee7d7c13cda0d823b4e7bbe255--vizsla-dog-argo.jpg

Right image URL: https://3.bp.blogspot.com/-5oZpuEqDKhk/VtHWrUI54vI/AAAAAAAAFt4/tgJ2pNzuZvo/s1600/11206649_1602779836628439_7350629888648364891_o.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same number of dogs, with one short haired and one long haired.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same number of dogs, with one short haired and one long haired.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

