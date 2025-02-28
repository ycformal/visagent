Question: In one image, a little dog is being cradled by a person, one hand clearly visible, and held up beside the person's face.

Reference Answer: True

Left image URL: https://ilovemychi.com/wp-content/uploads/2014/12/child-with-chi-225x300.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/80/be/c6/80bec6492dfe91da606eea0eff8137c8--chihuahua.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In one image, a little dog is being cradled by a person, one hand clearly visible, and held up beside the person's face.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one image, a little dog is being cradled by a person, one hand clearly visible, and held up beside the person's face.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

