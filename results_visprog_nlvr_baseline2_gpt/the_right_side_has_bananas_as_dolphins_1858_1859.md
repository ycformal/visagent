Question: the right side has bananas as dolphins

Reference Answer: False

Left image URL: http://2.bp.blogspot.com/-dL4sDwtqjOA/VplywZVqX1I/AAAAAAAACPQ/ags4vLsyHpo/s1600/IMG_3396_1.jpg

Right image URL: http://1.bp.blogspot.com/-QKOmKuS2H_s/Vln1yBMkBDI/AAAAAAAACKU/ZpzRZsX963k/s1600/DSC01664.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are there bananas shaped like dolphins?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are there bananas shaped like dolphins?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABAAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzS61REtkLYzKnFQQ3hEYkAAKMGGOh/wAOpqiCY0WMHzD2L/wn2pCHfKxHaCCHAX/PNcqkib6nZaferJp6THhCO/Wq186TIsqE4JHWsJZpbWHaZT5eBlWwRn+lamj6ZqGs2srxBEjjlVSxOcg8kge3H51MqiSu9jejRnWlyU1dmZfSAX9shHRQB+Ga02bdbOcniqN14d1aSWKZoQJAjuATzhW24/E9PrWn/ZGq2+irdzwq0cszW2xDlg68HjH1/KqclK1mE6U6es4tENurSW7HpxVS43LdDHC7ME9vvGuu1bwLrui6AdTintJrVYRNKFbEkYxzwRg49qzfCHgzVvE+uwie3ljsoyktxNOpUFM9Fz1Lc4xTi6fs3VclZbmbUk+WxiXLSw2qu8EuxiQH2EDP1qKBGmgY/d5+XFe8+INA0u9ea3lhxHMpzt4wc4BHuOPyrg9G+GuqzaultO8VvYKu77WxBDrkj5R3bjp271zYHMsNiIS5ly279jSrQqQa8zzSSZ0mO7+E9MYNMX5YZAxyA2cA9fpXT+J/DkljcNFLlcMQky8qfb/61cnNvgYxOCpx1P8AF9PUV1yjeKlHVMwknF2K00/mSsxkxnsDRSB5X5j2lenKgUVVw0OksYTdXKWtvGWeQ4CuwwPXtwK1L3w5bWw8ue+sgccJk7ifzGa6rwDodjd+LpI2IybOUiPuAcLuH0zXWeB/hbYeHdbn1XVZkvL6ORltw4yFU9HOerkflWVeolWdODSsr7Xub04px5pK55DcaHqdjai4m0m5itTyJntWVSPXJHFdVp4/s7RLTapaSSEyOB2yc/yxXtGu3ZFpdQRkq7wtGFYBkbI6kHrXE6dYabceFz9otYYDYx+S7oNudozk5PXBGea5Mbjqajytap9D1cpqrC1XUkr3R5/Jr8qxKqcEKRnvk9/yrvE0+xtvhmmoXP717oK7EZ+UMxyB6H1Pc1yFw3hK0iiuRcJMrPgBSZOepyPT1ra1LxDa69oFzoduYYwAI1jhYKE5yMY6DvXkyle3LFpX3PWzLG0sXGMacdnc6/Rb2K90K0WRBsGEIcZVlzwfQj/Cti7vJk1lLczbkRVYKD0ByOn1FcXo0B0XwRBatIXaGH7w5y3Xj8aoWQuv+EqbxHN4jieKeNbd7FlBbgYCDB6g5OcZ5NYScXTq00+unn/w543K+ZOxseMk1G4iU6aAZkcZBk2fKevNV/CNpq0Ml8us3STRSqpSBQWIYfxA9j2rUuruOQj5wCWC4b19KiNzeIHGnmASsuA8wJVT+HJ+lc+GxEqUVGysa1Kaep0unaZpt5b3Nrf6fDcQ7iGDruPIHHqT715R4x+G0NjeyQ2MsNxasQyxNMPOhJzx9B69/Su+0ia70izitp71tQuZZcSTlRDGCepIHOBU2pQWc9rPC32YTsMriILn0O4ZIPvzXuUMfKnSUaaulpd7fdozhqUVKV5HzrdeEdatZzFDCZIxyGH/ANaivVLeNniy7kHOM9M+9Faf2m+tPX1J+qR/mE+FlkR44uJnkIdLDKIOsg3gMPwyD+Ves3lwjSsYzhl4II6exFcn8NtBhgtE8Ry7/tEyvDCuflEeRk47klf0rsdRsYLyNnJNvclcK68EfUdD+NbZlQdSfNTdpIzoOy1POtWufEB8dxzYh/sI221yzjIf6dc9PbBq3qemRX/ha+s87Fu9zEp1zxg/oKuXNjdpcm0uoHkK7ZBLHGdrDP8A9auf0WbUZNNuo2iupkWeVEd0bLc/w56gdAfavBxKryalJWkrfM9GkoLqc5D8PNNhiBmuJpZVJZpM7Sc9qraNpY0+58QTSC1Fvc7Vgw/7xSp4wO3XH4V6Ra6HFf2yyveqscoziPk/iT0rQ8N+G9D0ZbmC423kl1IG33ShlGOgA7Y9e9b4arVqycJztfuFWUI6pXsY+gzR3WrWVtKfkALcjg8cV2h8NaE8rXQ0m0iuc489YFWQHGM7sZqvrkVlJYyCa3DRIDteP5XT3BFeUQeMpvDXiYC1vf7Q0yW3MufN3CRc4B5OAwPGRivUoYdYeLhumckpe0fMtD0eDwPp2iC6umvb29aWQyt9tkWQBuwAwMdvyFPstH0+/lmkYSQxt8rpbts3EjqSOR+FchrHxV0hbNi90ADgiPeGc+gIXP51yDfGaCwVvscE00zZO/hVU9seorJYVVcTzxj7qXyuDqOMLN6noN34T0/Q9Onht5pblWIPmXEm5jg5AJ749q5DWJ/LtT/Z07ZUjkzgLGO5LdhXHa78TvEniRoxZr9jgRfnCgNuJ7kkflXCNDczSSPIxO45aR2wCa6/qMXK5H1h2PabexutSto7mx1/yLcjCgQ7w3+0DkdaK8ks4ZjBiK/dUBIAWUoPwGaKx/s2a0Ul9yD61c9s8GfFnS9Ggi0PXFaGKCTbDcbcrtJzhsdME5r1+Fobm6jkWQSRnLqwbIY4yD718ueItLj8vAiXzMnnGTWbo/j3xN4UgWztbsmBOY0lG4J9Pb26V6lajeRy06nun13hXtx84Pz/ALzn3/wp0nlbpQzAJIu1T247V8/aP8dMWo/tS1kW4Tr9n5WT8zwfzp83x3CXiJFZSy2hXksArKfQDODWHsX2NedHtOsWltcIjQyCCZF2KQOOB0PtXFatd3GmQyS3qhYFGTMDmPH17fjXl+q/GPV2vZjZWypH/C8wO4j/AGgOKwtc8ca74h0kWcyRQwMo3iLdl8c9zxXNiMup13eWjLhXcNFqeial41h/syezTU0SGWNkzuDbcjGRXj91eWdjZT2OnyyT+cQJJ3XaNoOdqj696zktJGODhT6dT+QrTt9EZwGMZPvI20fkOa6cPhHSVnJtef8AVyalZS2jYz49Nu5I/METBCM5PpVm0swr/vU3n+6Bk1rXVveXRUSXpO0fcCYX9KtWMi27YeAIuTlUbIPvXVbXUxKP2gLaxbYDDZbtrup3Pn0PofQGrdnb2koYQTQXSScbpgY2jGOhB4H1BrZSxW9VntvKfeu11LclPRlPX8azbvTm05TDFbQncOUxKT+I3YxVbCFGlXlnmK3k03ys5XzZ48n9aKppO0g3f2Zpk3P35YnDH8N1FTeIj//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there bananas shaped like dolphins?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

