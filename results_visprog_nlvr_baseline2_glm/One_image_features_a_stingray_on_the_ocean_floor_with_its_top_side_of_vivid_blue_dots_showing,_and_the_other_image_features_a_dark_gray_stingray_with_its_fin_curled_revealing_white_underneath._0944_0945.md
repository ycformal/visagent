Question: One image features a stingray on the ocean floor with its top side of vivid blue dots showing, and the other image features a dark gray stingray with its fin curled revealing white underneath.

Reference Answer: True

Left image URL: https://thefisheriesblog.files.wordpress.com/2013/11/0aca1-blue-spotted-stingray.jpg

Right image URL: http://easyscienceforkids.com/wp-content/uploads/2013/06/stingray.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image features a stingray on the ocean floor with its top side of vivid blue dots showing, and the other image features a dark gray stingray with its fin curled revealing white underneath.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image features a stingray on the ocean floor with its top side of vivid blue dots showing, and the other image features a dark gray stingray with its fin curled revealing white underneath.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

