Question: Is the young person on the right side of the image?

Reference Answer: Yes, the girl is on the right of the image.

Image path: ./sampled_GQA/n243701.jpg

Program:

```
 Is A <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='young person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the young person on the right side of the image?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='young person')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gAMQXBwbGVNYXJrCv/bAEMACAYGBwYFCAcHBwkJCAoMFA0MCwsMGRITDxQdGh8eHRocHCAkLicgIiwjHBwoNyksMDE0NDQfJzk9ODI8LjM0Mv/bAEMBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIAFQANwMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/AOPl16xuUUTaedwBAZCBz+FZa3i5be2TjA5zT/IkVuUXBIHtUh0+TAxCpP1FTGCjsJu5U8zzpE25++oFdJqGs6paa3PaW85KrIESPaD6cVhx2dxFNG/lqNrBuo9a6OTWtMuL4TvG4dc4Zojnn6VnWvdPlvuNEFzrt8z+Xc2VlIycFfLXj681Nbaha+SrT6TGF5JMZPFZstzE8jymZF3HcV56k9On0qza31nAqsZ1LKp6Bjz+VZpafD+ZXzMPhpCVXAJJA9KKIx8worqjsbt2LccTAqhyCMcmpcRxS7GMhbdg5NXLl7Zre2u1DmdSN0ZQBSOf4t2c8en40k9pHc6dDqv2qBJmk2/ZjGRwM85z7Unc5rCNFDgfM+79KedIKQGcIyBhkEnrQ1owQSebE2RnaD0+oqSS5dl8sTrtwFJDn+RpArGY9qrSAea4/Gle0iEZcnJCnOT3xTVE4JD7Tg/fD/8A16fcKUt2/eH7uMAgjNMS3KduhklVR1P+FFXdFiE2pxI3TDfyorWEbo0rT5ZWH3SFdOtyDzhc49gf8aWdsaJZICQSc8fVjU08DXFnCIyvyJltzY/h7V040fSbWz0SPU5DmWSMS5faI1Iyf0P1yaxlJRsJRvc4dHk2E+Y3J9aRBI5yZmBHQ4zXd39voOo6rHY6Jp0RhbJMrSMAFHUkjmuKuNtvdT20tvG4hLJlRycH1ojU5ugpU3EpTSulyU84uFON2BzVoxE2kuW5THGPWqX7tpGdEYKTwo7VZjcmK4DFidq9R71p0Ij8SNDw4udYi4zhW/kaKv8AguATayQe0ZxziinF2RVf4x2lKst/Dbf89D5fTPUAV2+s+D7vXLAtF5WzzSiyNIEIAPG3PBzzXHaDZm78SadbwuCXnXnBGPmFe1+ILqGG1jsxGph+4VI447frWUqfNJMqM+VM4CXydPJg2MY4okildk6YGOfqa5K700XMc9zFaMZpXLgbDgjP8I/OvS59JtHJWSN2EybNzkkqPTJ54ODVOIPYeD7dbmTyZJNyI8JG5kDdM8jOSfwxWcoulrubRmqzs9jyWLTHd2WeJraRcfKVxmpJtPe3s538wPkrnI54NdJqEyXd8GiZ2iX5UZ2B+vI4rK1f9zYshHLsAMVqm2tTGyVSyNP4cBF14yPGHVUIIJx1Boqf4cwlr2ZgFJzgBun3TRWkXZEYj+IU/Bd5J/wmWlmWEhfPHzYIH1yRXo3iN5TKieU2SwyN2R7c8HtXl2m3ctrexzxOyvFhlI7EGvQtf1C0tIY70xLDGYhIrBi5YsOnv175qZTUbXCEXJ2RzWueI5FnGmQMVwwDhGwFzjt680zQL59Wjl0WVjJC8Mk7cDEbBSeMjg9PY59q5I3h1LWri5CMuEVjn1H/AOqu08M6XcTajfpZqBcR2v7uQ9m2j5SO4YZU+nB7UQV3qVJ22OHhnkto8xOVzzgdD+FT6nexXcaCJi2GyfyrNbciMjZBXg+taos/tC2gt4lc+WXkKJ1Axkk0dBxdppnUeAkMSyMw/jJ+nH/16KteG5BFYTysihScMuSM8j06dP0opO/RkTtJ3ZyNvDEshwmOg6muz1DWbnVfD008ixxSwqqI0IK4GdvrxwO1FFFRe580FJv2hwekx+ZrV4d8gBRtyhyQ/I655PXNeieA7iU+IJTuwHhZmHYkMMflk0UVpR+NejCr8L/rscJ4st47bxXqEMQ2p5zcfjXe/DLSLPUrq5+2RmYRwKFBYgDJHpiiio6FPc1PEVhb6bPe21qmyMPEQM5xlST+tFFFTHYctz//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the young person on the right side of the image?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if True else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
