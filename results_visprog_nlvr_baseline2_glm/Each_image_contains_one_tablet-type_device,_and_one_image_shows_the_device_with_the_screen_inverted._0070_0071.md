Question: Each image contains one tablet-type device, and one image shows the device with the screen inverted.

Reference Answer: True

Left image URL: https://www.kv.by/sites/default/files/user535/asus_taichi_31.jpg

Right image URL: http://insmart.cz/wp-content/uploads/2017/05/hp-laptop.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains one tablet-type device, and one image shows the device with the screen inverted.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains one tablet-type device, and one image shows the device with the screen inverted.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

