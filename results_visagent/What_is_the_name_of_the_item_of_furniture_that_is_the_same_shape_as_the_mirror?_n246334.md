Question: What is the name of the item of furniture that is the same shape as the mirror?

Reference Answer: The piece of furniture is a nightstand.

Image path: ./sampled_GQA/n246334.jpg

Program:

```
What is the name of A that is the same shape as B?
Program:
BOX0=LOC(image=IMAGE,object='mirror')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the name of the item of furniture that is the same shape as the mirror?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='mirror')=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCADkASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCqvh7TfEPj3UItU3mJLKKRdkmzDHaOv0rfPws8JIpZxcKqgkk3WABWLFx421D/AK87f+YrstTwdNvP+uEn/oJr18XmGLpTpUqVWUY8kNE2vsoUKcGm2jmR4M+G3/QXh/8ABmlL/wAIX8Nv+gtD/wCDNK53w7o2mXPh2znnsIJJWUlnZeT8xq4+gaT2063H/Aa6a+Y+xrTpPEVbxbW66O3clQuk7I1P+EP+GwIzqkJ5/wCgmlSDwb8NMc6pB/4NFrC/sHSv+fCD/vmo20PSx/y4Qf8AfNZf2sv+f9b71/mP2fkjof8AhDvhn/0FLf8A8Gi0Hwf8Ms/8hS3/APBmtcy2jaaP+XGD/vmoW0nTv+fGD/vmj+1l/wA/633r/MPZ+SOsHhH4Yjrqdv8A+DQUf8Ip8Lh11O2/8GYrk107T04On2xHulSLZaT/ABaXb/gKP7WX/P8Arfev8w9n5I6f/hFfhd/0E7b/AMGdH/CK/C7/AKCdv/4Mq59LLQ++nW4/3o6sJpehtyNNtW+i5o/tZf8AP+t96/zD2fkjXPhb4Xf9BO3/APBlR/wi/wALv+glbf8AgyrOXSdCPXS7T/vjFSDRdBP/ADC7Yf8AAKX9rL/n/W+9f5h7PyRdHhf4W99St/8AwZUf8Ix8Lf8AoJW//gyqqugaG3TTLU/Rf/r0f8I9ov8A0C7X/vij+1l/z/rfev8AMPZ+SLX/AAjHwt/6CNt/4MqP+EY+Fv8A0Erb/wAGNV/+Ed0T/oF2v/fFL/wjmi/9Au1/74o/tZf8/wCt96/zD2fkif8A4Rj4W/8AQRtv/Bkalt/Bvw2u2Zbe7jmZRkiO/LY/Kqn/AAjei/8AQLtf++KydJtYLPxnqcFtCkMQgiwiDAGcVccfUq06jo4ireKvq9N0uj8w5EmrpHUnwD4BH97/AMC3pp8BeAPU/wDgY1REEmmFGry/7XzD/n9L/wACf+Zp7OHYsf8ACB/D/u3/AJONR/wgfw//AL3/AJONVQxN0pyWzk0f2vj/APn9L/wJh7OHYs/8IH8P/X/ycanL8P8AwG4yoLD2vGqv9kc9jS/ZJ0O5cgij+18w/wCf0v8AwJ/5h7OHYn/4V94E/ut/4FvS/wDCvvAn9x//AALes25vZoFIZSSPTrWU+v3UcjRtGUdSchu1H9rZh/z+l/4Ew9nDsdP/AMK88Cn/AJZv/wCBb0D4d+B+8cn/AIFPUelW97qVmJhdpGxJHlnIP8v61ZttOVrww3stxn0TH9c0f2vmH/P+X/gTD2cOxCfh94EHVXH/AG9tSf8ACv8AwKeiSf8AgU9dPBoWnKquqSOGGQWkP8hirken2cf3LaIfVc/zpf2vmH/P6X/gTD2cOxxZ8AeBAMlX/wDAp6mi+Gng6dA0VrcOp6EXD4rptZjUaaQAANy9BiiwuIodNhDPzg8Dk9TR/a+Yf8/pf+BMPZw7HOH4XeEx/wAudx/4EtTT8LfCv/Pncf8AgQ1dWbuNsbQevepFmDjhTR/a+Yf8/pf+BP8AzD2UOxxE/wALPDbsvkxTp6gzMc1k+AECeHXQdFuZB/KvTUX94DjrgV5t4E/5AM3/AF9y/wA661jMRicDVVeblZwtd3/mM5QjGSsiGPjxnqZHe0tif++lrsdSP/EtvP8ArhJ/6Ca4/p4v1M/9Odt/6EtddqJ/4lt5/wBcJP8A0E1hj/49L/DD/wBJRpT+F/M4rwv/AMitYf7jf+hGtB6oeFf+RXsf91v/AEI1ovWOZf77W/xS/NhD4F6EDVC9TNUL1xlERqFh7VMaibrQBEV5ppSpTTG5zQBCy+lMKntUvUkUYpgRiWZBw7fTOact9Op7H9KeVGKYYweKQE6aqw+9n+dWU1gHADfhn/GqH2daaYwOAKAN6PVEP3sfyq3Fe27/AMWP1rjZQUPBI+lVWuJQeHNFgPSI2jkHyOrewNYFgmfH2rA/8+8P/stcqLu4/wCezj8a6fwyTJ4su3Ykk2FqST1J2rXoYFfu6/8Ag/8AbokT3XqdB5fPvS+TxyKtbfnNOKV5xoV47cMavQWygk4pkS/NWhGPl/CkIZHbrnpTpo12Nx2qccVFOfkIoGcfqKj7SwIrGvIt9zaPjLFMk+vztW9qKDzmJ9ayJAD9jb/pjn/x5qoR6Do2nQTaDaHlWMf3hUCRzR3wR9rBTgMRzitPw7z4fsj/ANM/6mo5VHnt9TUgX4QPIj/3RUuOajtwfs0fH8Ip5ZR95gPqcUAZ+tf8g1v95f50zT7aKbTISyjPPI69TTtXeOTT3RZY87gfvUukyoulxA7sjORtPrQMmWxjHRmqZYlTpTkkySNr47fLinhge36ikBHnBBwTjBwoyeteZeAx/wASGb/r7l/nXqCENIuPX+teY+A/+QDN/wBfcv8AOvTw3+41vWH/ALcZVPiXzK5/5G3VPaytf/Q1rq9Q/wCQbd/9cJP/AEE1yv8AzNurf9eVr/6GtdZqP/IMu/8ArhJ/6CarHfx6X+GH/pKHD4X8zjPCw/4pax/3G/8AQjWhJxWd4W/5Fex/3G/9CNaEg5zmssy/32t/il+bHD4EQtULdakY8VCx9a4ihrVE1PPWmkcUwIzSGnGkIoAYRRinEUYyKAG0oWnBelPxxSATHFQseamYcVC4oApz9az5PvVoT9azpPvGmAzPFdX4Wb/ip7on/oH2v8lrk810/hck+I7o/wDThbfyWvQwP8Ov/g/9uiRLdep2e75vpTt4quW5NIWJrzSy5G6561bSXAwDWSuScZqyhbHWgZoiUAdaxdV8XaJpdw1pe3nlTgBtnls3BHByBitBVLDrXN2dvFL8S79ZEVwNNjIDAHncvrXbgaFKrKbrXtGLejSe6W7T79iJtq1jLvfGGgzbil9nP/TJ/wDCqVvqlrfpE1tIWESeWxKkc5J7+xrrdWsrX7rW0JH/AFzH+FeeaQAl1qIUAKLlgB6V0OlhKuHqVKUZJxtvJNau3SKJvJSSZ6rpOtPbaNaxBXcqnG3aO59QarXWq3Dbm2zLlupkJHPbgCtnwjgaRGDwduf1NU/En/HpIcniZCOf9qvKNCO2m1VoEUWDPgfeZHOfzOKtLFrDji1jT/tkg/nW5augtI9zKDjual86IDmRP++hSA5nUYNUWzMl0/7pWHAYdfoKm0yyvLizSRbrbE2cAsfX0q5r08b6PMFdSQ68A9eaXw/PENGg3SAEFuPxoAVLF0l2NOxPspxV5LQIMFyfwpokV7oMrZGRVvrSGRIoWYAe3868z8Bf8gCb/r7l/nXp68Tr+H868w8Bf8gCb/r7l/nXp4b/AHGt6w/9uMqnxL5kIH/FXav/ANeNt/6MSus1If8AEsu/+uEn/oJrlV/5G/WP+vG2/wDRiV1OoknTbs/9MJP/AEE1WO/j0v8ADD8kOHwv5nF+Fv8AkVrD/cb/ANCNXZOKp+F8Hwtp+AR8jZ5772q7IKyzL/fa3+KX5scPgXoV2qMjmpWFMIrjKISvPWm7etSEU00AM2/SkIpxFBHFAEeBTakIpMUAAHGaeRxTRUmOKQDGHFQP3qw/Aqq/egCpP1rPk+8avzVQk+8fpTAjxW34ZvY08TTocgvaQIvuVAOP0NYdbXhm0WTxLLIzY2WsLggDIyAMjPfmvQwP8Ov/AIP/AG6JE916nZ2832m2in27fMUNtznGfepO9R28H2a1jg3bvLXbuxjNBbBrzSydTzVuMjAqgjc45q4hCgFjtX1PAoAtDpXOWJA+Jt+f+oZH/wChLXQLNFj/AFsf/fYrmrSVB8Sr0ghg2nRqCGH95a9LL0+Wt/gf5xIn09TR1s4BIrzjTDi71P8A6+Hr0TXfuGvOtO4vNTH/AE3ejC/7pX9I/wDpQS+JHruilTokBIycE1B4hcDS5D/tx/8AoQpugtMtjCCu6F4lxyPlPf8ApTPET40ycejJ/wChCvNLNONsopIGcdxUoPSmRIWt0YdMflzThkEqw5+lAFLWnxpUp91/mKXw84bSIzn+Jh+tRa+caLMR6p/6EKZ4YJk0WMDrvf8AnR0GdHHgkGr0UmQAevrWbFIAPvL/AN9VcQgjPB+lSBN/y8L9B/OvMfAP/IAm/wCvuX+delxtm5UZ7f1rzPwD/wAi/N/19y/zr08N/uNb1h/7cZVPiXzGL/yOGs/9eVt/6NSuo1HH9mXeP+eEn/oJrmF/5HHWf+vK1/8ARqV0+o/8g284/wCWEn/oJq8f/Hpf4Yf+kocPhfzOM8K/8irYf7jf+hGr8g5qj4U/5FWw/wBxv/QjWhJWOZf77W/xS/Njh8KKzioyOamYc1G2OtcRRCeKgeaNSAXUH3NJdTmNTjrXJSCC/wBfAvlLxLF90HBPPAH512YPDwrzkpyskm3ZXenldfmTKVtjr/MQ/wAa/wDfQpxFZGt+GdKtvDI1WyieGaK7jgYFywbcCT1PsK2WIyfrV4rDUadKFWjJyUrrVW2t2b7ijJttMiPeilI5pQK4SxFFSU0ClPWkA1+lVJD1q23SqcpxmgCrMcH3qhJ941Vs7O11C+1H7ZI0e3eVk8zAUhSRx35Aptgc6fETz8p/ma9TF5fChR9pGd2nFNWt8UeZa3d/uRnGbbtYsCui8Ln/AIn91/142/8A7LXOCuh8MHGv3P8A142//stRgf4df/B/7dEct16nVyzBWNUbu4BtpsH+Bv5GmXM212571nzz7opB/sn+VeY9jej/ABI+qF0vSbe8tYGYztLJwFSTGTnAAq1448KWWleC7u6WSdriNox80mVJLDOBitnwHAHgguGH3CEX9c1Y+KmF8C3wHd4f/QxXVktOH13Du2vNH80ehmmPxXtK1P2j5byVr9LvQxrL4aeHbmO6LRXGY8FMTH/CuG1fSLTRPH1hZ2SusQlt2w7bjksM17boy/vLsY/uZ/KvKfHcYj+K1mB3e2P6ivpMgx2KrYqpCrUlJcktG2107niV7cqslv2R2Gv8xtXnGnnGoakP+m8lej6/9xvrXm1icajqP/Xw9eJhf90r+kf/AEo0l8SPVtJVv7P0/DsqmNeAareImxY3oBPysOT/ALwqayaSPSdOZG24hByOorP12Rn068YgsWxnn3FeaWdCI1n0tFP8RAyenU0kFoYiSg49fWs77TLHEirK/l4BKdB1qS81aaK1ja32qPUluM/Q0ASeIUK6Bck9tp/8eFV/CBZtFRh2mb+lZmp6td3Wm3EUqKqOoI+ZifvD14qLw7fXkVikFuqMCztl2K4P4Gn0A69IHCgvJwucn8a0rf5Bgtzgd6woby7EC+Z5Ykz83zEjHccd6vx3TKwG0E4x+FSM0oWJ1NF7GLP61534A/5F+b/r7l/mK72zkL6xHkY/cE/+PCuD+H//ACL83/X3L/MV6WG/3Gt6w/8AbjKp8S+ZGv8AyOOtf9eVr/6NSun1D/kG3f8A1wk/9BNczHx4x1z/AK8bb/0aldPqH/INvD/0wk/9BNXj/wCPS/ww/JDh8LON8Kf8ipYf7jf+hGr0vWqPhT/kVbD/AHG/9Car8lYZl/vtb/FL82OHwr0IDnFRMDU1NNcZRnXEJcdM1zlxpd+up/aLS1EqmPblnC4OfrXYHGaYa6cLiXh5uSindNNO9rP0aFKPMcdeadrV48Ye0SNExwkw55zk8811jfe4pTSGrxOMdeEYKCio32v1tfdvsKMbO42loyKCRiuMoM0E8VEWHrQW460AOduKpytzU8jjbVCST5qAMm50vdNM63MqCUksq9KSKIW8KwhiQoIyRVyaWqLOS9dlbHYivTVOpK6Vui6Ky2V9iVBJ3RKtdB4Z/wCQ9c/9eNv/AOy1zitzXReGT/xPLo/9OMH81rXA/BX/AMH/ALdEUt16ly9lPmyDP8R/nWe03yOP9k1PfN+/k/3j/Osee68p1UIZNxxgdR715r2N6P8AEj6o9X8GKkHh3TyzAbiXOfdjVT4plJPA16ysrYaLof8AbWr3hL/kXdLJGOP/AGY1V+KX/Ihah9Yv/Ri12ZL/AL5h/wDFH80aZn/vFb/FL82bGnTxQSSrNLGpKIoJON2B1/WvJvHtzEfidaTrKrxr9mJZOehGa9NvYGeRnZcooDZ3D+4O3WvJ/E6IfiTZx7QUMsAKkcH5hXr8Nf75U/wS/Q4a/wAK9Tt9VvrC8XEWoWmT2aTaR165HtXB6baNcX2plJ7UD7SygvOq5yeoyeR71f1i6tl8ZXmnC2wwuD8wwFAOw4x+B/OsjTokP27I5FxIPyHFclPD1KGEq+0VuaMGvRy0ZTknJW8z1SwaN9Gs0SaKR448OI2345/2c1natMYLOd8sSCMED+fpWl4ahjTRyyRqrGRgzAYJxjGaz9d/49tQHfmvINC5FBvbcswCbQAuDwefb6U82Xmjy5LgmL+6rYP6in6O5YMM9q1Rnk8/nSA5rU7BI9KuZDJh0TCkMCAM8ZGM5qr4ejeW081di5lfeC+3rg4H51ua6CdDu+P+Wf8AUVmeFB/xKn/67H+QpgbKRNtwDFk9gwq7FE+CAF7D74xUajB7VYhAMoyAfl7ipYyzYsF1dIsqW8kk45x81cJ8P/8AkX5v+vuX+YrurbA1yDAAzC/Qe4rhfh//AMi/N/19y/zFelhv9xresP8A24yqfEvmQKX/AOE01vaM/wChW/8A6NSuq1Fv+JdeDH/LCT/0E1zNt/yOuvgD/lxt8/8Af2Oul1Ef8S68P/TGT/0E1eP/AN4pf4Yf+kodP4X8zjvCjf8AFK2A/wBhv/Qmq/K3NZnhbd/wi9jhSfkb/wBCNaEiuf4f1rHMv99rf4pfmxw+BehGW461GWz6UrI/sKj8tj/F+QriKELU3d1p/kMTxuNH2V+pUgf7TYpgQM3amFuOtPlNrCf3t1bR/WQZqJb7TTIqLeLIxPAjQnP44oAXdkcUckdK2n0dY1lLzxmSOPzjEr5bb+VZ2UH3YAf95iaQFEhvSnBHYYAzWu32T7IVijcXQRWYkLsGcZwM5796ZY+Y+oWyOxZGlQMuAAQSOKAMv7JcOMCNj+FQtpc2cu8aD/aYCuh8WrGmn27RsmRPIreXH5fTHHvjpmuO3qDzQBZk023z+91GBfZct/KoDaaNEcyXtzIR2ih/xNQySqB1qk8wLYFMDTB0Yfctb2X3kmVB+gNaOgMh8QXpjTy0+xQ7U3btoyOM965+Js1u+G+dbvP+vKH+Yr0MD8Ff/B/7dEiW69RL8nzpP94/zrHuGWGOSUru2gmte/H7+T/eP86xL85s5v8AcP8AKuTDwjUrQhLZtL8S+Zx95bo7bwt4q1C30Kzjg8MaldxqxKyw/dfLE8cUeOfEWp6t4XubOXwpqtkrlP30oyow4PPHtj8a1vh9cxjwpZxtwYXXd+PzA/r+ldubqHzoysyjGcnPTivSjjMLg8TenQXuS096XR6df0Cvz1ZylOWrbvt1PLJ/idbTddAvgwUKSJQOcY/u+1cVc6wut+N7O/it5I1M8P7snceGHoK9ivDbrqN01tcmVWuA0nPCOeo9+prxnRrHUY7i3v7P7OxkuPLQSMfvBgeQO1exleLwUaVbEU6SpySSV5uz5r91psRChKrVjSbbT7K708jpNX02NvGN5qklwyK0w/d+Xlv4R6/SseyIVtQ2sT/pUnbttNXdUPiA6pdG4jsBN5pL7CducR9PwC/rVWytLiFLprjZvlkaT5Dkchv6151ecvqs1Wqxk+WMYpNN2i/IhL3lZHqnhr/kCjH/AD1Y/wAqyfEDgC+TgEg962PCozo+P+mh/kKx9fYedfIRyCcce1fPmxoaGcvID6f1FbmOKwPDrBrmZfQH+YrpAvFDGZGuf8gS84/5Z5/UVmeF2D2VyVYsDcMQ3rwKueMxIPCl6YN27C7inXbuGf0rL8D7m0Ji5JYynr1xijoI6dcbsVPE371fdTUajmpUz9oQAfwmkxlm341q2/65P/Na4T4f/wDIvTf9fcv8xXdwcavbf9c3/mtcJ8P/APkXpv8Ar7l/mK9HD/7jW9Yf+3GVT4l8xtp/yO3iD/rxt/8A0bHXQ6tKsdhdKBljBJx/wE1z1nz438Qf9eNv/wCjY66doVknO8Blb5SDyCD1FXmL5a1N/wByH/pKHT+F/M848PeI9JsvDlnbz3AEyKQy+nzE1Zl8W6ZzsZG/3pAKqT6XYCaTFnbgBjx5Y9aqvYWQ/wCXSD/vgVpXrZfWqzqtTvJt/Z6u/YSU0ktC0/iy3P3HtV+rE1Wk8Tlul7Av+6BVaSzsx/y6w/8AfAqu9vZgH/R4f++BWX/Cd2n/AOS/5D9/yJpNeL9dSP4Pj+VUJr+GQ/Nch/q2aJIrYdIIv++RVSVYQeIU/wC+af8Awnf3/wDyX/IXv+QrXEGeJE/A1c0+7tUvIWkuI1UNySazVjRnwIlPsFrU0yyjN5D59oAm4Z3x8EfjR/wnf3//ACX/ACD3/I9NuvFejtZXMY1fTyptsIqyHcX2857flXEaXrGm2+r/AGm8uVmy2NmcowwepyMdv8iunSytZZb+GfwtY21tErCK4KJ+8+XggY7/AKfWuUvWsITIsemWoCEjeyDB/Skv7O7T/wDJf8h+/wCRqprumCaXN9B/qlAO4cn5e/4GhPEemW00c5vI3ETq5VG+Y4OePeuSN+lxEFW3skjU7eIEViAOvQk07T0hnvZ/NsRGdmURwGAGR7Dn/Gn/AMJ39/8A8l/yD3/I6jxH4mtdUgVYr2B4xJuQsQr85yCBkAAYwep5zXPoYJDl9RtUHvJmp4bS0BbfbwEdsotSiztH5+ywKn94xil/wnf3/wDyX/IPf8hiQaQxBm1mL6If8atRp4YiGTdxyn1aY/yFPhTTbfkaXbSNj70qA/pjitqG30mSyjc6RYh5BnAgXj9KL5d/f/8AJf8AIPf8jmb270qMD7NLbAZ/gNX/AAtNHPrN68LB0FnECV7cjNdlo+iaRcxkT6PYbgOP9HX/AArfstM07TNz2djbW7ONrmKJV3D0OOoqliMHSp1I0lK8lbW1t0+noHLJtXPNL5SZ5OP4jXPan8lpLnupAr17UvDNhfhnizazHncgyhPuv+FcB4k8N3mnWF3JcRbohGSssfzL/wDW/GuTBv8A2in/AIl+ZUvhZY8G6hHbvFaTFVS6t4lQucDevQH65I/Ku1srzVbKXDSxmBScQmNBk/UDP9a8t0+RBbWrMpcCFBgp19uD06V32meP4bONUk0dCVGPMR23H/voH+dZYyrBYipr9p/meh/ZuLl70abszYvL+/mPzxRICckrEF+nJ615Po9zOllZ7I02xXLOm7I3NuHU+nArvtR8aWuoXDSrZ3KR8Z3DPTjtXn+lXDNYWcasQI5nbBHGS3WtozjLLa1n9qH/ALedGBwWIo42m6kGtJP8P+CdbNcWcty895bozync5jmJwdqggDHtj8KsWtvol60iR21zuCknMm0dT06+vpXOiYv7mrejzanbzs8KafIzbUKzLIB8zAdQfUjtXMeQjqI7QXEcVrZuYTvwpJ38nHXj2rOv9J1m3SRriGL7OgYl0PbHXk1p/btY2hZvDdhddgLW7AY+wDr/AFok1qGJSuoeFtatVIw2yLeuP+At/SgCvBp+rRAT2SMvmKCeeeeex6e1WjceIrdQTBJKB1A6/wAq021jS7Kzhna9nht5B+7YncTx2Q88f/WqXSfFWnXFjEbu7hS5x84UHHU4PGcZGDjtnFIDmtT1jWptKngXT5UlcbdzoMAd/wBKr6Jqb6XpwWeH95I29wBnB6djXbanqumTaRdrHewMxhYAb8EnHoay/Bnkzafcq5QsJhgHGelAFe38SWshO4bT7hh/StCPVLVp0lEi7QuDhga220y0f71tGffZUTaLYMObdPwFIZHp93FdarbmI5Co+f0rifh//wAi/N/19y/zru7SwgstTtzCu3crg8/SuE+H/wDyL03/AF9y/wA69LDf7jX9Yf8AtxlU+JfMSw/5HjxD/wBeNv8A+jY66gtiUfWuXsP+R38Rf9g+D/0ZHXQu5Le+aWafxIf4If8ApKKpfCef3M+ZpNo/iP8AOqT+dJwiE10skUCO22JM5PUZqJ3x0GB7CuAo5z+zbyU52kD34qRNAkb/AFk6r9Dmth5Mck01VmkPyrgHuxwKYFGPw9ZA/vJHf9KsppOnxDK2sbH1f5q2LPSo3cGedmH92Pgfma3ray02LAWzidvWT5z+tK4zjXkihQrGscf+6AP5Vn+Yr6hAdwPzjvXq9v5Y4SKJB6KgFPltLS4QrNa28inqHiU5/SlcVjzLUNZGHCsN7JsJDZ45/wAa5K7k86XEj4ViTzxkV7BfeDdCvEI+yNbsf4reQp+hyP0rlb/4ZypJJNp98lxnpFcjYwHoGHH6CmmFjzbUHjiZYIYvL24ZnDctx+nU8VbsLyGSKZbpWMhAIKHBP19T2xxWzdaMLC6+z6jpxhmxwHJww9QehH0qVfIsU32qQBioJIjwVPp7/WquIjt7Oe3BnkgVlA+VD0X3I7mnqxbB++38KDoPrVg6nNLYXLzSbiIzgYGBn6VDYNHJAdw5PH4UhiorM2XOR/P/AOtV23kmMiLGxXPyr7DuaZ5QJ4cj2IqeObyJQWRW49e1IDvdLkEFgktw6rx8pfClvQ1HPqs0oAtLSaU+pwi/mf6Vh2Os22STbqsp6v8AeJ/E81oLrFvjLNz70hmnBLqEqjz2gjz1CAsf6Cor7SF1DT7q1e5uA1xE0W8ucLkYztGB+FQR6pbk/LIv51fhuY5BlXB/GnCcoSUo7oNzkYfhzdRRJHH4muVRBhVFuOB/31Uw+H9/gj/hKbvB/wCmA/8Aiq7JZAO9SK5PTmvQebYpu7cf/AIf/Imfso/1c4x/AGoSRlD4rvACOnkAD07NSWHw6l06FY/tcF0ihjwpidifU8j1rt8mpFkIGMVlWzDEVqfs5tW30jFbeiXcapxTujg5vCNzDFPJHZz5z8saSLINvfnrn04/nVyw0nTrWfY1zO63CGN0lgMbLxuz9cgV2YkFP80kYJJHua47l2MSzs9Sjdnjit54o3/dtOzRO4/vcAjP4DPWp9QW+vbYQy6feQFXD+ZZXEUnI7FWxuHsRWsDkUv4/rSAztMews7aOyk+0I5YnN7CUMjE5PONv4A1cn0fTLn/AF2nWkh/2oF/wp7RB0ZG5VhgqTkH6ipE3xIEUjaBgAjpQBi3Pg3RJ1IWy8g+sMjJ/I4qgPAGmL9y6vkPr5oP8wa3bm/vbfLLaRXKjtFLsf8AJhg/nU9tdLd20UypJH5iB/LkG11B6bh26UCMBPCE9v8A8euuXSegdAf/AEEirCaX4hg4TVoZVH98MP8AGt4P2FPB45ouMydOi1b+1YWvhC0SK4DxsDycewPauM+H/wDyL03/AF9y/wA69Lj5lX615p8Px/xT03/X3L/OvSw3+41vWH/txjU+JfMZYnHjbxIf+odB/wCjI63Xc7+KwrH/AJHXxN7abD/6HHV65u1R+W6HpRmn8SH+CH/pKKpfCY1xOA7cjqagy8oz91exNU7NzPP503KZO1fX3NXnlB5NeeWQkFGyDz60iyuHDE5pWYGkGAeKYF+11NoiAy8Gun04efGJMcEZrjUUsQoGSa7vTFSG1jjyPlUc1LGaEcYAxTiuKVCGb2pZWUDkgAdzSArsxBxzTCT2pkt/bKOGLkdlFUZr2eYYUrEv+yMk/nQBauoorq3aC7hilgPVZQCP1rktV8IafNGx02d4Zs5MbkvGfo3Vf1rYdCTuZmY+rNmkwffFMDjbzwfq66fIlu9tcMwxsRyp/DcAD+dczJJe6I4hvrSa3bHAlQrn+h/CvXopCvb8+Kkmfz4jE6xvG3VGUMPyPFFwseU2mswzMEdgpPQ9jWlHcxSkjPI611Nz4P0C9JMmnRxuf4oCYz+hx+lU/wDhX1nGCbTUrqL0WVVkA/LBp3QjH+RhwRSMrDgsT9as33hTWrLLQol7H6wHDfih5/LNYctzd2blLmGWJh2lQof1oA01DryDU8V3cwf6tiB161kw6qj8EirS38LAfMKANca/egjLNgfjV+28Vyx/6wkj3WufE0T9CPwNO2o3egDtrXxXaS48yREPucfzrWh1W1m+5Kjf7rA15kUUelORfLO5W2t6iiwXPV0micZDipdvHWvJLzWr6CNHS4lLZCLhyMnsO5JqSLxLqtt80jzQk9WC5B/AjFKw7nrABHQ08FsYIBrz6y8b3aqDI0c6+v3c/wBK3rTxdDOmZIXjHdiMj8xRYDpSQBytVZZ1DYQkewOQabbz/b22wgtkZyOg/Gql7qtvYTCC1Kz354Mn8MXvSAXUr9dKTkB7tx8kZ6J/tN/h+dUtAvXuBd+bcbpDIHMmMliR3/Kub1DUUCtIkrTzuf3ikZL/AE/wp/h2drCxmlnBa6uJAEgHLDA4H15NOwjtGv5YWVNiPI5wig4Lf4Vpo5KgkAHvisLToXgBluHD3D/eI6KP7q+3861kkPrmkMuwt+9X615r8P8A/kXpv+vuX+dejwNmZa83+H5/4p6b/r7l/mK9HDf7jW9Yf+3GNT4l8yO1bHjHxSfTS4j/AOPR1QvJ2kJ9KvW3Pi/xX/2Co/8A0KOsm6barH61WZ/xIf4If+koqn8I3T4ybYSn+Lp9KsyJyAO1CkJBEiDChRj8qaZj355rziyErg0qoxOKduVskGpIyedmAR396YFu2iWMgyKzMR8qKOT9fQVuyTyTvE5KDZEEI6e54rn4zIpyD16k96sx3LBhu7etIDoYLq4ji8vzc++ORTXZpT87sx9zWdHeZXjnHc1OkwPU4pWGTmM/WkCFaehBHXP0qYFVHP60gISnTrn2qIgAnAwfarvyvnFQOnPSgCuSfXNODMD0oeIgZxkUICB6g+lAEqSZ68VOvPQ1Vx3z+dTwkdufoaAJgpznP50AuowfmXuDzTDMoON2D78Um89wfqOaAIL3StH1LIutLtJWYcv5YDf99DBrCufAGhHJS5vrU9gJdwH/AH0D/OumBU9SPxpwyPunj2p3A87fwROt7tstZgkj/wCmqYf8lJB/StVfCZhTMtzcSNj/AJZxhR+pNdc8SyDDxo3+8gNNNsMYVSB6KcUXFY4xtNtoHInhvwp/iSRePfG2o5PD9zNCZtOvYrqMfwOPLcfUcj9a7M2svWO4mQ+hbI/WmxRXsMmXjjlXu3ljP5ii4HlbpeQashubdwYmHy9xwc8fgK0RqCF8H5W/I16Pc6VY6jDtuLcEdgedv07j8K4/W/C11aMraY7XAZgogeMMxJ7DsfyFO4GTmGVt2wBv7y/KfzHNKS+wpHcyRgnOQF3f99Yz+tWvFOif8I82n5kRZrmDdNCr5EbjGQD6c1jxSuefamBvade3dtcDfqt55ZG1grsevsTirVxeKIkgtMguA0hJyc/WsO0kPCrw7nA9TXc+G9DSFFvrlcueY1I/X/D86QEWleGgEFzeAgtyE6E/X0+laiafYwXbXUNnAk5XYZFQbtvpmtKRxg1VLA96QyWNvSrUb8VRUirMfseaTA0LQ5uU9a89+H//ACL83/X5L/MV6BZHNyleffD8/wDFPzf9fkv8xXpYb/ca3rD/ANuManxL5kdtx4u8WZ/6BMf80rGuiCGFbEH/ACNviz/sEp/NKxLgqM55p5n/ABIf4If+koqnsZ9trrNCvmwn5RglDnP4dquLf2843RuCOpHcfUVy8MzxDAAK+lSM0cpyDtf8jXn2KOmDejcVoQhdoAH0rilu7qBSoYuuOM9RXUadeLcWscq+wI9D0oYzWXOfap0Ct1FVUb5B7cCrcRCKSaQE6xA9KcUZep49akhXKLnqaeVPXrg4H1pDHxzCNQF/M1YjkB5k69gKqOuEGOppqluqk9aANX5duRgGml2zyM1SS4YNgkD3qytwAvzD8RSAeGRuDkUeShHBGPSoxJFIpKHn071C2/14oAleN1PyncPrUbLIeo/ShJDxz+RqUSN3GaAIt1wowNrj0PNM84qfntpE94zVoTRnrj8xSlox0IH40AVluoz/AMt3HtIn+FWIZVc/I8bH/ZOD+VM327HBdc+9O+zW8n3XQn60AWN7p1yPrT1nGexqqIZoR8hJHpu4p+8Y/eRKaALokVvUGn+aFHWs5pY1X5CQf7p5qFbgv95gFHX2oA0zMHOFx7n0rOvfEUGmyG1sUFzfnKs3aP6/4fnzxXO3/iCW8lNlpTFE/jnB7eoP/s34LjrWdHLHZoYoep+WR/X/AAHtTsIu+I9Otdc01ZRKj6pCeZGP+tDHlT+PT8u9caumahbcrFIV/wCmbbh/Wrv2lx5uXIBUc57gg1JHfu0m7dkk5NUBseErGKTNxdI3yuUPmdSBjA9h6+tegLdo3AOPauAtb+RlABP51vWlyWxknJ71LA6BnB6MPxqBmO6q32nHfpS7w5GOlAFlSQe9W4vXNZ8ZYtnNXYnOelIZqWX/AB8x/WvPvh//AMi/P/1+S/zFd9Yn/SY/rXAfD/8A5AE/H/L5L/MV6WG/3Gt6w/8AbjKp8S+ZHD/yNnis/wDUIT+aVz1y2c10CHb4o8Wt6aOh/VK4i/vJ3dlUhFzjjqavMlepD/BD/wBJQU3oZTSAdOahdyaeykZqMj0rzyxVuHTjOV9DV6x1RrdiEIAbqrf0NZxWo2FFgO/sNWguVCZ2yDnYevXt61tROHBUHOTXlCTyRYwcj0Na2n6/PbSKRKRj+F+VP41Nh3PVoMZz+FTxpnZnrn/69c1pXiW0uFVJW8mTH8R4J9jW/DdRuCA4PPBFSMmZAzYHrgGhYV25XjqaecHAHQcmp44yVx64H60gKMkBUZxnvVN3mDHYSBngDvWteY8o+7BfwqiwzlmH0HpTAqLPcL/AR74qVb6UfeTI9qBlRwxGPSkDyMcZBA9QKAJ1u4m+8pFW4XhblGI/Guc1DW7TTWzdPGAfuKuckfQUun+LbC6+RBj8CKLAdSbVH5ZFY+oFNNqg6ArVKK/iYB45eD3ByKuR3yHhnX86QET2vsDUYiZTwK0EeOQfKwP0prFFoArLJt+8CPcVHNcYHDZpJ5hyEP1FYupapBYQl3cnPCov3nPoo/r2piLU2oQWkL3Fy4SNOrMcD6e5+lYF1qNx4gl8i2R4LPqyydT67vb/AGfz9KzALzWrrz5iFSPO1V+7EPb1b/a/KtvEdsiW8KhVB2t7n/8AWKYFZvLghENvnnO9ieWPqay7i5kWR44U3ytjjOAPcntV64mWFSi8uScCsW51BYTsgKtL/E2OAf6mmIS+j+zR2yM+6VlLSY6E5447Ci2wxGCc1SQNLJuclmY5JPU1s2dvjBxQBp2SMmO9blu+AKzbVNuMjFaMY4yDSGX439DkVKJBkY4qkDsFSK2MHNAGnBJxitCNhjrWRE/Srkc3YipYzXsZD9tiGe/9K4f4fj/in5v+vyX+YrrtNkDapAP9r+hrkvh+f+Kem/6+5f5ivSw3+41vWH/txlU+JfMrkZ8SeLhz/wAgZf5pXEXEZZzx+leg634W0zUVv9QmF19s+znZ5UpAJUcDbjnpXAv4bx92C8/Jv8K6q7wdfllKo4tRirct9klvzImPMloihJGR2/Sq7Ljsa028NOB/x73n/fDf4VA3h6YZxbXf/fDf4Vh7HA/8/n/4B/8AbFXn2M5hUbA1oHw/c44tbr/v23+FN/sC6xza3Of+ubf4UewwX/P5/wDgH/2wXl2M0g+lIRWgdCux1tbn/v23+FNOiXQ/5drj/v23+FP2GC/5/P8A8A/+2FeXb8SpFPLAco2B/dPIP4VrWWs+WQC7wH1QnbVT+xbn/n2uP+/bf4UHRbj/AJ95/wDvhv8ACj6vgv8An8//AAD/AO2Dml2/E7bS/Et1DsEpFzD6j72Pr3ru7C9t7yFZYX3Kf0PofSvDRpF2OFhuPwRv8Kv2WlOTtmtNQQ/34w+PxGKl4bBf8/n/AOAf/bDU5dvxPZrmLJGQTxxxVaS3bbypA+lef23hpG2mWz1SRD/FG7g/kVrYh8HaTIo3Q60pPZi//wATUewwP/P6X/gH/wBuVefb8ToGiIGAhz9KqzhgwjweTzVAeANOf7qar+LP/wDE1E3w8thKR5WpHgkfO3P6UexwP/P6X/gH/wBsF59vx/4Bymn2c3iLxBLK88savKVXy2wQi/8A1sfnW5deGZ4WZoWW7UdBONko+kij+Yqr4d8CXFwWOoafqUXysRhWj5yMdvTNb5+G9uWO2HUse8p/wpujgb/xn/4B/wDbCTn2/E5XzrizuvKljmhc/dFx8hb6OPlb8a0oNTdSElBU+jDaf8D+BrWk+GduY/ng1Bhn7u8n+lUbz4YSSxg2iX0TL2lBYH+RFHscD/z+l/4B/wDbBefb8S3b37xBnRmAUZIIIrUh1QXUWVbkda5afwNfC1ER8O6kJhx51vdb0b32Fcj86zoPAHiAkhtJv1H0Io9hgf8An8//AAD/AO3C8+34nS6tra2ahI1Esz/djB6+7egrDgsLm/ma7vWJJHJxjI9AOy/zq5b/AAyvjtkls7zbuAdS+1sHvV9/hk38Ftfnjk+Z1o9jgf8An8//AAD/AO2C8+34jEURwSRou0bcAAVQ1K4EblR97cf0NaCfDKXBLWt/nHQS1z1z8PPETSkQaLf7PVmBz+tNUMC/+Xz/APAP/tgbn2/Ex7zUXlZkiY4PDOO/sPaoYIye1ba/DfxJ30e7/Nf8atQ/DTXDjzNKvF/4Ev8AjT9jgV/y+f8A4B/9sK8+xRs7UnGQa2re2PHymiL4aaj/AB6ffD/toP8AGrsfwxnP3rW+H/bYVPscD/z+f/gH/wBsO8+34liGBtvQn8KtxxnjKn8qpr8MTn5re/8A+/4qUfDFMf6jUP8AwIFL2OB/5/S/8A/+2C8+34lzy2HWo2V1boarf8KyXB/0fUM+n2gVF/wrQg4NrqH/AIECj2OB/wCf0v8AwD/7YLz7fibcEhxg9fcVKZWIOFJ+grAHw05/49dQx/18ClPw2AyPsmo/X7SKPYYH/n9L/wAA/wDtx3n2/E6jR7g/2zaIc5L/ANDWD8P/APkXpv8Ar7l/mKrWnw3Q6hALi21GO33fvH+0gYGD/XFdBp2lW2gJPp9l5nkJKWHmNubJAPWtebDU8NOjSm5OTi9Y22v5vuRPmbTaLqsUdWU4IORWomoTe35n/GiivOrboumB1S4Ax8v6/wCNIdSnyOF5+v8AjRRWJoOXVLjH8P6/40n9qXAPG39f8aKKLAPXVbjj7v6/401tXucH7v6/40UU7CEXV7nAPy/r/jS/2zdf7H6/40UUCAazdY/h/X/GlOsXX+z+v+NFFNIY3+2brPRP1/xpf7ZufRP1/wAaKKLCEOsXP92P8j/jTf7Yud33Y/yP+NFFFhiDWLnrtj/I/wCNH9sXOfux/kf8aKKLAINZucfdi/I/40HWLknGyL8j/jRRRYBP7YuAPuRf98n/ABp39s3Bx8kX/fJ/xooosAv9s3IB+SL8j/jSf21c/wByL/vk/wCNFFOwg/tq5x9yL/vk/wCNB1m5/uRf98n/ABooosgE/tm5/uRdf7p/xo/tq5z9yL/vk/40UUJCuH9s3OSNkXT+6f8AGg6zc8fLF+R/xooosMQaxc5+7F+R/wAaX+2LjB+WP8j/AI0UUWAX+2Lj+7H+R/xpp1e4/ux/kf8AGiiiwCf2vcZ+7H+R/wAaDq1x/dj/ACP+NFFCSAibVrgg/LH+VUmcvI8rctIdzUUVpTWpEj//2Q=="></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the name of the item of furniture that is the same shape as the mirror?')=<b><span style='color: green;'>bed</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>bed</span></b></div><hr>

Answer: bed
