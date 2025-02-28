Question: Each image includes at least four flutes displayed vertically, and the right image contains exactly five flutes.

Reference Answer: True

Left image URL: https://s3.eu-central-1.amazonaws.com/cnj-img/images/5o/5ogzKInw8cup

Right image URL: http://1.bp.blogspot.com/-VDrTj__lug8/VBIltk9tsLI/AAAAAAAAGTw/nxgQ-FvmT7k/s1600/kayser%2B(1).jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image includes at least four flutes displayed vertically, and the right image contains exactly five flutes.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image includes at least four flutes displayed vertically, and the right image contains exactly five flutes.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

