Question: There are four desserts in the foreground, three in one image and one in the other.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/2c/62/c3/2c62c3a1165eb591fb209aaadef9925f--summer-pudding-berry-trifle.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/0b/f0/78/34/summer-pudding-trifle.jpg

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

