Question: There is a dog sleeping with a santa hat on

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/51t8A3ldbjL.jpg

Right image URL: http://www.warrenphotographic.co.uk/photography/bigs/18277-Sleepy-American-Cocker-Spaniel-pup-with-Santa-hat-on-white-background.jpg

Original program:

```
Statement: There is a dog sleeping with a santa hat on
Program:
ANSWER0=VQA(image=LEFT,question='Is there a dog sleeping with a santa hat on?')
ANSWER1=VQA(image=RIGHT,question='Is there a dog sleeping with a santa hat on?')
ANSWER2=EVAL(expr='{ANSWER0} xor {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is a dog sleeping with a santa hat on' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a dog sleeping with a santa hat on' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

