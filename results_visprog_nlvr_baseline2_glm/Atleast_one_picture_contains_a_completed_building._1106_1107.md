Question: Atleast one picture contains a completed building.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/98/e7/72/98e772d8db4d9a6728960e49a43dc1b7--yurts-sustainable-living.jpg

Right image URL: https://bdn-data.s3.amazonaws.com/uploads/2016/06/13021061_H17825481-600x394.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Atleast one picture contains a completed building.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Atleast one picture contains a completed building.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

