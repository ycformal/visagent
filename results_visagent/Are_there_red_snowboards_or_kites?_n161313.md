Question: Are there red snowboards or kites?

Reference Answer: Yes, there is a red snowboard.

Image path: ./sampled_GQA/n161313.jpg

Program:

```
 Are A or B?
Program:
BOX0=LOC(image=IMAGE,object='snowboard',color='red')
BOX1=LOC(image=IMAGE,object='kite',color='red')
ANSWER0=COUNT(box=BOX0)
ANSWER1=COUNT(box=BOX1)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} + {ANSWER1} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA4AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDI20u2n7aXbX0R4AzFKFp4WnBaAI8UoWnhaULQMbilC07hQWYhQOpJwBTztRN7MqoBncWAGKm40hm2jbVWK/8A+JiyzvAljIpW3kVwS7jrk5wBj+YrR8pv7p/Ks4VYzvy9DSdKULc3Uh20oSpduKULV3JsRhaKl20UDsVdtGKfil21ZkMC07bTwtKFpDGbaXbUgWl20DIniSWNo5EV0YYZWGQRWBqPhnTYLOa4t7aV5sbY4vObaWJwOM/1rpGwiM5BwoycDmmyl3tsRxFmbsxAA75NcmKqUoxala9tDuwmGxFRc9OLcb62PNdO0d9R1qHTLiKaIDJlJHKjGT7c8V2sHhWzgwBdX5UdF8/AH5CnT6c1jGL43EhmkZPNR8FScdvTgYrbiIkhjcdGQMMHPUVz4aGrjNa7lYib0cXpsQxQiKJYwzsFGAXbcfxNSBalC0u2u847EW2iptlFA7FHbTgtSBKcErUxSIgtOC1IEpwSkNIj204LUojp4jpXKSIQvNO2A9VFTCOlAG4KOWPQDkn8KznGMlaSubUqlSm7wk0/LQqtZRFAoUYDbgGG4Z9eadBHOvyybAi8Ljk1swaDq1yCYtOuNuM5ddg/XFXE8JapsElx9nto84LSS5I/AZ5rlVOjCXNF2+Z3SxderTdOcVLza1XozCVMnFKYjzx0rpn8G363hjhfdAFUGaUbfn74AySPyrorHwtp1sqrLF9okI+Z5OfyHaqliYLY5o4eT3PNcc4wePaivTI7LT4ZZ447ZFVXAxsP91aKz+uLsX9Vfc8w8ul8uiiu+5w2HeUacsRPAUk+gGaKKTY0jTtvD2rXLKEsJUBGQ0vyLj6mrCeFtZaYRG0CdMuzrtA/A0UV588VNO2h3Qw8GrnRWXgazjKm8nmuWznan7tP8f1rorbT7SxTFpZxxDnmNAD+fWiiuWdWc/iZ0RpxjsiUHLbDkNjOMU4oq5IC5659aKKgsRtzKMHB/Q04kjkYoooAoYLXNw20jLg5U4z8q0UUUAf/2Q==">, <b><span style='color: darkorange;'>object</span></b>='snowboard')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA4AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDI20u2n7aXbX0R4AzFKFp4WnBaAI8UoWnhaULQMbilC07hQWYhQOpJwBTztRN7MqoBncWAGKm40hm2jbVWK/8A+JiyzvAljIpW3kVwS7jrk5wBj+YrR8pv7p/Ks4VYzvy9DSdKULc3Uh20oSpduKULV3JsRhaKl20UDsVdtGKfil21ZkMC07bTwtKFpDGbaXbUgWl20DIniSWNo5EV0YYZWGQRWBqPhnTYLOa4t7aV5sbY4vObaWJwOM/1rpGwiM5BwoycDmmyl3tsRxFmbsxAA75NcmKqUoxala9tDuwmGxFRc9OLcb62PNdO0d9R1qHTLiKaIDJlJHKjGT7c8V2sHhWzgwBdX5UdF8/AH5CnT6c1jGL43EhmkZPNR8FScdvTgYrbiIkhjcdGQMMHPUVz4aGrjNa7lYib0cXpsQxQiKJYwzsFGAXbcfxNSBalC0u2u847EW2iptlFA7FHbTgtSBKcErUxSIgtOC1IEpwSkNIj204LUojp4jpXKSIQvNO2A9VFTCOlAG4KOWPQDkn8KznGMlaSubUqlSm7wk0/LQqtZRFAoUYDbgGG4Z9eadBHOvyybAi8Ljk1swaDq1yCYtOuNuM5ddg/XFXE8JapsElx9nto84LSS5I/AZ5rlVOjCXNF2+Z3SxderTdOcVLza1XozCVMnFKYjzx0rpn8G363hjhfdAFUGaUbfn74AySPyrorHwtp1sqrLF9okI+Z5OfyHaqliYLY5o4eT3PNcc4wePaivTI7LT4ZZ447ZFVXAxsP91aKz+uLsX9Vfc8w8ul8uiiu+5w2HeUacsRPAUk+gGaKKTY0jTtvD2rXLKEsJUBGQ0vyLj6mrCeFtZaYRG0CdMuzrtA/A0UV588VNO2h3Qw8GrnRWXgazjKm8nmuWznan7tP8f1rorbT7SxTFpZxxDnmNAD+fWiiuWdWc/iZ0RpxjsiUHLbDkNjOMU4oq5IC5659aKKgsRtzKMHB/Q04kjkYoooAoYLXNw20jLg5U4z8q0UUUAf/2Q==">, <b><span style='color: darkorange;'>object</span></b>='kite')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>4</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER2</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 + ANSWER1 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 4 + 1 > 0 else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER2</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
