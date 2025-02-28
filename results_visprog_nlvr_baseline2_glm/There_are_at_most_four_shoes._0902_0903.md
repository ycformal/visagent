Question: There are at most four shoes.

Reference Answer: True

Left image URL: http://2.bp.blogspot.com/-7yVJ3DlDDtg/URNPNaNm14I/AAAAAAAAXrw/vizeK7iqmYA/s1600/DSC03373.JPG

Right image URL: https://s.kaskus.id/images/2014/06/09/262510_20140609104122.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are at most four shoes.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are at most four shoes.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

