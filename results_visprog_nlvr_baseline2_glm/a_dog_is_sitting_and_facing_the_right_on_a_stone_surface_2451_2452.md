Question: a dog is sitting and facing the right on a stone surface

Reference Answer: False

Left image URL: http://www.cutepuppies.net/sites/cutepuppies.net/files/imagecache/default/images/ozzy_5.jpg

Right image URL: https://www.cimformacion.com/blog/wp-content/uploads/cavalier-spaniel-obeso.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'a dog is sitting and facing the right on a stone surface' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'a dog is sitting and facing the right on a stone surface' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

