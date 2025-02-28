Question: There are cheetahs eating in each image.

Reference Answer: False

Left image URL: http://i.dailymail.co.uk/i/pix/2010/11/30/article-0-0C49CAF1000005DC-772_634x397.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/86/84/6f/86846f824585773c745e339c5ede8600.jpg

Original program:

```
The program provided is a series of logical steps to determine if certain statements are true or false based on the content of images. Each statement is evaluated step by step, and the final answer is determined by evaluating the logical expressions.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are cheetahs eating in each image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are cheetahs eating in each image.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

