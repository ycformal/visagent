Question: Left image shows a forward-angled topless convertible with headlights that project upward and a hood that slopes downward, and right image shows a car with a top.

Reference Answer: False

Left image URL: https://68.media.tumblr.com/7f6896d22771c51088bb4fc79d1bbdb0/tumblr_nyouj0xs1h1qbw2r6o1_500.jpg

Right image URL: https://i.pinimg.com/736x/5a/e3/22/5ae3223706e4301ce3b737855768076b--wedding-cars-old-cars.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Left image shows a forward-angled topless convertible with headlights that project upward and a hood that slopes downward, and right image shows a car with a top.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Left image shows a forward-angled topless convertible with headlights that project upward and a hood that slopes downward, and right image shows a car with a top.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

