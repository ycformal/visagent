Question: Two dogs are standing in the grass with their tails up.

Reference Answer: False

Left image URL: https://i.pinimg.com/originals/f4/ba/f2/f4baf2968f3ea01cc37faf5aa959c06e.jpg

Right image URL: http://2.bp.blogspot.com/-4iss77a4aD8/UMYanKUvCOI/AAAAAAAAAgo/5FAIq5lHTKY/s1600/border_terrier.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Two dogs are standing in the grass with their tails up.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Two dogs are standing in the grass with their tails up.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

