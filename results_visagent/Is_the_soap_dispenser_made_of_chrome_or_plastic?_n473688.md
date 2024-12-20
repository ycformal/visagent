Question: Is the soap dispenser made of chrome or plastic?

Reference Answer: The soap dispenser is made of chrome.

Image path: ./sampled_GQA/n473688.jpg

Program:

```
 Is A made of <material> or <material>?
Program:
BOX0=LOC(image=IMAGE,object='soap dispenser')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the soap dispenser made of?')
ANSWER1=EVAL(expr="'chrome' if {ANSWER0} == 'metal' else 'plastic'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='soap dispenser')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gAMQXBwbGVNYXJrCv/bAEMACAYGBwYFCAcHBwkJCAoMFA0MCwsMGRITDxQdGh8eHRocHCAkLicgIiwjHBwoNyksMDE0NDQfJzk9ODI8LjM0Mv/bAEMBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIAC4ALgMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/ANzzARxTfNPrVISgHr+tJ9oA/iAryj27l/zcD3qN7hQfmNZ7XRdtqBmY9lGTUN0l3HavKFTcBnYzc0nJLcTZbmvAoOGH1rFudaUN8h3VgTajPcPiR/lJ6DtUYcdOKcnYi9zoptTiiPLfN6LWxp8FrPpA1C4LyZYqIg2APrXFzA7ufWtCw1s2MM8MkNyYSeqIGBPtzmiyaJbZ07XRwVhRYk/uoMVXnmjiiLzSpGp/ikYAH865ifXdSufls7VLZe0kxDv+XQfrVEaYZ5vtGoTyXUv96Rjj/P0rNUV9pg59iXTUWbV0CDfDHJlm7EDoK7NLOK5G6S3iY+pUGsXS7QKu/YAv8IxgV0tqW2Vc6HNqyI1OiOHnHzccc1P5KpArk/fycZqK4PznjvWta2UU9uryln74J4ranHmIqyaSMgHc2I1Jb0ArQt9Nkdg0/A7IP61t29hGo+RVQewrRgsolwcZ+tW1GO5muaRRtbNpMADAFa8VsIlAqSMKuMDFT8EVnOTZrGNj/9k="></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gAMQXBwbGVNYXJrCv/bAEMACAYGBwYFCAcHBwkJCAoMFA0MCwsMGRITDxQdGh8eHRocHCAkLicgIiwjHBwoNyksMDE0NDQfJzk9ODI8LjM0Mv/bAEMBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIAC4ALgMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/ANzzARxTfNPrVISgHr+tJ9oA/iAryj27l/zcD3qN7hQfmNZ7XRdtqBmY9lGTUN0l3HavKFTcBnYzc0nJLcTZbmvAoOGH1rFudaUN8h3VgTajPcPiR/lJ6DtUYcdOKcnYi9zoptTiiPLfN6LWxp8FrPpA1C4LyZYqIg2APrXFzA7ufWtCw1s2MM8MkNyYSeqIGBPtzmiyaJbZ07XRwVhRYk/uoMVXnmjiiLzSpGp/ikYAH865ifXdSufls7VLZe0kxDv+XQfrVEaYZ5vtGoTyXUv96Rjj/P0rNUV9pg59iXTUWbV0CDfDHJlm7EDoK7NLOK5G6S3iY+pUGsXS7QKu/YAv8IxgV0tqW2Vc6HNqyI1OiOHnHzccc1P5KpArk/fycZqK4PznjvWta2UU9uryln74J4ranHmIqyaSMgHc2I1Jb0ArQt9Nkdg0/A7IP61t29hGo+RVQewrRgsolwcZ+tW1GO5muaRRtbNpMADAFa8VsIlAqSMKuMDFT8EVnOTZrGNj/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the soap dispenser made of?')=<b><span style='color: green;'>metal</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'chrome' if ANSWER0 == 'metal' else 'plastic'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'chrome' if 'metal' == 'metal' else 'plastic'")=<b><span style='color: green;'>chrome</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>chrome</span></b></div><hr>

Answer: chrome

