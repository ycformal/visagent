Question: Is it an indoors scene?

Reference Answer: Yes, it is indoors.

Image path: ./sampled_GQA/2371554.jpg

Program:

```
 Is A <scene type>?
Program:
ANSWER0=VQA(image=IMAGE,question='Is it an indoors scene?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAyAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDuG08dxioHsMdBXQm2kA4L/nmoZIZAPX6rXm69zc5mS1Ze1VJIiP4a6SaCTGdq/rWZdCSIZ8kH8aHJopJMxJFI7VWfPpWlJdx5w8LL+FMkFn5fmPMqA+pA/nWbrW3LVK5lM4HXFTWpjlDZQkg/hVa4vNOViqSCQ/7Jz/KohqqxRSrFGwcjKHjGfz5pqq2N0zaVT2VVpskagZduPWqh0LW5fD8ery6okcUsvlLFEuG78549Kym0FZTm4uJ5T/tEf1zVu/UiyNCe/wBOgJElzCD6b8n8hWZc+ILBAdnmP/ux4/U1Kug2Sf8ALIt/vSn+mKcNPtIj8ttAPfZu/U0J+YaGHJ4ljLnbbuR7yCiugCKBgLgewAop3DTse+m2TH3aqy2ik8CkupzaW9xOLnecZVWxheg/GueudQlmbd57k+xwBVvlWxlFNm1JYgjpVWXR1mIQjk1izatfpHsa8KJjGS6g/n1qK11O6tp4pkv90e8bw0ocEZ59f0qJST6FqL7kmt+GTbWjzqAQK8uv7XN3OQgzuOT+Feq614ps5rSW1huvMkfJAZCpA/IV5HqOp+Xf3QDfxkVyVIPdHVQl0kVbOMr9oPcRHr+Na1sDJp9uC4P7r7pHPQ1iafceeboZziE/1q7oUshWWJ3basa7QWz/AH849O1axWgpvU7PxRLNZfCCya3co41BACpI4Ib0rNs1K2MbSFmHPzMcnrXRavpN1rXwpt7ayhae4F4jqgIHQ89eOmax01CGwhOn3Vti6gJMsTttIXPX3HNbVPhT8jFayaXconUbIzlFdiRkfdxzVW5kbyi0ZwSwAOM9TSReI9HiuN11okAPzANFGdoJOM5zk8VUn1S1vLr7LY2805c/KkXJz6DvXPC6eqNJJP4Sv9vk3OryOjKxUhto/HpRV/8AsDUSAW8O6lz6wrRW90ZcsjHvvHQl1exhtbiRIVnXzCTweR3r1/RC+rWQnkWNCSRwOuOM/nXzjPbxy9ODXd6T8TtQ0jT0tYrCFykaxhySMkdT35JJNbTo6pxM41NNT1DVdK0nT4nvrq3e4dmCBUXcWJ6cE4H17VRTSZy4kh8OGMdds+ort/FVDV5pf/EvxBflAWhiRXD7UXuPes3UPFeu6hKd2qXHkq5MaA4wM8ZxTVOQnKJ7FcJdQIhvLfTIIicbVnkdvw4Arz34hS6RDaLJam0S7LceWQWf1Bx7c5PpXHyXt9O4ea8uJSDn53JHXPSqT2akEgDJ68U1Q7i9rbY0fDd8GkvNw2bYRyTx1NdFps2GbaVwyDOO/wB+uMsw1g8pVA6yrsZW6YrWstXtrYBfIeIYxhTkd8fzNZzotN2RtGqmldn0b4GnVPCEDu6qPMYZJwOteI/EO0vf+Fga5JBKyea+AGGRgouCPy/Ws698V3E9lHp6zg2a4YqydWznvWedXLtuLA++a3pxfKlIwqS95uJSDa3avKxJlGx9gHOCenvXW+DdWW28V2EE6/vXZYwTF3YD+IA+vf0rJh1iPoUH1q7BqMG9ZAwV1OVI4IPtROlGSsyY1pRPSbr4keF1mIj1u0IxySGHP4rRXnRXTX+ZoI2PrtorL6rAv61LscmOlIOaKK6jIVQM9Kev3qKKBEo/pSnpRRQIjk6GqTgZ6UUUDQRgc8CmyAegoooZRCeCccVJG7Z+8fzoooAvxyPsHzt+dFFFBJ//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it an indoors scene?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

