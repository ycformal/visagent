Question: Which material makes up the brown cap, cloth or plastic?

Reference Answer: The cap is made of cloth.

Image path: ./sampled_GQA/n318684.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='brown cap')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the brown cap made of?')
ANSWER1=EVAL(expr="'cloth' if {ANSWER0} == 'fabric' else 'plastic'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='brown cap')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the brown cap made of?')=<b><span style='color: green;'>leather</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'cloth' if ANSWER0 == 'fabric' else 'plastic'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'cloth' if 'leather' == 'fabric' else 'plastic'")=<b><span style='color: green;'>plastic</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>plastic</span></b></div><hr>

Answer: plastic
