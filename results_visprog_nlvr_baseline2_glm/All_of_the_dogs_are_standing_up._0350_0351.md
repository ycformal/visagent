Question: All of the dogs are standing up.

Reference Answer: False

Left image URL: http://buzzsharer.com/wp-content/uploads/2016/04/basset-hound-picture.jpg

Right image URL: http://www.bhcsc.com/basset-hound-standard/images/disqualifications/shape_pic-41.png

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
ANSWER0=VQA(image=IMAGE,question="Is 'All of the dogs are standing up.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All of the dogs are standing up.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

