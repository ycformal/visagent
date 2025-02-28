Question: In one image, the back of a running shoe is balanced on a second shoe with the treads of its sole showing.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB19aX1OVXXXXa7XVXXq6xXFXXX6/1-Sztuk-Koszyk-wka-Knee-Pad-Sport-Pi-ka-No-na-Siatk-wka-Bezpiecze-stwa-Ochrony.jpg_640x640.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB12Vd1hbSYBuNjSspiq6xNzpXaG/New-Thickening-Kneepad-Football-Volleyball-Extreme-Sports-Knee-Pad-Eblow-Brace-Support-Lap-Protect-Cycling-Knee.jpg_640x640.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In one image, the back of a running shoe is balanced on a second shoe with the treads of its sole showing.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one image, the back of a running shoe is balanced on a second shoe with the treads of its sole showing.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

