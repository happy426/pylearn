from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

bar = (
    Bar(init_opts=opts.InitOpts(
        width="500px",
        height="500px",
        theme="white"
    ))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [5, 21, 30, 13, 55, 80])
    # 横向柱状图
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title='bar2',
            subtitle="副标题",
            title_textstyle_opts=opts.TextStyleOpts(**{"color": "#333", "font_size": 12})
        ),
        visualmap_opts=opts.VisualMapOpts(type_="color", range_text=['大', '小'])
    )
)
bar.render('result/bar2.html')
