Question: Each image shows the bare framework of a yurt-type building under construction, and the right image shows a ladder under the framework.

Reference Answer: True

Left image URL: https://image.jimcdn.com/app/cms/image/transf/none/path/sc8557ec86e144884/image/i201190ca525a5d71/version/1392048862/image.jpg

Right image URL: https://i.pinimg.com/736x/9f/62/10/9f6210f91cad5e920964b1b45b7a172e--dome-homes-geodesic-dome.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows the bare framework of a yurt-type building under construction, and the right image shows a ladder under the framework.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows the bare framework of a yurt-type building under construction, and the right image shows a ladder under the framework.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

