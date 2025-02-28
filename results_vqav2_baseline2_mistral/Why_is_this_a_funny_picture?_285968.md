Question: Why is this a funny picture?

Reference Answer: funny cat

Image path: ./sampled_GQA/285968.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Why is this a funny picture?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Why is this a funny picture?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwClCvStCFKqW65xWjEtI0J41xVlBUSLVlE6UAOVamVaVEqUKFGSQAO5o2EMC07ZVC58Q6LZDNxqdsgHXD5x+VaUEkVzbxzwOJIZVDo69GB6GgCIpTGWrRWmMlAFJlqvIlXnSq0i0AZ7J81FTMvNFAHNW2rWIAzNwenymtq1vbWUApOh+px/OvI/DurqjrZXJ+UnEb+h9DXcwQhhwvFQ5NMcUmjt4QrjKkEexzVuNK4+1jeFg0cjRt6qa3rfVZYo8TIJSO4+U0Ka6jsbSJVDxBYtf6LcWa5xPG0Zx2JUhT/31ilXX7CCCaa9kS2jiXczMwIx/jXmeq/Fi8v7dobPT47YB8+bv3kqDxgEAZqasXUpuMd2JOz1OBDu9nhyTsPIx0/ya998B3IvfBGlOGDMkXlNg9CpI/livEI5Ybie6kHkrvLS/PGQQOpGOlQWWsXOlahDeWssiTQv5ke4cZ9Nvp7VtujNaH0wUpjJ7V5r4W+JOta3rekaZJY2m2aXy55Rnc4wSSBnC4/GvWDCMUirmYye1V5Ez2rVeIVVkQUAZLR/NRVtlG6igR8xAkHIODXqGi3nn6dbyueXQEk+vevM7eBriTavA7k9q7+zby7eNUxsUAD8KmY4nVRzjcKtLcfKelYEFxkjk1cS5A+tY2NLmN8QNRRdHS0JUSzupCYGSoPX6V53GTGoA/8A110HjRmbWknJyPJAUZ6cmueDswVwQCOK3grIyk7sbMxSds57ZoVJZQ03UZwSatR2pnW7lMUhEMO6QjouSAD9Mmo4XVYvK3HbjPA6GqEbPhvUJ7TxRpDwk7kuY/ujruOCPyNfSjygZr5i8MTIPFulyTNthW5Qk+gBr6QMoIyDkHvSGiZ5hVWSUVHJKRVdpM0ADyjdRVSRhvPNFMls8H02MLbZPVjn/Cum0uXzbcIeNpIrAgwAFHTGK0tKkVbh19eaylqWjpIkX+9n8KuosW3c/wCvNUYmxwByTVTxRczaVpSAHE9xlc5+4o6/ielSk2W3Y47Xb0X+qSuG/dhtq/QcVe0C90+zvY47q3SS2n+RxtBZVP8Ay0yem3rxjOD9a5vzMyAuNwz0NSIkjGRo8nOAW7DPvW60Mnqem6l8NdZ0yyuHRxJa3Kr5cyMAk0fXnjjsRWJH4XgsdMu59Zhw+3FvEkm1i5OAT7DmtzX/AIvXP/CKaf4e0V3jWC2jhmuj95iFwQvt7159pMVxqF8luj5knbZlieBQJGl4csI5vEKAjdHEpccY5HqOxzXsuhXxm08xseYm28+nUVxeheFhoxkmmn86d1wWC4AFdDo58ma5TsQrfzFRe7L2RuyTdeawvEOvrottFJhGeV9iq7Yzxk1ekl9687+JImkSwlCM0EZYMR0DHGM/lV2IvqaR8dEnm1XPtIf8KK86gu9ke2SJXIPVsg0VfIK5eX7tXLLi8T36/lRRWDLR3OhRq8jMyglcbc9q5n4lO39oWiZO0QZA+rH/AAoooiVLY4I/1rr9SjS18CacsK7BcT5lx/Hx3ooq2SjkpQA5A6V2fw7hjfU5ZGQF0T5Se2aKKT2BbnpeMq2aqWhP2yT/AHP6iiipjuVLYtOTisrUYo57OeKVA8bIwKkcHiiitkczPHpZGBTn+Bf5UUUVN2bH/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Why is this a funny picture?')=<b><span style='color: green;'>hat</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>hat</span></b></div><hr>

Answer: hat

