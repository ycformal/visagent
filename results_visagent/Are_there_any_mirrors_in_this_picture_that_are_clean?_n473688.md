Question: Are there any mirrors in this picture that are clean?

Reference Answer: Yes, there is a mirror that is clean.

Image path: ./sampled_GQA/n473688.jpg

Program:

```
Are there any As that are <attr>?
Program:
BOX0=LOC(image=IMAGE,object='mirror')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Are there any mirrors in this picture?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} and {ANSWER0} == 'clean' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='mirror')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gAMQXBwbGVNYXJrCv/bAEMACAYGBwYFCAcHBwkJCAoMFA0MCwsMGRITDxQdGh8eHRocHCAkLicgIiwjHBwoNyksMDE0NDQfJzk9ODI8LjM0Mv/bAEMBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIAGQAFQMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/AO50WDw7atcvouopKJwoMRl5XGex570l5H8x4ryZ4Zg43qxI6E1uaDfaguoW1uZ5mt2bDK53Dp79K8qMeVndzXR1EiDd0oqaRfmorYg4mSRI2BZ1H1NWNOvITqlsolUkyADHNZLRIXHyj64q/pSY1S2xx+8X+dT1Go6HcuOaKe45oq7EnnKj5c1o6N5Y1a0MvCecu4j0yKy4n3IPoKs277XVu6sDU7MvdHoUgG40U1m3fN680VrYzPLbeT5R9K6HQNKGp+bJJIUhjOMr1J9K5K1myv4V2ukTPpvhiW8MQIcs4bdz6Dj8Kyq6G9GN3qaWp6pcW0yW9lGspRcv3xngD8hRTdFiC6elzIwea5AkdiP0FFSqN92OVbXRHltmxd9i/eJ2j8TXfeJD9l8ORWsfCKESuY0zR5Y/EXkvgCGQs249cMRxXflLa5Eb3AVlQggNyMjvU15e+rG2HjeDI9EEj6Lafu2yI8EEYorT/tKFAArKB7mil7SoHsaZi3tvZ2/ibV4AAt4blxG5UttBOR9BVO/t9QtYfNmmijXeqkLyTk44rU8R6def8LE1RraV4eFkBP3WDIuce+RWzBaxSopl+fIBIPTNazg29DnhU5YnC2dveXqy+VfMqxStGQY8nIPc4or0xLO32jbCnvx3op+yXZC9p5lHxV8njVsfxWqE/maW17j0NFFbPdmUdkaGeOgH0ooorFtmp//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there any mirrors in this picture?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 and ANSWER0 == 'clean' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if True and True == 'clean' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No
