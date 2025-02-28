Question: There are no humans visible in either image.

Reference Answer: False

Left image URL: http://i.dailymail.co.uk/i/pix/2010/03/09/article-1256559-089F44C4000005DC-646_634x422.jpg

Right image URL: http://www.kidsdiscover.com/wp-content/uploads/2013/02/2.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are no humans visible in either image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are no humans visible in either image.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

