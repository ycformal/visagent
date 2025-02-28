Question: An image shows a large silver-framed sliding glass door that is open, revealing swivel office chairs around a table on brown carpeting.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/50/41/08/5041087941fa825ec2bd4223f819917a.jpg

Right image URL: https://i.pinimg.com/originals/64/40/d9/6440d94b3932b0239ff6965380dda9f6.jpg

Original program:

```
Statement: An image shows a large silver-framed sliding glass door that is open, revealing swivel office chairs around a table on brown carpeting.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows a large silver-framed sliding glass door that is open, revealing swivel office chairs around a table on brown carpeting.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows a large silver-framed sliding glass door that is open, revealing swivel office chairs around a table on brown carpeting.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

