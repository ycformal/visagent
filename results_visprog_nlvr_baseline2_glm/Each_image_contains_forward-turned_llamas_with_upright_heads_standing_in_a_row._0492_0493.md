Question: Each image contains forward-turned llamas with upright heads standing in a row.

Reference Answer: True

Left image URL: http://3.bp.blogspot.com/_9py6IgNlFak/TJOFf8h2kXI/AAAAAAAAAoE/94Tb8oMFy4g/s1600/llama.jpg

Right image URL: http://www.llamatrekking.co.uk/wp-content/uploads/2013/04/Aviary-Photo_130125019190623322.png

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains forward-turned llamas with upright heads standing in a row.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains forward-turned llamas with upright heads standing in a row.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

