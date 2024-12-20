Question: Is the weather partly cloudy or cloudless?

Reference Answer: It is partly cloudy.

Image path: ./sampled_GQA/2365753.jpg

Program:

```
 Is A <weather> or <weather> B?
Program:
ANSWER0=VQA(image=IMAGE,question='Is the weather partly cloudy or cloudless?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the weather partly cloudy or cloudless?')=<b><span style='color: green;'>partly cloudy</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>partly cloudy</span></b></div><hr>

Answer: partly cloudy

