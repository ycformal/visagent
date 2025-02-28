Question: Each image shows exactly one girl, who is wearing matching knitted mittens and cap, her hands pointing up towards her face, and a large pompom on her hat.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1cSJYRFXXXXXYaXXXq6xXFXXX4/2017-Winter-font-b-Women-b-font-Casual-font-b-Hats-b-font-font-b-For.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1JYaCOFXXXXX9XFXXq6xXFXXXL/CIVICHIC-Korean-Stylish-Woman-Warm-Set-Color-Mix-Winter-Knitted-font-b-Hat-b-font-Gloves.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows exactly one girl, who is wearing matching knitted mittens and cap, her hands pointing up towards her face, and a large pompom on her hat.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows exactly one girl, who is wearing matching knitted mittens and cap, her hands pointing up towards her face, and a large pompom on her hat.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

