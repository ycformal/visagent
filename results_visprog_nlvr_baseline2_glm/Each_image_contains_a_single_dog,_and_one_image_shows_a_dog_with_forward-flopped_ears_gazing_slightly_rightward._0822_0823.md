Question: Each image contains a single dog, and one image shows a dog with forward-flopped ears gazing slightly rightward.

Reference Answer: True

Left image URL: http://s6004.pcdn.co/wp-content/uploads/2015/05/kIV5NIDl-370x215.jpg

Right image URL: http://royauxsuedois.r.o.pic.centerblog.net/Border-Terrier-9M037D-15.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains a single dog, and one image shows a dog with forward-flopped ears gazing slightly rightward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains a single dog, and one image shows a dog with forward-flopped ears gazing slightly rightward.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

