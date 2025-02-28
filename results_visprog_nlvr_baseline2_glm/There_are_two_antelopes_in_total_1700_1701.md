Question: There are two antelopes in total

Reference Answer: False

Left image URL: http://www.animalspot.net/wp-content/uploads/2012/01/Hartebeest.jpg

Right image URL: https://storage.cdn.bookyourhunt.com/originals/3f457b58-aad3-4146-baed-b564777f08b1/4ccd37f0-f447-4728-a438-60172ffd3014.png

Original program:

```
Statement: There are two antelopes in total
Program:
ANSWER0=VQA(image=LEFT,question='How many antelopes are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many antelopes are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 2')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are two antelopes in total' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two antelopes in total' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

