"""
编写一个 BMI 计算器程序，要求如下：
1. 用户输入：通过 input() 函数获取用户的身高（单位：米）和体重（单位：千克）。
2. 计算 BMI：使用公式 BMI = 体重(kg) / 身高(m)² 计算 BMI 值。
3. 判断分类：根据 BMI 值判断身体状况（参考中国成人标准）：
  ○ BMI < 18.5：偏瘦
  ○ 18.5 ≤ BMI < 24：正常
  ○ 24 ≤ BMI < 28：超重
  ○ BMI ≥ 28：肥胖
4. 输出结果：使用 f-string 格式化输出用户的 BMI 值和分类结果。
5. 健康建议：根据分类结果给出相应的健康建议，例如：
  ○ 偏瘦：建议适当增加营养摄入，进行适量运动
  ○ 正常：保持良好的生活习惯
  ○ 超重/肥胖：建议控制饮食，增加运动量
"""

height = float(input("请输入您的身高（米）："))
weight = float(input("请输入您的体重（千克）："))
health = "超重"
proposal = "建议控制饮食，增加运动量"
if height > 0 and weight > 0:
    BMI = weight / height**2
    print(f"您的BMI值为{BMI}")
    if BMI < 18.5:
        health = "偏瘦"
        proposal = "建议适当增加营养摄入，进行适量运动"
    elif 18.5 <= BMI < 24:
        health = "正常"
        proposal = "保持良好的生活习惯"
    elif 24 <= BMI < 28:
        health = "超重"
    elif health > 28:
        health = "肥胖"
    print(f"身体状况：{health}")
    print(f"建议：{proposal}！")
