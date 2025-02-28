Question: One image shows a dog team heading straight, away from the camera, with the sled driver not in the scene.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/0c/94/71/0c9471161e815053a24ebb753d3a5858.jpg

Right image URL: http://1.bp.blogspot.com/-TU1sPUw3z0M/Uw5B76HiNvI/AAAAAAAAFVE/klColGf-gag/s1600/Day+290+-+Sled+M.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a dog team heading straight, away from the camera, with the sled driver not in the scene.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a dog team heading straight, away from the camera, with the sled driver not in the scene.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

