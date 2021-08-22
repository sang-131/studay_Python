import xlwings as xw

#提取 表3 的当日销售，提取表4 当日其他出库
app = xw.App(visible=False, add_book=False)
# 警告提醒及屏幕更新关闭
app.display_alerts  = False
app.screen_updating = False
# 文件位置：filepath，打开test文档
filepath = r'D:\文档\python代码\openpyxl练习用.xlsx'
wb = app.books.open(filepath)
sht = wb.sheets.active
# sht.autofit() # 行列自适应宽度
info = sht.used_range
a1 = sht.range('a1:e1')
a1.api.Font.Bold = True   # 设置为粗体。
a1.api.HorizontalAlignment = -4108  # -4108 水平居中,-4131 靠左，-4152 靠右。
a1.api.VerticalAlignment = -4108
info.api.Font.Size = 10   # 设置字体的大小
"""如果是一个区域的单元格，内部边框设置如下"""
# # Borders(11) 内部垂直边线。
info.api.Borders(11).LineStyle = 1
info.api.Borders(11).Weight = 3
# # # # Borders(12) 内部水平边线。
info.api.Borders(12).LineStyle = 1
info.api.Borders(12).Weight = 3
# Borders(9) 底部边框，LineStyle = 1 直线。
info.api.Borders(9).LineStyle = 1
info.api.Borders(9).Weight = 3   # 设置边框粗细。
# Borders(7) 左边框，LineStyle = 2 虚线。
info.api.Borders(7).LineStyle = 1
info.api.Borders(7).Weight = 3
# Borders(8) 顶部框，LineStyle = 5 双点划线。
info.api.Borders(8).LineStyle = 1
info.api.Borders(8).Weight = 3
# Borders(10) 右边框，LineStyle = 4 点划线。
info.api.Borders(10).LineStyle = 1
info.api.Borders(10).Weight = 3
# 保存文档
wb.save()
# 退出工作簿（可省略）
wb.close()
# 退出Excel
app.quit()