Question: An image contains a single chimp, which is eating something nut-like and holding more food in its hand.

Reference Answer: True

Left image URL: http://i.dailymail.co.uk/i/pix/2013/02/20/article-2281527-17EAE611000005DC-614_634x541.jpg

Right image URL: https://i.ytimg.com/vi/ZlVICsSIASc/maxresdefault.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'An image contains a single chimp, which is eating something nut-like and holding more food in its hand.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image contains a single chimp, which is eating something nut-like and holding more food in its hand.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

