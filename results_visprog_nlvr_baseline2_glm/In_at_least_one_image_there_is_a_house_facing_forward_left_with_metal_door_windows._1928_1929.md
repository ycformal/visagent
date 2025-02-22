Question: In at least one image there is a house facing forward left with metal door windows.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/44/7e/d4/447ed4320e7a68d89d19adef6784af01.jpg

Right image URL: https://i.pinimg.com/736x/43/c2/0b/43c20b56e154840c3454a01b2dc4163c--english-cottage-style-english-cottages.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAApAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDrTpoHzNjHvUgtosKBGc+tdElrFJGsiAMrDII54rh/GXiUaVdJp2msBc9ZW4O3PQD39a9eWJilc8uFCTdkXZWEGpSW0qxpCkQcuzEHn68Vh63rNhuhisrlZGDEvtOQPTn864fUNWnvJy01w80hPLM2cn8abp7tO8jdRHXm1sTJwafU9TD0IqrFrodNc+PmgLNBYK8cQBfcxyRnBPHSvS9PuTqGkW9xET9llRZBjpz615Ppln9j0K5vbmGBoNVSW3jDylHKL94LwRknGP8AdqrpXjPWdB0r/hHXEe62mkV5FcMdvUqp6dcn8adPFNJuWphWw6fwnozW/wA7fU0fZ/atCCPfbxSEA7kVs/UZqq96pufJihMm3l27KK9yeKjCN5M8SNFzlyxIfs/tR9mJ9qdLePuKqix+7cn8qy7q4lV/nlLMO2OK5J5pFfArnbTy2T+N2A3hGuDTJIFQFSySYbL8euMY4/nV5rUYrlr3xNPbXLypEbuSzVpig4AQ4DAHvxz9a6ebXtKhsrW7a4zDdKHjIGeCM8/4UYLG3jJ1ZbP8wx+FUHFwWjX4ob9nUdYwfxorn5/HtnFO6C2YgHgjuO2aK3/tPD/zfmcf1ep2L2jeMr600hNNs3iEio4ieSIkRr2c+vXiuZm0BdUmYxa2Lm9mbMmTgscjJJ7c8/SlsrDxE2l3P2iPyZY5Ase8bNvTI+namx6K2nagL/7apYsWkQIQQc9v8a+K+uNWjz7fM95Pl2Ob1G1Gj6hc2l/LseNiqiL5g3POD6Yx+dRR36QW8rW6yMVOck4H0x3ruJorDVdKlhniSN4TJmUR/OCR6nqOBXAX9i0d2kKGMRS5MYUkkCupVVPZlNyWx6Readfjw0Lq9uybbTLdJre1iVHDbzjrtzyMg968mNzOkn2rLZZy27b/ABEn1r1BLjT9S0Uoby8iL28cZDXTsMqSement0Fc/wCR9ns1SOXbbC5R4RKhycE5IPYcjitFUivdTuU7rQ7ifxsJbOzS1CWyLGDPLKQwAAA4+vpVM+NtJhtnNv5sqlss0MbbfpnGKwrOSw0222XEU+Sw3zkA5J6YHTH061VaXRrPw6t/f2N0ltLLItmOcb1PzbiD3PqCO3rWvtZzWupFKhGHQ2T46kmkaG00eVzkHMxVF49Tz61SutQ1y8klJNtaKy4YRAs2T057d+1Ztle3VvdmKOSaxkjjWSRYogVbd90Ec569OlWbjWfKmaOMok25C5bgSMM8j0wD2qHNpqy1NraHeeENEew0d5LxVe4lQAhvmJXnr9c15VrljdaPrUmiO7+TDJ/o5J48pvmU/hk/rXZav48vdN1K4hhihZFVR8474BJH51xV3rL6lcLLcsrzbiVbGSB6D0+lZKpJttrcwnOFuXcdFpkHlgyl5HPJZSAKKgGqlMgJMcnOeuf0opc0uwvaQ/lPRx8QNA+1zAXtpGn3hKrZJOPQ1z+u6hb69IptvEOkIyO4EtzIsfyHGMHJPXnoOnavHKKxpZXTpO8GaT97c9v0nT9Ah2nVPHOlOmwq0cE/LZGMFif6Vrq3w9hTy49W05l9XuAx/M1880USy7md3UfyshKKWx787+BwB5OvWsWBgbLpTx6YINZ07+FLZHey1mylnJDKZbhMAj0wOPwrxKgU45db/l4wsfRMPgxSsU+m32mySFQ+2ZWQbuoxkH8Kr+JPBmv6p4YOm2+nxbbeUzQrBIrhstkqDn3J5rYsv+QZbf8AXFP/AEEVv6V1H4V1OPK+ZM0tezOJ8Z+HdP027ga1W9NzcqplTjBwuBgkYXuM8+teZaofsVrEiRxnMhLyMQxHbH/16+p7v/kHTf7hrg5v+QoP96P+dQqrTVwfQ8bnt5p1WXapkZRuKjaent+FVI7dyCgtZFOMng547+30rs/EH/IYu/8Arsf61kS/dvvo38qxVVs492YXlXgA8jzHT1Y7SPworrl/1af7ooo9t5FqKsf/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

