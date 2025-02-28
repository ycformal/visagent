Question: In the left image, the cocker spaniel is clearly outside; you don't have to guess.

Reference Answer: True

Left image URL: https://cavaliersbycrumley.files.wordpress.com/2011/08/blake-1.jpg

Right image URL: https://images.fineartamerica.com/images-medium-large-5/cavalier-king-charles-spaniel-dog-lying-john-daniels.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In the left image, the cocker spaniel is clearly outside; you don't have to guess.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In the left image, the cocker spaniel is clearly outside; you don't have to guess.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

