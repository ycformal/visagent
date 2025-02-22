Question: The lipsticks in the left image are shown with their caps next to them.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/70/ea/cd/70eacd97f6cd7aae03adb745775ae787--isabelle-chanel-makeup.jpg

Right image URL: http://3.bp.blogspot.com/-3f1OFkxYSNU/UhcDNHqX49I/AAAAAAAAEI4/aIER6Pl7dTw/s1600/GiorgioArmaniRougeEcstasyLipstickReview.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='Are the lipsticks shown with their caps next to them?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are the lipsticks shown with their caps next to them?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

