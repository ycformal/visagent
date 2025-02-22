Question: There is a dog on a pool raft in the left image.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/xiwaKBr4EOs/maxresdefault.jpg

Right image URL: https://i.ytimg.com/vi/Vrf_3wxPw_w/maxresdefault.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='Is there a dog on a pool raft?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a dog on a pool raft?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

