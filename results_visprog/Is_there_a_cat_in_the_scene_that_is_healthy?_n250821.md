Question: Is there a cat in the scene that is healthy?

Reference Answer: Yes, there is a cat that is healthy.

Image path: ./sampled_GQA/n250821.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cat')
ANSWER0=VQA(image=IMAGE,question='Is the cat healthy?',box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='cat')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the cat healthy?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
