Question: The left and right image contains the same number of boats with their sails open.

Reference Answer: True

Left image URL: http://www.denmanmarine.com.au/image/data/Sail/Caledonia%20Yawl/EowynLaunch050.jpg

Right image URL: https://i.pinimg.com/originals/c9/bc/de/c9bcde3ab9b1964d7b20e45a71f9aaf3.jpg

Original program:

```
Statement: The left and right image contains the same number of boats with their sails open.
Program:
ANSWER0=VQA(image=LEFT,question='How many boats with their sails open are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many boats with their sails open are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} == {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same number of boats with their sails open.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same number of boats with their sails open.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

