Question: The dog in the image on the right is sitting and wearing a black tie.

Reference Answer: True

Left image URL: http://i.dailymail.co.uk/i/pix/2012/07/11/article-2172032-140498CB000005DC-548_470x423.jpg

Right image URL: https://i.pinimg.com/236x/3e/1c/b7/3e1cb7b93f6be6c4741776660207d726--wedding-tux-our-wedding.jpg

Original program:

```
The program is designed to evaluate the given statement by asking questions about the images on the left and right. The questions are designed to check if the conditions mentioned in the statement are true or false. The program uses the VQA function to ask the questions and the EVAL function to evaluate the expressions. The final answer is obtained by evaluating the expression '{ANSWER0} and {ANSWER2}' which checks if the conditions mentioned in the statement are true for both images. If the expression evaluates to true, the final answer is True, otherwise it is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The dog in the image on the right is sitting and wearing a black tie.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The dog in the image on the right is sitting and wearing a black tie.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

