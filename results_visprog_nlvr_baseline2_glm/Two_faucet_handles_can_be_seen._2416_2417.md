Question: Two faucet handles can be seen.

Reference Answer: False

Left image URL: http://2.bp.blogspot.com/-LFESatip5vs/UcIi9zFRs_I/AAAAAAAAF8k/5lxFkhdCkOU/s1600/IMG_3591.JPG

Right image URL: https://i.pinimg.com/736x/86/82/60/86826053e5420ef7fdc0679215ae5970--under-bathroom-sinks-under-kitchen-sinks.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Two faucet handles can be seen.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Two faucet handles can be seen.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

