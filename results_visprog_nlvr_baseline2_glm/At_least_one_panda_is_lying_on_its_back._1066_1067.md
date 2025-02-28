Question: At least one panda is lying on its back.

Reference Answer: False

Left image URL: http://www.chinadiscovery.com/assets/images/travel-guide/dujiangyan/panda-base/giant-panda.jpg

Right image URL: http://68.media.tumblr.com/tumblr_lxrb3my6kr1r0n5y3o1_500.jpg

Original program:

```
The program is asking if there is at least one panda lying on its back in the image. The answer is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least one panda is lying on its back.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAmAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDuYtSGpxEy3Ea6iqkGJwNrRhSevrx06gis/WPEUEnh62gs/wB3NIgMsjcdRkjPUdTyKzYpbPymZVcRglhgH06dKwtRijeUTNHIsDriN/uqDnJAB5/z7156xMrWsYN2R2uh+JbKDWrCG6mkm1G+Q28QIzuk3bmPA+Ubf880/wAb2OraeiarbWwv4VZlmEQw0CMc79nIbHcjBHXmuH0fxVoPhrWYrjVrfMjxH7LdY3iE5IJ6Z5BweuK1F+ImjaZo1ld3eu3eo6nZ277/ACXXyrtpCf3RXrxxhscAdTnFdtNuUE2aR96JnWXimBDHctAft8M5lE4lwkhwRhh2XHp1xWnqHxG1G9sPJVIIojGQ2zLbjj1NchdeBtWh0watZ3KXaGPzZ47djvhPUjaeoHt6VlwXzXFqSwWQHgjcQeOvBqG5LqZz5onVfEWWUWWjWyud2DKxPO75VH+NccJCTHujxzjIrs/H9qZDpc0CsWeIoq9c4IIA/Ok0fwjc6hBbwW6KupFw7sx+WJc8k/SlKqotRe7Ohu2hkRPb6fdL5O+eYYzkYC+w9a27fwzr3iXfFbFIIizOEklCEAnnjqRXK6ybjR9Xu7GF/wB9BIVabux9fasvSNf1C18S2U0dzIJjMqlgxOQTyD7YpqhH4pasSO48R/D+78K6A+pTXYvWVlBt7dMkZ759B9Kw9FUSJHf3lrcR2DMYw5XgOOqk164vivS31KHSpJY2vJFDiNjk4PT8T6VuXdtaXei3VlIkZheJjtOAA2M5Hoc1Uo8y5dimrHh914imW4ZbUtHCvCgcZHrjtRUI01dQHnxxzKOmEjJH8qKxWFpJWsTZHRRNe6hf29tazFTK+NshWMk+ign5j3rPvbOaKeS6u9RSdsEeXK4DKoz/AA85+nFU9Hu7Z/FFnqF808pRwyRwAh3k6IM/Xr610N/ceAr69mnu7a8huJXLyKs7KMn2/wAKzjRvHexkqd1oZfjLQ9P1P4e6PcRXFsNXtoWlMO8K7xyMWwV9cYIryO2hEM8croVKuCoK5BI5xW34rWCTxZNJHLKbMyjZIWy/l8Y57kDj8K7/AErSPBsDJMskkkm3lnkz/wDqrtT5IpG0Y6WIrLxfJo+sJcNlEuERpIeflJHJ/wDrVg61eWOoald3GmObS3uHLJAzA7DjkjHY9fatvxXYabc6S2oQQoCJRHEY+pTOPx6VxSaVcyNvt45XiA+UBWz/ACrIirqewzNDcW+gySgiTyisIJyWJVBn/CvRLS2h0XTvJjC+a3Mrj+I1xel6PHqNnpdtdLiW2t0dssQVyoB6d+K3r3U7a0jMZVGQYVdo9e/NKFFc7qdSrJSuzw7xtBPF4n1AMAFlkMgbPVTWFods9vr1rcPbySrHJkhFLY+oHb3r3l7rSpAfPt4pcgjJRSMenSsPTE0Dw9Pc3NhZusspwQW4Qeg9B9K6AYy/8ReHHsm8QWmkRSavaP5S5G2TcOF+vHIOOBWtbm71/SzHPdC2M6gTGEc7e4BPT0zVO51vSTIzSwW3TJZlByfc1lf8JcpZ4rQF8LlVhUEjtgAdulLrdgeiR3Ato1hiKqiAKAp44orzqe91yR1dZ4E3KCVL8g+h460U+cLHl1r8QL6yQfZ9M0xJcEef5TGTJ4yCW44yOPWm3Xj2+vdSN7cafpzybERV8tgqBeFx83aiip5UGxA/jCSQjzNI0yRQuArxuQOc/wB71qUeO75dNvbIafpqpeACRlhIbg5GOeKKKLId2RWvjbUrS0jto4bYxxnI3K2c/nVpPiHqqMrfZrM7cnlW7/8AAqKKa00Qj0z4aeOdS8RT6wL2G2QwWaeWYVIPL47k+taOv3QtdMeWUFyCoyDjg8gfyoooeiDqcFd+KnhUsiPgjoT3rR8O28uuWi315dSpEWOIojjgH1/OiioQ2bo0TSjOfMtfMj6BHJYZ9cGrC6ZDp17mNVCkblRVwFx9OtFFMDD1DWbaK+lj8iVipAJ3Y5xRRRSA/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one panda is lying on its back.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

