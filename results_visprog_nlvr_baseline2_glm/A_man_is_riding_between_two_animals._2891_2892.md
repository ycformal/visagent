Question: A man is riding between two animals.

Reference Answer: True

Left image URL: http://i.dailymail.co.uk/i/pix/2012/10/14/article-2217619-157D0EF5000005DC-854_964x580.jpg

Right image URL: https://i.pinimg.com/236x/03/70/29/037029e992c806f4b901a3cf5cc24a32--riding-horses-water-buffalo.jpg

Original program:

```
Statement: A man is riding between two animals.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a man riding between two animals?')
ANSWER1=VQA(image=RIGHT,question='Is there a man riding between two animals?')
ANSWER2=EVAL(expr='{ANSWER0} and {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A man is riding between two animals.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A man is riding between two animals.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

