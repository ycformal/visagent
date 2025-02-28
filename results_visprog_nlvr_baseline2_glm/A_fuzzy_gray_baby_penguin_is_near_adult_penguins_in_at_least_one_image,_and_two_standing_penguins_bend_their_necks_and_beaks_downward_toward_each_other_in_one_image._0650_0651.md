Question: A fuzzy gray baby penguin is near adult penguins in at least one image, and two standing penguins bend their necks and beaks downward toward each other in one image.

Reference Answer: True

Left image URL: http://i.dailymail.co.uk/i/pix/2013/12/16/article-2524769-175C6848000005DC-444_634x410.jpg

Right image URL: https://www.aboutanimals.com/images/emperor-penguins-820x507.jpg?d8bc0c

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A fuzzy gray baby penguin is near adult penguins in at least one image, and two standing penguins bend their necks and beaks downward toward each other in one image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A fuzzy gray baby penguin is near adult penguins in at least one image, and two standing penguins bend their necks and beaks downward toward each other in one image.' true or false?')=<b><span style='color: green;'>same</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>same</span></b></div><hr>

Answer: same

