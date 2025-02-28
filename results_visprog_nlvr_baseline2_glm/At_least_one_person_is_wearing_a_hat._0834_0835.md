Question: At least one person is wearing a hat.

Reference Answer: False

Left image URL: http://www.gentlegiantsrescue-great-pyrenees.com/Images2/Princess%20Leah%20and%20family%201%20cropped%20452%20arrow.jpg

Right image URL: http://img.photobucket.com/albums/v672/WJTH05/Great%20Pyrenees/HannahAndKeeper.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'At least one person is wearing a hat.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one person is wearing a hat.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

