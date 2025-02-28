Question: The left image is absolutely full of balloons, the right image has balloons and sky.

Reference Answer: True

Left image URL: http://sfwallpaper.com/images/balloons-wallpaper-12.jpg

Right image URL: https://static3.depositphotos.com/1001048/122/i/450/depositphotos_1221636-stock-photo-group-of-balloons.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The left image is absolutely full of balloons, the right image has balloons and sky.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left image is absolutely full of balloons, the right image has balloons and sky.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

