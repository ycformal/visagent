Question: Each image shows a rightward-turned non-white man in a suit holding a saxophone, and at least one of the men depicted is playing the instrument he holds.

Reference Answer: False

Left image URL: http://bassic-sax.info/blog/wp-content/uploads/2013/02/mac1063_garrett_pr_3_10_rgb__large.jpg

Right image URL: http://bassic-sax.info/version5/wp-content/uploads/2010/06/Right-Side-Upright.jpg

Original program:

```
The program provided does not contain a statement for this question.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows a rightward-turned non-white man in a suit holding a saxophone, and at least one of the men depicted is playing the instrument he holds.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows a rightward-turned non-white man in a suit holding a saxophone, and at least one of the men depicted is playing the instrument he holds.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

