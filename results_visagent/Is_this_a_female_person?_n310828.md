Question: Is this a female person?

Reference Answer: Yes, this is a female person.

Image path: ./sampled_GQA/n310828.jpg

Program:

```
 Is A <gender>?
Program:
ANSWER0=VQA(image=IMAGE,question='Is this a female person?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is this a female person?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
