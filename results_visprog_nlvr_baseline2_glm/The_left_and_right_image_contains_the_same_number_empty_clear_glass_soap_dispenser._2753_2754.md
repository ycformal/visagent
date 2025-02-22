Question: The left and right image contains the same number empty clear glass soap dispenser.

Reference Answer: True

Left image URL: http://cdn8.bigcommerce.com/s-i17pk3h6/products/226/images/1219/bell-glass-soap-dispenser-antique-bronze-metal-well-pump-rail19-19__98138.1479316879.800.800.jpg?c=2

Right image URL: https://img.etsystatic.com/il/3fc78a/761172121/il_570xN.761172121_i92j.jpg?version=1

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many empty clear glass soap dispenser are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many empty clear glass soap dispenser are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} == {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many empty clear glass soap dispenser are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many empty clear glass soap dispenser are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} == {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAD8DASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0Qio2FTkVGwoAgYVGy1ORUZFAEWKYRUpqNqAIGFRMtWGFQsKAN9qiapTUbCgCIimEVKRUZoAiaozUrVE1AETVG1SNUbUAbxqM1KajagCNqxde8QWfh+0a4ug7YQuETGWA64yR61He2nii7vZlh1Sw0+yDfujFbGaZl9TuO0H6A1ga9pWrWtmZr7X31C38uZGiks4o8ZhfncOeuKALfh7x7pPiOO6eMSWYt9pc3RVVO7OMHOM8HiuhimiuIVmglSWJvuvGwZT+IrzD4OpZHT76SZYPtazosZcjdgpyFB+navQl0bT4bxrqGAwyu29/JkZFdvUqDtJ/CgC21RNUjGomoA6I1E1StUTUARMa4nXPDkOuy3dg9/aQ3dyd6St5hZR2BA+U8DFd5axLPdLG33cFj9BV4x/Z76Fv4ScLx7dKAPnu1+G7W2pWzPr8UbiTKyLCchhyMHOM/jXsDHPOc5q0YfNP7tQeMnA96z3jNtP5R+6w3Aeh70AKxqJjTmNQs1AzqGqFqnZW/un8qhdW/un8qBElgga6Z88qh/XFWbptstueeJVqvp6t9qOcgbD261LeLma2GcDzRn8xQBUkJGo3QGQAcfhWPe/8fqH0U/0rWm/5Cd3z1b/Csq+RmnGxSxxzgZpAVWaoGanMkv8Azyf/AL5NRNFP/wA8ZP8Avg0xno5GaYV96kJ9BSfhQIg6TIMgEhsZ71HerEkcbySouHByTSX9lFf2/lSb1IO5HRtrIw7g1jSaJqAj8tr6G5Qfd+0wAkfipH8qQFhvs1xfzyJdRnec4zUKx+Req+8EFSODVePQ79WOHs4/UxQEH8yTV2DTJIVwXLHGCT1oAeZlbo1MMyj+LJ9qV7Js5NAgxxjFMDo9oprKAKKKAI1X5qc6ggUUUAN2jcTTCgoooAayLimeUh7UUUAf/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many empty clear glass soap dispenser are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAEMDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD1YCnAUoFOxQAgpcUdKg+3WYfYby23f3fOXP5ZoAnxQaUcjI5B6HtSGgBpFMIqQ000DIivNFPI5ooAmApcUoFLQIqX9jBqVjNZXSFoJkKOoYqSD15Fc2vww8GMVU6JFyQN3myZ6+u6uuNFvcW8N6UmljRpISEDnG456D1oA4Lwj4OtbB7TU7DU9QgQPJ5tms+6GQB2UAg9BwPyruq8j8GWt3b/ABSmZ7eWOI2UgY7SF3ZXr2r1vNJAwpuaUmmmmMKKSigCyKKKKBCGpLMA3seRng1EarJLLFd/aDMBGAUSMDk88sT+GBQBQiiEfim6YKAHgz9fnArTJqnfSi2vmnAG0MVYd8Mwx+tWmoACaTNNJpM0AOzRTM+9FAy7mgmm5pCaAFJqhK/Qe7f+hGrhNUJM7ScfxN/6EaQiHXB+7mOedyf+hrWgx+Y/WszXSwjkOOskX/oS1oMeTR1ACaYWxQzVEzUxkm6ioN9FAGlmjNR7qC1ADiagyNnPct/M04tUZOEUn3/maQhuqjEMjdCEU/qKc7cmotakxaOR/wA81/mKY8nJ+tMEPZ6iZ6jaSomlFAyXdRVfzaKAN3yH9fzoML9sfjVoyIvUik8xPr+FFhEIgGOQDUSiIo+SuEdl5+tXgQaybnR3luJJIrrYsjFtpXOCTzg0WAnu0guIivysNoFMe2jJ4UVEmj3KjH2sEHsU7VcWxZRy5JpiKTWkXtUbWURHAOfrWk1mezGk+ysPWiwzL+wx+/60VqeQ/wDkUU7BcURjOcmrCRKBnHPvRRQBKFHWgqMA0UUCEb+lKaKKAFwD1FJtFFFADT1ooooA/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many empty clear glass soap dispenser are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER2</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == ANSWER1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER2</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

