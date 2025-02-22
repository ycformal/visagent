Question: There are no more than five bottles of perfume.

Reference Answer: True

Left image URL: http://1.bp.blogspot.com/-r5dpE47xGJQ/VB8amrcVxZI/AAAAAAAAC2w/raTuDDNbAUE/s1600/anniversary%2Bperfumes.JPG

Right image URL: http://i.ebayimg.com/images/g/AycAAOSwENxXmjoj/s-l400.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='How many bottles of perfume are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 5')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many bottles of perfume are in the image?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 <= 5")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="2 <= 5")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

