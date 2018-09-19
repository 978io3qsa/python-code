#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlsxwriter

def charts():
    workbook = xlsxwriter.Workbook('chart_column.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold':1})

    headings = ['Number','Batch 1','Batch 2','Batch 3']

    data = [
       ['aabbb-\ndasfdadf', 'fdajdad-\ngddfddfefafdsgf', 'dadafd-\neefeffdsafd', 'jfeiofij-fjdjfd', 'jdojf-ddjfdad', 'dfjaod-dafd'],
       [10,40,50,20,10,50],
       [30,60,70,50,40,30],
       [1,2,3,4,5,6]
    ]

    format = workbook.add_format()
    format.set_text_wrap()
    worksheet.set_column('A:A',10,format)

    worksheet.write_column('A1',headings,bold)

    worksheet.write_column('A2',data[0])
    worksheet.write_column('B2',data[1])
    worksheet.write_column('C2', data[2])
    worksheet.write_column('D2', data[3])

    chart1 = workbook.add_chart({'type' : 'column'})
    line_chart = workbook.add_chart({'type':'line'})

    chart1.add_series({
        'name' : '=Sheet1!$B$1',
        'categories' : '=Sheet1!$A$2:$A$7',
        'values' : 'Sheet1!$B$2:$B$7',
        'data_labels' : {'values' : True},
    })

    chart1.add_series({
        'name': "=Sheet1!$C$1",
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$C$2:$C$7',
        'data_labels': {'value': True},
        'gap':150,
        'overlap': -50,
    })
    line_chart.add_series({
        'name': "=Sheet1!$D$1",
        'categories': '=Sheet1$A2:$A$7',
        'values': '=Sheet1!$D2$2:$D$7',
        'data_label':{'value': True},
    })
    # 添加图表标题和标签
    chart1.set_title({'name': 'Results of sample analysis'})
    chart1.set_x_axis({'name': 'Test number'})

    chart1.set_style(11)
    chart1.set_size({'width': 720, 'height': 376})
    chart1.set_legend({'position': 'top'})
    chart1.set_y_axis({
        'major_gridlines': {
            'visible': False,
            'line': {'none': True}
        },
        'line': {'none': True},
        'num_font': {'color': '#FFFFFF'},

    })
    # 在D2单元格插入图表（带偏移）
    chart1.combine(line_chart)
    worksheet.insert_chart('D3', chart1, {'x_offset': 50, 'y_offset': 10})
    workbook.close()


if __name__ == '__main__':
    charts()




