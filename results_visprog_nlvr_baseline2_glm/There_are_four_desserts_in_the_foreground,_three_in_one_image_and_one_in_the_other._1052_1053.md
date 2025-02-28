Question: There are four desserts in the foreground, three in one image and one in the other.

Reference Answer: False

Left image URL: http://img.taste.com.au/8Vy2vc75/taste/2016/12/raspberry-vanilla-and-mascarpone-trifle_digiapi_1980x1320-119106-1.jpg

Right image URL: https://i2.wp.com/celebratingsweets.com/wp-content/uploads/2015/06/Berries-Cream-Trifle-2.jpg?resize=600%2C900

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are four desserts in the foreground, three in one image and one in the other.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are four desserts in the foreground, three in one image and one in the other.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

