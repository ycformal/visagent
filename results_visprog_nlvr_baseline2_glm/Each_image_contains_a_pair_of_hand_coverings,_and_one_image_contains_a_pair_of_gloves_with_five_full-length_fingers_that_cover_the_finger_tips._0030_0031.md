Question: Each image contains a pair of hand coverings, and one image contains a pair of gloves with five full-length fingers that cover the finger tips.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/8b/2b/f3/8b2bf38b1d46f88d9a89053f8cc7c141.jpg

Right image URL: http://ae01.alicdn.com/kf/HTB1F_o.QpXXXXcraXXXq6xXFXXXO/Warm-Windproof-Waterproof-Touch-Screen-Glove-font-b-Mittens-b-font-Fleece-Outdoor-Cycling-font-b.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains a pair of hand coverings, and one image contains a pair of gloves with five full-length fingers that cover the finger tips.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains a pair of hand coverings, and one image contains a pair of gloves with five full-length fingers that cover the finger tips.' true or false?')=<b><span style='color: green;'>fake</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>fake</span></b></div><hr>

Answer: fake

