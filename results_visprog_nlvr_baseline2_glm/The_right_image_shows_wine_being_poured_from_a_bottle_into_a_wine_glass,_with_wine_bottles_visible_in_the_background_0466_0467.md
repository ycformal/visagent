Question: The right image shows wine being poured from a bottle into a wine glass, with wine bottles visible in the background

Reference Answer: False

Left image URL: http://www.achillcottages.com/images/fireplace-reading-book.jpg

Right image URL: http://www.achillcottages.com/images/fireplace-wine-glasses.jpg

Original program:

```
Statement: The right image shows wine being poured from a bottle into a wine glass, with wine bottles visible in the background.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image shows wine being poured from a bottle into a wine glass, with wine bottles visible in the background' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image shows wine being poured from a bottle into a wine glass, with wine bottles visible in the background' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

