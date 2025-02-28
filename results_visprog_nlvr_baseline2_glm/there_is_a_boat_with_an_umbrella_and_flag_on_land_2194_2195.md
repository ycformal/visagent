Question: there is a boat with an umbrella and flag on land

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/c9/c4/41/c9c441e8e265cf82c6db40aaeb9e6cdf.jpg

Right image URL: http://2.bp.blogspot.com/_h0fJxJvtYDc/TUVdNHfUH5I/AAAAAAAACMw/tHW1qwafz8s/s1600/IMG_0043.JPG

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
ANSWER0=VQA(image=IMAGE,question="Is 'there is a boat with an umbrella and flag on land' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'there is a boat with an umbrella and flag on land' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

