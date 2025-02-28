Question: Fingers are touching the keyboards in both images.

Reference Answer: False

Left image URL: http://www.techaddiction.ca/images/internet-addiction-laptop-.jpg

Right image URL: https://www.industry.nsw.gov.au/__data/assets/image/0005/67028/varieties/thumbnail_two.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Fingers are touching the keyboards in both images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Fingers are touching the keyboards in both images.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

