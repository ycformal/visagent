Question: Is that an Asian woman?

Reference Answer: Yes, that is an Asian woman.

Image path: ./sampled_GQA/n527290.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is that an Asian woman?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is that an Asian woman?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
