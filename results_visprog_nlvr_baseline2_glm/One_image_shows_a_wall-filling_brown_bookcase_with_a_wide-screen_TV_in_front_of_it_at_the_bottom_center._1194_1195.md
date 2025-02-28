Question: One image shows a wall-filling brown bookcase with a wide-screen TV in front of it at the bottom center.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1m6dMKFXXXXbVaXXXq6xXFXXXR/zelle-tirilmi-3d-duvar-ka-d-3d-duvar-ka-d-duvar-ka-d-kitapl-k.jpg_640x640.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB13IP_PpXXXXauXFXXq6xXFXXXF/Customized-3d-font-b-wallpaper-b-font-3d-wall-murals-font-b-wallpaper-b-font-3.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a wall-filling brown bookcase with a wide-screen TV in front of it at the bottom center.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a wall-filling brown bookcase with a wide-screen TV in front of it at the bottom center.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

