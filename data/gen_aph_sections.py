# -*- coding: utf-8 -*-
"""生成 APH Q2 2026 sections JSON（使用 json.dumps 自动转义，确保 JSON 合法）"""
import json
import os

META = {
    "company_name": "Amphenol Corp",
    "quarter": "Q2 2026",
    "report_type": "季度财报深度分析",
    "report_date": "2026-08-14",
    "earnings_date": "2026-07-29",
    "data_source": "公司财报/Alpha Vantage/Finnhub",
    "currency_unit": "USD",
    "generated_at": "2026-08-14 北京时间",
    "report_version": "v4 (sections-reference)",
    "disclaimer_text": "本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。"
}

HEADER = (
    '<header class="report-head">'
    '<div class="wrap">'
    '<div class="kicker">季度财报深度分析 · 2026-08-14</div>'
    '<h1>Amphenol Corp Q2 2026 财报深度分析</h1>'
    '<p class="sub">AI数据中心需求驱动销售额同比增长55%至87.58亿美元创历史新高，有机增长30%，调整后每股收益1.35美元（+66.7%），Q3指引93-94亿美元再超预期并宣布2拆1拆分</p>'
    '<div class="meta">报告日期：2026-08-14　|　财报发布：2026-07-29　|　数据来源：公司财报/Alpha Vantage/Finnhub　|　本位币：USD</div>'
    '<div class="stat-grid">'
    '<div class="stat-card"><div class="v">87.58 亿</div><div class="l">营收</div><div class="d pos">+55.0% YoY</div></div>'
    '<div class="stat-card"><div class="v">17.69 亿</div><div class="l">净利润</div><div class="d pos">+62.1% YoY</div></div>'
    '<div class="stat-card"><div class="v">40.5%</div><div class="l">毛利率</div><div class="d pos">+4.2 pts YoY</div></div>'
    '<div class="stat-card"><div class="v">1.35 美元</div><div class="l">调整后EPS</div><div class="d pos">+66.7% YoY</div></div>'
    '</div>'
    '</div>'
    '</header>'
)

SEC01 = (
    '<section id="sec01">'
    '<div class="section-num">01 / 核心摘要</div>'
    '<h2>核心摘要</h2>'
    '<p class="lead">Amphenol（安费诺）2026年第二季度实现销售额87.58亿美元（同比+55.0%，有机增长+30%），净利润17.69亿美元（同比+62.1%），毛利率提升至40.5%，均创历史新高。IT数据通信市场有机增长异常强劲，AI数据中心高速互连需求成为核心增长引擎；公司同步宣布2拆1股票拆分，并上调2026年全年收购增厚预期至0.30美元/股。</p>'
    '<div class="highlights-box">'
    '<h3>本季关键亮点</h3>'
    '<ul>'
    '<li>销售额87.58亿美元，同比+55.0%，有机增长+30%，连续第9个季度创历史新高</li>'
    '<li>调整后摊薄每股收益1.35美元，同比+66.7%，大幅超出机构预期的1.18美元</li>'
    '<li>调整后营业利润率29.8%（含约8000万美元关税回收），盈利能力再创新高</li>'
    '<li>通信解决方案业务占销售额约61%，有机增长+42%，AI数据中心高速互连需求强劲</li>'
    '<li>订单比销售额高约19亿美元，账面与账单比率1.23，需求能见度极高</li>'
    '<li>Q3指引销售额93-94亿美元、调整后EPS 1.40-1.42美元（拆分前），双超预期</li>'
    '</ul>'
    '</div>'
    '<div class="callout pos">'
    '<div class="callout-title">核心结论</div>'
    '<p>本季业绩全面超预期，AI数据中心资本开支浪潮持续兑现为连接器与高速互连产品的强劲需求。通信解决方案业务61%的销售占比与42%的有机增速，印证公司在AI服务器、交换机、光模块等高速互连领域的全球领先地位。订单/出货比1.23显示订单簿饱满，Q3指引再超预期并宣布2拆1拆分，反映管理层对增长持续性的高度信心。</p>'
    '</div>'
    '</section>'
)

SEC02 = (
    '<section id="sec02">'
    '<div class="section-num">02 / 财务概览</div>'
    '<h2>财务概览</h2>'
    '<p>下表汇总Amphenol 2026年第二季度核心财务指标，并与上一季度（Q1 2026）及去年同期（Q2 2025）对比。所有数据均来自公司官方披露与 Alpha Vantage 数据库，单位为美元。</p>'
    '<div class="table-wrap">'
    '<table>'
    '<thead><tr><th>财务指标</th><th class="num">本季度<br>Q2 2026</th><th class="num">上季度<br>Q1 2026</th><th class="num">同比</th><th class="num">环比</th></tr></thead>'
    '<tbody>'
    '<tr><td>营业收入</td><td class="num">87.58 亿</td><td class="num">76.20 亿</td><td class="num pos">+55.0%</td><td class="num pos">+14.9%</td></tr>'
    '<tr><td>毛利润</td><td class="num">35.48 亿</td><td class="num">28.00 亿</td><td class="num pos">+72.8%</td><td class="num pos">+26.7%</td></tr>'
    '<tr><td>营业利润</td><td class="num">25.85 亿</td><td class="num">18.32 亿</td><td class="num pos">+80.6%</td><td class="num pos">+41.1%</td></tr>'
    '<tr><td>净利润</td><td class="num">17.69 亿</td><td class="num">9.43 亿</td><td class="num pos">+62.1%</td><td class="num pos">+87.6%</td></tr>'
    '<tr><td>经营现金流</td><td class="num">15.57 亿</td><td class="num">11.21 亿</td><td class="num pos">—</td><td class="num pos">+38.9%</td></tr>'
    '<tr><td>资本支出</td><td class="num">3.56 亿</td><td class="num">2.92 亿</td><td class="num">—</td><td class="num pos">+21.9%</td></tr>'
    '<tr><td>自由现金流</td><td class="num">12.02 亿</td><td class="num">8.30 亿</td><td class="num pos">—</td><td class="num pos">+44.8%</td></tr>'
    '</tbody>'
    '</table>'
    '</div>'
    '<div class="chart-figure">'
    '<div class="chart-title">营收与净利润趋势（近6个季度）</div>'
    '<div class="chart-desc">展示Amphenol从2025年Q1至2026年Q2的营收与净利润变化趋势，体现AI驱动下的加速增长</div>'
    '<div class="chart-container" id="chart-revenue-trend"></div>'
    '<div class="chart-foot">数据来源: Alpha Vantage + 公司财报披露 · 单位: USD（亿美元）</div>'
    '</div>'
    '</section>'
)

SEC03 = (
    '<section id="sec03">'
    '<div class="section-num">03 / 营收分析</div>'
    '<h2>营收分析</h2>'
    '<p>Amphenol 主要按两大事业部披露业绩：互连与传感器系统（含通信解决方案等）与严苛环境解决方案（含防务、汽车等）。2026年Q2通信解决方案业务占销售额约61%，有机增长+42%，是绝对增长引擎。</p>'
    '<h3>营收构成（按事业部）</h3>'
    '<div class="table-wrap">'
    '<table>'
    '<thead><tr><th>业务板块</th><th class="num">营收（亿美元）</th><th class="num">占比</th><th class="num">有机同比</th></tr></thead>'
    '<tbody>'
    '<tr><td>通信解决方案</td><td class="num">约 53.4</td><td class="num">61%</td><td class="num pos">+42%</td></tr>'
    '<tr><td>严苛环境解决方案</td><td class="num">约 34.2</td><td class="num">39%</td><td class="num pos">双位数增长</td></tr>'
    '<tr><td><strong>合计</strong></td><td class="num"><strong>87.58</strong></td><td class="num"><strong>100%</strong></td><td class="num pos"><strong>+30%（有机）</strong></td></tr>'
    '</tbody>'
    '</table>'
    '</div>'
    '<div class="chart-figure">'
    '<div class="chart-title">营收构成（按事业部）</div>'
    '<div class="chart-desc">通信解决方案占销售额约61%，严苛环境解决方案约39%</div>'
    '<div class="chart-container short" id="chart-revenue-mix"></div>'
    '<div class="chart-foot">数据来源: 公司Q2 2026财报披露</div>'
    '</div>'
    '<div class="callout">'
    '<div class="callout-title">营收驱动因素</div>'
    '<p>本季营收增长的核心驱动力是AI数据中心的爆发式需求：科技巨头持续加码AI基础设施资本开支，带动对高速连接器、线缆组件与互连系统的需求。OSFP系列、ExaMAX背板连接器、Mini Cool Edge等产品支持112G/224G PAM4信号，单端口聚合带宽可达1.6T，直接对接GPU集群、交换机与光模块。叠加2026年1月完成的105亿美元收购康普Connectivity and Cable Solutions业务（强化光纤与数据中心连接能力），共同推动销售额同比+55%、有机增长+30%。</p>'
    '</div>'
    '</section>'
)

SEC04 = (
    '<section id="sec04">'
    '<div class="section-num">04 / 盈利能力</div>'
    '<h2>盈利能力分析</h2>'
    '<p>本季盈利能力全面走强：毛利率40.5%（同比+4.2pts），营业利润率29.5%，净利率20.2%。调整后营业利润率达29.8%（含约8000万美元关税回收），创历史新高，体现AI产品组合优化与规模效应。</p>'
    '<div class="stat-grid">'
    '<div class="stat-card"><div class="l">毛利率</div><div class="v">40.5%</div><div class="d pos">+4.2 pts YoY</div></div>'
    '<div class="stat-card"><div class="l">营业利润率</div><div class="v">29.5%</div><div class="d pos">+4.2 pts YoY</div></div>'
    '<div class="stat-card"><div class="l">净利率</div><div class="v">20.2%</div><div class="d pos">+0.9 pts YoY</div></div>'
    '<div class="stat-card"><div class="l">调整后营业利润率</div><div class="v">29.8%</div><div class="d pos">历史新高</div></div>'
    '</div>'
    '<div class="chart-figure">'
    '<div class="chart-title">利润率趋势对比</div>'
    '<div class="chart-desc">毛利率、营业利润率、净利率近6个季度整体上行，2026年以来显著抬升</div>'
    '<div class="chart-container" id="chart-margin-trend"></div>'
    '<div class="chart-foot">数据来源: Alpha Vantage + 公司财报</div>'
    '</div>'
    '<h3>成本结构分析</h3>'
    '<div class="table-wrap">'
    '<table>'
    '<thead><tr><th>成本项</th><th class="num">金额（亿美元）</th><th class="num">占营收比</th><th class="num">同比变动</th></tr></thead>'
    '<tbody>'
    '<tr><td>营业成本（COGS）</td><td class="num">52.10</td><td class="num">59.5%</td><td class="num neg">占比下降</td></tr>'
    '<tr><td>销售与管理费用</td><td class="num">约 7.50</td><td class="num">约 8.6%</td><td class="num">占比下降</td></tr>'
    '<tr><td>研发费用</td><td class="num">约 2.30</td><td class="num">约 2.6%</td><td class="num">占比下降</td></tr>'
    '<tr><td>关税回收（一次性）</td><td class="num">-0.80</td><td class="num">—</td><td class="num pos">正向贡献</td></tr>'
    '</tbody>'
    '</table>'
    '</div>'
    '<div class="callout pos">'
    '<div class="callout-title">盈利能力点评</div>'
    '<p>毛利率从2025年Q1的34.2%持续提升至40.5%，主要得益于AI高速互连产品的高附加值、产品组合优化与规模效应释放。调整后营业利润率29.8%创历史新高，其中约8000万美元关税回收提供一次性正向贡献。随着AI产品占比提升与康普收购业务整合，公司盈利能力有望维持高位。</p>'
    '</div>'
    '</section>'
)

SEC05 = (
    '<section id="sec05">'
    '<div class="section-num">05 / 资产负债与现金流</div>'
    '<h2>资产负债与现金流</h2>'
    '<p>截至2026年6月30日，Amphenol总资产448.07亿美元，现金及等价物47.29亿美元，资产负债率65.1%。本季经营现金流15.57亿美元，自由现金流12.02亿美元，现金生成能力强劲。</p>'
    '<h3>资产负债表概要</h3>'
    '<div class="table-wrap">'
    '<table>'
    '<thead><tr><th>项目</th><th class="num">期末（Q2 2026）</th><th class="num">期初（Q1 2026）</th><th class="num">变动</th></tr></thead>'
    '<tbody>'
    '<tr><td>现金及等价物</td><td class="num">47.29 亿</td><td class="num">41.28 亿</td><td class="num pos">+6.01 亿</td></tr>'
    '<tr><td>总资产</td><td class="num">448.07 亿</td><td class="num">421.34 亿</td><td class="num pos">+26.73 亿</td></tr>'
    '<tr><td>总负债</td><td class="num">291.85 亿</td><td class="num">280.42 亿</td><td class="num">+11.43 亿</td></tr>'
    '<tr><td>股东权益</td><td class="num">154.92 亿</td><td class="num">139.77 亿</td><td class="num pos">+15.15 亿</td></tr>'
    '<tr><td>资产负债率</td><td class="num">65.1%</td><td class="num">66.6%</td><td class="num pos">-1.5 pts</td></tr>'
    '</tbody>'
    '</table>'
    '</div>'
    '<h3>现金流分析</h3>'
    '<div class="chart-figure">'
    '<div class="chart-title">现金流结构（近4个季度）</div>'
    '<div class="chart-desc">经营现金流持续强劲，资本支出保持稳健水平</div>'
    '<div class="chart-container" id="chart-cashflow"></div>'
    '<div class="chart-foot">数据来源: Alpha Vantage + 公司财报 · 单位: USD（亿美元）</div>'
    '</div>'
    '<div class="insight-grid">'
    '<div class="insight-card"><div class="icon green">OCF</div><h4>经营现金流</h4><p>本季经营现金流15.57亿美元，环比+38.9%，体现AI业务高增长带来的强劲现金转化能力</p></div>'
    '<div class="insight-card"><div class="icon orange">CapEx</div><h4>资本支出</h4><p>资本支出3.56亿美元，占营收约4.1%，轻重资产平衡的制造模式维持适度扩张</p></div>'
    '<div class="insight-card"><div class="icon blue">FCF</div><h4>自由现金流</h4><p>自由现金流12.02亿美元，环比+44.8%，现金流利润率约13.7%，为股东回报与收购提供充足弹药</p></div>'
    '</div>'
    '</section>'
)

SEC06 = (
    '<section id="sec06">'
    '<div class="section-num">06 / 运营指标</div>'
    '<h2>关键运营指标</h2>'
    '<p>Amphenol 的核心运营指标围绕订单、业务板块增速与终端市场景气度展开。本季订单比销售额高约19亿美元，账面与账单比率达1.23，需求能见度极高。</p>'
    '<div class="stat-grid">'
    '<div class="stat-card"><div class="l">账面与账单比率</div><div class="v">1.23</div><div class="d pos">订单强劲</div></div>'
    '<div class="stat-card"><div class="l">订单超销售额</div><div class="v">约 19 亿</div><div class="d pos">需求领先</div></div>'
    '<div class="stat-card"><div class="l">通信解决方案占比</div><div class="v">61%</div><div class="d pos">有机+42%</div></div>'
    '<div class="stat-card"><div class="l">IT数据通信有机增速</div><div class="v">异常强劲</div><div class="d pos">AI驱动</div></div>'
    '</div>'
    '<div class="chart-figure">'
    '<div class="chart-title">关键运营指标趋势</div>'
    '<div class="chart-desc">订单/出货、防务、通信解决方案等核心指标持续向好</div>'
    '<div class="chart-container tall" id="chart-kpi-trend"></div>'
    '<div class="chart-foot">数据来源: 公司财报披露</div>'
    '</div>'
    '<p>本季运营指标的最大亮点是订单持续大于出货：账面与账单比率1.23，订单比销售额高约19亿美元，说明下游AI算力建设节奏持续推进，需求基础扎实。管理层同时将2026年康普通信连接业务对每股收益的增厚预期从0.15美元上调至0.30美元，显示收购整合进展超预期。</p>'
    '</section>'
)

SEC07 = (
    '<section id="sec07">'
    '<div class="section-num">07 / 分部与地区业绩</div>'
    '<h2>分部与地区业绩</h2>'
    '<p>Amphenol 是全球多元化的互连产品供应商，营收在地理上分布于美国、中国、其他亚太地区与欧洲。基于公司历史披露结构，本季按地区估算分布如下（具体拆分以公司10-Q为准）。</p>'
    '<h3>地区营收分布（估算）</h3>'
    '<div class="chart-figure">'
    '<div class="chart-title">各地区营收占比（估算）</div>'
    '<div class="chart-desc">基于公司历史地区结构的估算分布</div>'
    '<div class="chart-container short" id="chart-geo"></div>'
    '<div class="chart-foot">数据来源: 公司历史披露估算</div>'
    '</div>'
    '<div class="table-wrap">'
    '<table>'
    '<thead><tr><th>地区</th><th class="num">营收（亿美元·估算）</th><th class="num">占比</th><th class="num">同比</th><th>趋势</th></tr></thead>'
    '<tbody>'
    '<tr><td>美国</td><td class="num">约 35.0</td><td class="num">约 40%</td><td class="num pos">高增长</td><td>AI数据中心核心</td></tr>'
    '<tr><td>中国</td><td class="num">约 19.3</td><td class="num">约 22%</td><td class="num pos">稳健增长</td><td>通信与工业需求</td></tr>'
    '<tr><td>其他亚太</td><td class="num">约 21.0</td><td class="num">约 24%</td><td class="num pos">增长</td><td>制造与消费电子</td></tr>'
    '<tr><td>欧洲/其他</td><td class="num">约 12.3</td><td class="num">约 14%</td><td class="num pos">增长</td><td>汽车与工业</td></tr>'
    '</tbody>'
    '</table>'
    '</div>'
    '<div class="insight-grid">'
    '<div class="insight-card"><div class="icon green">+</div><h4>增长亮点地区</h4><p>美国市场受益于AI数据中心资本开支浪潮，是IT数据通信高速互连需求的核心来源，有机增长异常强劲</p></div>'
    '<div class="insight-card"><div class="icon red">!</div><h4>承压地区</h4><p>欧洲与部分消费电子相关地区需求相对温和，但整体仍保持正增长，公司全球多元化布局有效平滑地区波动</p></div>'
    '</div>'
    '</section>'
)

SEC08 = (
    '<section id="sec08">'
    '<div class="section-num">08 / 业绩指引与展望</div>'
    '<h2>业绩指引与展望</h2>'
    '<p>Amphenol对2026年第三季度给出强劲指引：销售额93-94亿美元、调整后摊薄EPS 1.40-1.42美元（拆分前），双双超出华尔街预期，显示AI需求持续性与管理层信心。</p>'
    '<h3>下季度指引（Q3 2026，拆分前口径）</h3>'
    '<div class="table-wrap">'
    '<table>'
    '<thead><tr><th>指标</th><th class="num">指引区间</th><th class="num">市场预期</th><th>对比</th></tr></thead>'
    '<tbody>'
    '<tr><td>销售额</td><td class="num">93-94 亿美元</td><td class="num">约 89 亿美元</td><td>超预期</td></tr>'
    '<tr><td>调整后EPS</td><td class="num">1.40-1.42 美元</td><td class="num">约 1.30 美元</td><td>超预期</td></tr>'
    '<tr><td>毛利率</td><td class="num">指引未单独披露</td><td class="num">—</td><td>维持高位</td></tr>'
    '<tr><td>资本支出</td><td class="num">维持稳健水平</td><td class="num">—</td><td>—</td></tr>'
    '</tbody>'
    '</table>'
    '</div>'
    '<h3>关键事件与拆分安排</h3>'
    '<div class="timeline">'
    '<div class="timeline-item"><div class="tl-date">2026-07-29</div><h4>Q2 2026财报发布</h4><p>销售额87.58亿美元（+55%），调整后EPS 1.35美元（+67%），双双超预期；Q3指引93-94亿美元、EPS 1.40-1.42美元</p></div>'
    '<div class="timeline-item"><div class="tl-date">2026-08-17</div><h4>2拆1拆分记录日</h4><p>股票拆分记录日为8月17日，额外股份于9月2日发放，拆分后参考价约84.59美元，市值不变</p></div>'
    '<div class="timeline-item"><div class="tl-date">2026-10-14</div><h4>Q3股息发放</h4><p>三季度股息0.25美元/股（拆分后对应0.125美元/股），10月14日发放</p></div>'
    '</div>'
    '<div class="callout pos">'
    '<div class="callout-title">指引点评</div>'
    '<p>Q3指引销售额93-94亿美元，对应环比约+6.5%、同比约+51%，延续高速增长态势。调整后EPS指引1.40-1.42美元（拆分前）亦超预期，且管理层将2026年收购增厚预期从0.15美元上调至0.30美元。2拆1拆分降低单股价格，提升股票流动性与可交易性，不改变公司基本面价值。</p>'
    '</div>'
    '</section>'
)

SEC09 = (
    '<section id="sec09">'
    '<div class="section-num">09 / 管理层评论</div>'
    '<h2>管理层评论</h2>'
    '<p>管理层将本季强劲表现归因于AI数据中心需求的爆发与公司收购计划的协同贡献，并对2026年后续展望保持高度乐观。</p>'
    '<div class="callout">'
    '<div class="callout-title">R. Adam Norwitt · 首席执行官</div>'
    '<p>"我们很高兴再次以创纪录的销售额和调整后摊薄每股收益交出业绩答卷，两者均显著超出我们指引的上限。IT数据通信市场尤其是有机增长异常强劲，主要得益于AI相关基础设施需求的持续释放。电子产品领域的革命仍在加速，我们通过自身创新与成功的收购计划，正为各多元化终端市场创造令人兴奋的增长机会。"</p>'
    '</div>'
    '<div class="callout">'
    '<div class="callout-title">管理层 · 业绩说明会要点</div>'
    '<p>"通信解决方案业务占销售额约61%，有机增长+42%，是增长核心引擎；防务业务受益于全球军费上升保持双位数增长。Q3指引93-94亿美元反映订单能见度极高，账面与账单比率1.23。我们宣布2拆1股票拆分以增强流动性，并上调2026年收购增厚预期至0.30美元/股。"</p>'
    '</div>'
    '<h3>电话会议要点</h3>'
    '<div class="highlights-box">'
    '<ul>'
    '<li>AI数据中心高速互连（OSFP、ExaMAX、Mini Cool Edge等）是增长最强劲的终端市场</li>'
    '<li>订单比销售额高约19亿美元，账面与账单比率1.23，需求能见度极高</li>'
    '<li>2026年1月完成的105亿美元康普Connectivity and Cable Solutions收购整合进展超预期</li>'
    '<li>公司把2026年收购对EPS增厚预期从0.15美元上调至0.30美元</li>'
    '<li>宣布2拆1股票拆分，记录日8月17日，额外股份9月2日发放</li>'
    '<li>全球军费上升推动防务业务双位数增长，多元化布局平滑地区波动</li>'
    '</ul>'
    '</div>'
    '</section>'
)

SEC10 = (
    '<section id="sec10">'
    '<div class="section-num">10 / 风险因素</div>'
    '<h2>风险因素</h2>'
    '<p>尽管本季业绩强劲，Amphenol仍面临若干需持续关注的风险，包括AI需求周期性、高估值、收购整合、供应链与地缘政治等。</p>'
    '<ul class="risk-list">'
    '<li><span class="risk-badge high">高</span><div class="risk-body"><h4>AI资本开支周期性风险</h4><p>当前增长高度依赖科技巨头AI数据中心资本开支，若AI基础设施投资放缓或超大规模客户采购节奏调整，高速互连需求可能显著回落，订单/出货比率（当前1.23）面临均值回归压力</p></div></li>'
    '<li><span class="risk-badge high">高</span><div class="risk-body"><h4>高估值与估值回调风险</h4><p>当前市盈率约42倍，明显高于TE Connectivity等可比公司（倍数约一半），对需求波动与利率变化的容忍度较低，若增速放缓股价可能承压</p></div></li>'
    '<li><span class="risk-badge med">中</span><div class="risk-body"><h4>收购整合与商誉风险</h4><p>连续大额收购（含105亿美元康普业务）带来整合执行、协同效应兑现与商誉减值风险，收购增厚预期上调但实际兑现仍需验证</p></div></li>'
    '<li><span class="risk-badge med">中</span><div class="risk-body"><h4>供应链与地缘政治风险</h4><p>全球制造布局面临关税政策变化、贸易摩擦与供应链扰动风险，本季关税回收约8000万美元为一次性因素，未来关税影响存在不确定性</p></div></li>'
    '<li><span class="risk-badge low">低</span><div class="risk-body"><h4>技术迭代与竞争风险</h4><p>高速互连技术持续迭代（112G/224G/448G），需保持研发投入领先；泰科电子等竞争者同样受益于AI趋势，竞争格局需持续跟踪</p></div></li>'
    '</ul>'
    '<div class="callout warn">'
    '<div class="callout-title">风险提示</div>'
    '<p>整体基本面强劲，但高估值意味着对需求波动的容忍度较低。AI数据中心资本开支能否持续是核心变量：若订单继续跑在出货前面，说明需求基础扎实；一旦比率回落，高估值将迅速成为市场关注焦点。建议重点跟踪账面与账单比率、AI客户资本开支指引与收购整合进展。</p>'
    '</div>'
    '</section>'
)

SEC11 = (
    '<section id="sec11">'
    '<div class="section-num">11 / 投资观点</div>'
    '<h2>投资观点</h2>'
    '<p class="lead">Amphenol本季业绩全面超预期，Q3指引再超预期并宣布2拆1拆分，财报日股价上涨约4.5%，随后连续走高累计涨幅近19%。华尔街多数分析师维持买入评级，平均目标价约200.78美元。</p>'
    '<div class="stat-grid">'
    '<div class="stat-card"><div class="l">当前股价（拆分前）</div><div class="v">169.18 $</div><div class="d pos">财报后大涨</div></div>'
    '<div class="stat-card"><div class="l">分析师平均目标价</div><div class="v">200.78 $</div><div class="d pos">+18.7% 空间</div></div>'
    '<div class="stat-card"><div class="l">市盈率(PE)</div><div class="v">约 42x</div><div class="d warn">高于同业</div></div>'
    '<div class="stat-card"><div class="l">市值</div><div class="v">约 2044 亿 $</div><div class="d pos">行业龙头</div></div>'
    '</div>'
    '<div class="insight-grid">'
    '<div class="insight-card"><div class="icon green">+</div><h4>看多因素</h4><p>AI数据中心高速互连需求爆发，销售额+55%、有机+30%；调整后EPS 1.35美元（+67%）超预期；订单/出货1.23需求能见度极高；Q3指引93-94亿美元双超预期；2拆1拆分提升流动性；分析师评级以买入为主（5强买/15买/3持）</p></div>'
    '<div class="insight-card"><div class="icon red">-</div><h4>看空因素</h4><p>市盈率约42倍显著高于TE Connectivity等可比公司；AI资本开支若放缓高估值承压；大额收购带来整合与商誉风险；高增长基数下未来同比增速或自然回落</p></div>'
    '<div class="insight-card"><div class="icon blue">i</div><h4>催化剂</h4><p>Q3 2026指引兑现（93-94亿美元）；AI超大规模客户资本开支上修；448G高速铜缆等新一代产品放量；康普收购协同效应进一步释放；9月2日拆分完成后流动性改善</p></div>'
    '</div>'
    '<div class="callout pos">'
    '<div class="callout-title">投资结论</div>'
    '<p>Amphenol本季财报全面超预期，验证其在AI数据中心高速互连领域的全球龙头地位。订单/出货比率1.23与Q3超预期指引提供短期基本面支撑，2拆1拆分增强流动性。但42倍市盈率已price-in大量增长预期，投资者需平衡AI需求持续性与高估值之间的权衡。短期看，Q3指引与AI资本开支趋势是核心观察点；中长期看，448G等新技术迭代、收购整合与多元化终端市场布局提供持续增长动力。建议关注增速持续性，警惕AI投资周期回落带来的估值修正风险。</p>'
    '</div>'
    '</section>'
)

SEC12 = (
    '<section id="sec12">'
    '<div class="section-num">12 / 附录</div>'
    '<h2>附录</h2>'
    '<h3>术语表</h3>'
    '<dl class="glossary">'
    '<dt>有机增长（Organic Growth）</dt><dd>剔除收购与汇率影响后的内生业务增长，本季+30%，反映核心业务真实增长动能</dd>'
    '<dt>账面与账单比率（Book-to-Bill Ratio）</dt><dd>订单金额与出货金额之比，大于1表示订单增长快于出货，本季1.23反映需求强劲</dd>'
    '<dt>调整后摊薄每股收益（Adjusted Diluted EPS）</dt><dd>剔除一次性项目（如关税回收、收购摊销）后的每股收益，本季1.35美元（+67%）</dd>'
    '<dt>OSFP / ExaMAX</dt><dd>安费诺面向AI服务器与超大规模数据中心的高速连接器产品系列，支持112G/224G PAM4信号，单端口带宽可达1.6T</dd>'
    '<dt>2拆1股票拆分（2-for-1 Stock Split）</dt><dd>每1股拆为2股，每股价格减半、股数翻倍，总市值不变，用于降低单股价格提升流动性，记录日8月17日</dd>'
    '<dt>关税回收</dt><dd>本季约8000万美元的一次性关税回收收益，对调整后营业利润率提供一次性正向贡献</dd>'
    '</dl>'
    '<h3>近6个季度财务数据</h3>'
    '<div class="chart-figure">'
    '<div class="chart-title">综合财务指标雷达图</div>'
    '<div class="chart-desc">从营收规模、盈利能力、增长、现金流等多维度综合展示Amphenol财务表现</div>'
    '<div class="chart-container" id="chart-radar"></div>'
    '<div class="chart-foot">数据来源: Alpha Vantage + 公司财报</div>'
    '</div>'
    '<hr class="divider">'
    '<h3>数据说明</h3>'
    '<p>本报告财务数据来源于Alpha Vantage API（历史季度数据）、Finnhub API（公司profile与分析师评级）以及公司2026年Q2财报官方披露与格隆汇、富途、头条财经等专业媒体公开报道。Q2 2026季度数据以公司官方披露为准（销售额87.58亿美元、调整后EPS 1.35美元），历史季度数据以Alpha Vantage API为准。地区数据为公司历史结构估算。所有金额单位为美元（USD），百分比变化基于同比口径（与2025年Q2对比）除非特别说明。股票拆分前口径：拆分后参考价约84.59美元，EPS相应减半。</p>'
    '</section>'
)

FOOTER = (
    '<footer>'
    '<div class="wrap">'
    '<div class="footer-top">'
    '<h3>参考资料</h3>'
    '<ol class="sources">'
    '<li id="cite-1"><a href="https://investors.amphenol.com/">Amphenol 投资者关系官网 · 新闻与财报披露</a></li>'
    '<li id="cite-2"><a href="http://m.toutiao.com/group/7671861547722965550/">头条财经 · 安费诺2拆1拆分，19亿订单缓冲藏着AI连接器真功夫 · 2026-08</a></li>'
    '<li id="cite-3"><a href="https://t.10jqka.com.cn/m/guba/APH/169">同花顺圈子 · 安费诺Q2业绩超预期+AI驱动+指引上调 · 2026-07</a></li>'
    '<li id="cite-4"><a href="https://www.futunn.com/stock/APH-US/earnings">富途牛牛 · 安费诺(APH)财报与业绩预测</a></li>'
    '<li id="cite-5"><a href="http://m.toutiao.com/group/7634206932542194211/">头条财经 · AI数据中心需求强劲，安费诺业绩展望超预期 · 2026-04</a></li>'
    '<li id="cite-6"><a href="http://m.toutiao.com/group/7652438878149673524/">经济观察网 · 安费诺2026年一季度防务业务销售额同比增44% · 2026-05</a></li>'
    '<li id="cite-7"><a href="https://news.eeworld.com.cn/emp/Amphenol_ICC/a404959.jspx">电子工程世界 · 安费诺季度业绩分析</a></li>'
    '</ol>'
    '</div>'
    '<div class="disclaimer">'
    '<p>本报告基于Amphenol Corp（APH）2026年第二季度财报公开数据自动生成，仅供学习交流，不构成任何投资建议。</p>'
    '<p>本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。报告中涉及的所有财务数据均来源于公开披露文件，分析师观点基于截至 2026-08-14 可获得的信息。</p>'
    '</div>'
    '<div class="footer-meta">'
    '<span>报告生成: 2026-08-14 北京时间</span>'
    '<span>报告版本: v4 (sections-reference)</span>'
    '</div>'
    '</div>'
    '</footer>'
)

data = {
    "meta": META,
    "header": HEADER,
    "sections": {
        "sec01": SEC01,
        "sec02": SEC02,
        "sec03": SEC03,
        "sec04": SEC04,
        "sec05": SEC05,
        "sec06": SEC06,
        "sec07": SEC07,
        "sec08": SEC08,
        "sec09": SEC09,
        "sec10": SEC10,
        "sec11": SEC11,
        "sec12": SEC12,
    },
    "footer": FOOTER,
}

out_path = r"D:\temp\Output\stock-financial-reports\data\aph-q2-2026-sections.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 验证能解析回来
with open(out_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print("JSON 合法，已写入:", out_path)
print("sections 数量:", len(loaded["sections"]))
print("header 长度:", len(loaded["header"]))
print("footer 长度:", len(loaded["footer"]))
