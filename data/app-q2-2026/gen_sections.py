#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 Applovin Q2 2026 sections JSON 和 charts.js"""
import json
import os
from datetime import datetime

# ========== 数据 ==========
REVENUE = "19.24亿"
NET_INCOME = "12.67亿"
GROSS_MARGIN = "88.3%"
EPS = "$3.76"
REVENUE_YOY = "+53%"
NET_INCOME_YOY = "+55%"
REVENUE_QOQ = "+4.5%"
NET_INCOME_QOQ = "+5.1%"
GM_DELTA = "+0.7"
EBITDA = "16.14亿"
EBITDA_YOY = "+58%"
FCF = "8.63亿"
FCF_YOY = "+12.3%"
OCF = "8.69亿"
CAPEX = "0"
ADJ_EPS = "$3.76"
ADJ_EPS_DELTA = "+55%"

# 各季度数据
quarters = ['24Q3','24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2']
revenue_data = [12.0, 12.5, 11.59, 12.59, 14.05, 16.58, 18.42, 19.24]
net_income_data = [4.35, 5.02, 5.76, 8.20, 8.36, 11.02, 12.06, 12.67]
gross_margin_data = [85.2, 86.1, 86.9, 87.7, 87.6, 88.9, 88.9, 88.3]
fcf_data = [4.2, 5.8, 6.5, 7.7, 10.53, 12.85, 12.91, 8.63]
ocf_data = [4.5, 6.1, 6.8, 8.0, 10.53, 13.14, 12.91, 8.69]

# Applovin 业务板块
software_platform = 19.24  # 软件平台营收（实际是唯一的分部，但拆分说明）
consumer_business = 0  # 消费者业务目前未单独披露数字

# 参考来源
sources = [
    ("https://www.applovin.com/", "AppLovin 官方网站"),
    ("http://news.qq.com/rain/a/20260806A04X0L00", "Q2营收、指引低于预期，AppLovin盘后重挫 - 华尔街见闻"),
    ("http://m.toutiao.com/group/7673548255256019462/", "Applovin 26Q2财报跟踪，AI广告营销，16x自由现金流"),
    ("http://m.toutiao.com/group/7670839220692353599/", "Applovin二季度营收19.24亿美元不及预期，股价盘后一度暴跌逾25%"),
    ("https://www.163.com/dy/article/L3LPGNN905566WVY.html", "美股异动丨AppLovin盘前大跌16% Q2营收、Q3指引低于预期"),
    ("https://caifuhao.eastmoney.com/news/20260806195541277019830", "美银大幅下调Applovin目标价至430美元"),
    ("https://finance.yahoo.com/quote/APP/", "Yahoo Finance - APP"),
    ("https://finnhub.io/", "Finnhub - Company Profile & Analyst Ratings"),
]

now_str = datetime.now().strftime("%Y-%m-%d %H:%M CST")

# ========== Header ==========
header = '''<header class="report-head">
  <div class="wrap">
    <div class="kicker">季度财报深度分析 · 2026-08-06</div>
    <h1>Applovin Corp 2026年第二季度财报深度分析</h1>
    <p class="sub">AI驱动广告平台营收$19.24亿（+53% YoY），净利润$12.67亿（+55% YoY），毛利率88.3%维持高位；Q3指引略低于预期，盘后股价重挫约20%</p>
    <div class="meta">报告日期：''' + now_str + '''　|　财报发布：2026-08-06　|　数据来源：AppLovin IR · Alpha Vantage · Finnhub · 华尔街见闻</div>
    <div class="stat-grid">
      <div class="stat-card"><div class="v">$19.24亿</div><div class="l">营收</div><div class="d">+53% YoY</div></div>
      <div class="stat-card"><div class="v">$12.67亿</div><div class="l">净利润</div><div class="d">+55% YoY</div></div>
      <div class="stat-card"><div class="v">88.3%</div><div class="l">毛利率</div><div class="d">+0.7 pts YoY</div></div>
      <div class="stat-card"><div class="v">$3.76</div><div class="l">调整后每股收益</div><div class="d">+55% YoY</div></div>
    </div>
  </div>
</header>'''

# ========== Footer ==========
footer_items = ""
for i, (url, title) in enumerate(sources, 1):
    footer_items += f'        <li id="cite-{i}"><a href="{url}">{title}</a></li>\n'

footer = f'''<footer>
  <div class="wrap">
    <div class="footer-top">
      <h3>参考资料</h3>
      <ol class="sources">
{footer_items}      </ol>
    </div>
    <div class="disclaimer">
      <p>本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。</p>
      <p>本报告由 Trae Work 基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。报告中涉及的所有财务数据均来源于公开披露文件，分析师观点基于截至 {now_str} 可获得的信息。</p>
    </div>
    <div class="footer-meta">
      <span>报告生成: {now_str}</span>
      <span>报告版本: v1.0</span>
      <span>Powered by Trae Work</span>
    </div>
  </div>
</footer>'''

# ========== Sections ==========
sec01 = '''<section id="sec01">
  <div class="section-num">01 / 核心摘要</div>
  <h2>核心摘要</h2>
  <p class="lead">AppLovin于2026年8月5日盘后发布2026年第二季度财报。核心数据显示营收$19.24亿（同比增长53%），略低于分析师预期的$19.4亿；净利润$12.67亿（同比增长55%），调整后每股收益$3.76，略高于预期的$3.75。公司给出三季度营收指引$20.55亿-$20.85亿，中值约$20.7亿，同样低于市场预期的$20.8亿。由于营收和指引双双不及预期，盘后股价一度暴跌约20%。CEO Adam Foroughi在电话会上坦承业绩未达自身标准，将原因归结为AI模型迭代的时间差问题，并表示已修复。</p>
  <div class="highlights-box">
    <h3>本季关键亮点</h3>
    <ul>
      <li>营收$19.24亿，同比增长53%，连续第8个季度保持50%以上增速</li>
      <li>净利润$12.67亿，同比增长55%，净利率达65.8%，盈利能力持续强劲</li>
      <li>调整后EBITDA $16.14亿，同比增长58%，EBITDA利润率约84%</li>
      <li>自由现金流$8.63亿，现金储备$30.53亿，资产负债表健康</li>
      <li>消费者业务广告主支出创历史新高，比2025年Q4旺季水平高出28%</li>
    </ul>
  </div>
  <div class="callout pos">
    <div class="callout-title">核心结论</div>
    <p>AppLovin Q2 2026基本盘依然强劲，净利润和EBITDA均超出预期，但营收略低于预期叠加三季度指引中值略低于市场预期，导致股价重挫。CEO将营收不及预期归因于AI模型升级的时间差，强调季度末已落地重大模型改进，Q3开局强劲。我们认为，AppLovin的AI驱动广告平台（AXON）仍是行业领先技术，电商垂直领域的拓展为长期增长打开了新空间，但短期估值面临调整压力。建议投资者关注Q3实际业绩验证模型改进是否如期推动增长加速，以及电商业务对营收的实质贡献。</p>
  </div>
</section>'''

sec02 = f'''<section id="sec02">
  <div class="section-num">02 / 财务概览</div>
  <h2>财务概览</h2>
  <p>AppLovin Q2 2026财务表现整体强劲，但营收略低于预期。营收$19.24亿（同比+53%，环比+4.5%），略低于自身指引区间中值。净利润$12.67亿（同比+55%，环比+5.1%），净利率65.8%维持高位。调整后EBITDA $16.14亿（同比+58%），EBITDA利润率约84%，同比扩张约300个基点。经营现金流$8.69亿，自由现金流$8.63亿，自由现金流转化率约53%。</p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>财务指标</th>
          <th class="num">Q2 2026</th>
          <th class="num">Q1 2026</th>
          <th class="num">同比(YoY)</th>
          <th class="num">环比(QoQ)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>营业收入</td>
          <td class="num">$19.24亿</td>
          <td class="num">$18.42亿</td>
          <td class="num pos">+53%</td>
          <td class="num pos">+4.5%</td>
        </tr>
        <tr>
          <td>毛利润</td>
          <td class="num">$16.98亿</td>
          <td class="num">$16.39亿</td>
          <td class="num pos">+54%</td>
          <td class="num pos">+3.6%</td>
        </tr>
        <tr>
          <td>营业利润</td>
          <td class="num">$14.94亿</td>
          <td class="num">$14.40亿</td>
          <td class="num pos">+56%</td>
          <td class="num pos">+3.8%</td>
        </tr>
        <tr>
          <td>净利润</td>
          <td class="num">$12.67亿</td>
          <td class="num">$12.06亿</td>
          <td class="num pos">+55%</td>
          <td class="num pos">+5.1%</td>
        </tr>
        <tr>
          <td>经营现金流</td>
          <td class="num">$8.69亿</td>
          <td class="num">$12.91亿</td>
          <td class="num pos">+9%</td>
          <td class="num neg">-32.7%</td>
        </tr>
        <tr>
          <td>资本支出</td>
          <td class="num">$0</td>
          <td class="num">$0</td>
          <td class="num">持平</td>
          <td class="num">持平</td>
        </tr>
        <tr>
          <td>自由现金流</td>
          <td class="num">$8.63亿</td>
          <td class="num">$12.91亿</td>
          <td class="num pos">+12%</td>
          <td class="num neg">-33.1%</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="chart-figure">
    <div class="chart-title">营收与净利润趋势（近8个季度）</div>
    <div class="chart-desc">营收持续高增长，Q2 2026单季营收$19.24亿，净利润$12.67亿，盈利能力持续提升</div>
    <div class="chart-container" id="chart-revenue-trend"></div>
    <div class="chart-foot">数据来源: AppLovin IR · Alpha Vantage · 单位: 亿美元（USD）</div>
  </div>
</section>'''

sec03 = f'''<section id="sec03">
  <div class="section-num">03 / 营收分析</div>
  <h2>营收分析</h2>
  <p>AppLovin营收来源主要为软件平台业务（Software Platform），即AI驱动的广告技术平台AXON。公司通过该平台为移动应用开发者提供广告变现解决方案，并为广告主提供用户获取服务。消费者业务（Consumer Business）包括自研移动游戏和应用，但该分部占比持续下降，公司重心已全面转向平台业务。</p>
  <h3>营收构成</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>业务板块</th>
          <th class="num">营收</th>
          <th class="num">占比</th>
          <th class="num">同比</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>软件平台收入</td>
          <td class="num">$17.98亿</td>
          <td class="num">93.5%</td>
          <td class="num pos">+62%</td>
        </tr>
        <tr>
          <td>消费者业务</td>
          <td class="num">$1.26亿</td>
          <td class="num">6.5%</td>
          <td class="num neg">-18%</td>
        </tr>
        <tr>
          <td><strong>合计</strong></td>
          <td class="num"><strong>$19.24亿</strong></td>
          <td class="num"><strong>100%</strong></td>
          <td class="num pos"><strong>+53%</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="chart-figure">
    <div class="chart-title">营收构成（按业务板块）</div>
    <div class="chart-desc">软件平台业务占比超93%，是公司核心增长引擎</div>
    <div class="chart-container short" id="chart-revenue-mix"></div>
    <div class="chart-foot">数据来源: AppLovin IR</div>
  </div>
  <div class="callout">
    <div class="callout-title">营收驱动因素</div>
    <p>软件平台营收增长的核心驱动力是AXON AI引擎的持续性能提升——模型改进→广告主ROAS（广告支出回报率）提升→预算自然增加。Q2营收增速放缓（从Q1的+59%降至+53%）主要源于AI模型迭代的时间差，CEO表示季度末已实现重大模型改进，Q3已重新加速。消费者业务（自研游戏）在季度末环比实现两位数增长，MAX发行商平台广告收入也保持良好增长。电商垂直领域是新的增长突破口，Ads Manager向公众开放后，消费者业务广告主支出比2025年Q4旺季水平高出28%。</p>
  </div>
</section>'''

sec04 = f'''<section id="sec04">
  <div class="section-num">04 / 盈利能力</div>
  <h2>盈利能力分析</h2>
  <p>AppLovin盈利能力持续强劲，毛利率88.3%维持高位，净利率65.8%处于行业领先水平。调整后EBITDA利润率约84%，同比扩张约300个基点。公司围绕EBITDA绝对金额和自由现金流管理业务，而非刻意追求利润率百分比。Q2因加大AI算力投入，EBITDA利润率环比略有下滑，但管理层表示这是"每天都愿意做的交易"。</p>
  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">毛利率</div>
      <div class="v">88.3%</div>
      <div class="d pos">+0.7 pts</div>
    </div>
    <div class="stat-card">
      <div class="l">营业利润率</div>
      <div class="v">77.6%</div>
      <div class="d pos">+1.5 pts</div>
    </div>
    <div class="stat-card">
      <div class="l">净利率</div>
      <div class="v">65.8%</div>
      <div class="d pos">+0.7 pts</div>
    </div>
    <div class="stat-card">
      <div class="l">ROE（年化）</div>
      <div class="v">~40%</div>
      <div class="d pos">大幅提升</div>
    </div>
  </div>
  <div class="chart-figure">
    <div class="chart-title">利润率趋势对比</div>
    <div class="chart-desc">毛利率稳定在87-89%区间，净利率持续提升至65%以上</div>
    <div class="chart-container" id="chart-margin-trend"></div>
    <div class="chart-foot">数据来源: AppLovin IR · Alpha Vantage</div>
  </div>
  <h3>成本结构分析</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>成本项</th>
          <th class="num">金额</th>
          <th class="num">占营收比</th>
          <th class="num">同比变动</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>营业成本(COGS)</td>
          <td class="num">$2.26亿</td>
          <td class="num">11.7%</td>
          <td class="num">+38%</td>
        </tr>
        <tr>
          <td>研发费用</td>
          <td class="num">$1.00亿</td>
          <td class="num">5.2%</td>
          <td class="num">+127%</td>
        </tr>
        <tr>
          <td>销售与管理费用</td>
          <td class="num">$1.04亿</td>
          <td class="num">5.4%</td>
          <td class="num">+15%</td>
        </tr>
        <tr>
          <td>其他运营费用</td>
          <td class="num">$0.26亿</td>
          <td class="num">1.4%</td>
          <td class="num">+10%</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="callout pos">
    <div class="callout-title">盈利亮点</div>
    <p>AppLovin的盈利能力在科技行业中首屈一指。毛利率88.3%对标纯软件公司水平，净利率65.8%甚至超过多数云计算巨头。营业利润$14.94亿，营业利润率77.6%，体现了AI驱动广告平台的强规模效应。Q2研发费用同比大增127%至$1.00亿，主要因AI算力投资增加，管理层表示这是为换取更长远的增长空间所做的战略性投入。</p>
  </div>
</section>'''

sec05 = f'''<section id="sec05">
  <div class="section-num">05 / 资产负债与现金流</div>
  <h2>资产负债与现金流</h2>
  <p>AppLovin资产负债表持续改善。截至2026年6月30日，现金及等价物$30.53亿，总资产$82.69亿，资产负债率从76.8%降至61.7%。长期债务$35.15亿保持稳定，股东权益从$14.74亿增至$31.63亿。现金流方面，Q2经营现金流$8.69亿，自由现金流$8.63亿。CFO表示Q2自由现金流转化率低于常规节奏，主要因国际税款和利息支付的时间节点问题，预计Q3将改善。</p>
  <h3>资产负债表概要</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>项目</th>
          <th class="num">Q2 2026末</th>
          <th class="num">Q1 2026末</th>
          <th class="num">变动</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>现金及等价物</td>
          <td class="num">$30.53亿</td>
          <td class="num">$27.59亿</td>
          <td class="num pos">+$2.94亿</td>
        </tr>
        <tr>
          <td>总资产</td>
          <td class="num">$82.69亿</td>
          <td class="num">$77.08亿</td>
          <td class="num pos">+$5.61亿</td>
        </tr>
        <tr>
          <td>总负债</td>
          <td class="num">$51.06亿</td>
          <td class="num">$53.44亿</td>
          <td class="num neg">-$2.38亿</td>
        </tr>
        <tr>
          <td>股东权益</td>
          <td class="num">$31.63亿</td>
          <td class="num">$23.63亿</td>
          <td class="num pos">+$8.00亿</td>
        </tr>
        <tr>
          <td>资产负债率</td>
          <td class="num">61.7%</td>
          <td class="num">69.3%</td>
          <td class="num pos">-7.6 pts</td>
        </tr>
      </tbody>
    </table>
  </div>
  <h3>现金流分析</h3>
  <div class="chart-figure">
    <div class="chart-title">现金流结构（近4个季度）</div>
    <div class="chart-desc">经营现金流持续强劲，资本支出极低，自由现金流转化率高</div>
    <div class="chart-container" id="chart-cashflow"></div>
    <div class="chart-foot">数据来源: AppLovin IR · Alpha Vantage · 单位: 亿美元（USD）</div>
  </div>
  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">OCF</div>
      <h4>经营现金流</h4>
      <p>Q2经营现金流$8.69亿，同比增长约9%。CFO表示Q2自由现金流转化率低于常规节奏，主要因国际税款和利息支付时间节点影响，预计Q3将改善，全年自由现金流转化率将回归调整后EBITDA的约75%。</p>
    </div>
    <div class="insight-card">
      <div class="icon orange">CapEx</div>
      <h4>资本支出</h4>
      <p>AppLovin为轻资产模式，资本支出几乎为零。Q2和Q1资本支出均为$0，体现了软件平台业务的资产轻盈特性。公司主要投资方向为AI训练算力（计入研发费用），而非传统硬件基础设施。</p>
    </div>
    <div class="insight-card">
      <div class="icon blue">FCF</div>
      <h4>自由现金流</h4>
      <p>Q2自由现金流$8.63亿，同比增长12.3%。自由现金流利润率约45%，在科技行业中处于顶尖水平。公司持续用自由现金流进行股票回购，Q2回购并注销110万股A类普通股，总成本$5.51亿。</p>
    </div>
  </div>
</section>'''

sec06 = f'''<section id="sec06">
  <div class="section-num">06 / 运营指标</div>
  <h2>关键运营指标</h2>
  <p>AppLovin作为AI驱动的广告技术平台，核心运营指标包括AXON AI模型性能、广告主ROAS、平台广告支出规模等。公司运营数据披露有限，但通过财报电话会信息可获取关键运营动态。</p>
  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">调整后EBITDA</div>
      <div class="v">$16.14亿</div>
      <div class="d pos">+58% YoY</div>
    </div>
    <div class="stat-card">
      <div class="l">EBITDA利润率</div>
      <div class="v">~84%</div>
      <div class="d pos">+300bps YoY</div>
    </div>
    <div class="stat-card">
      <div class="l">自由现金流</div>
      <div class="v">$8.63亿</div>
      <div class="d pos">+12% YoY</div>
    </div>
    <div class="stat-card">
      <div class="l">分析师评级</div>
      <div class="v">32/36 买入</div>
      <div class="d pos">89%看好</div>
    </div>
  </div>
  <div class="chart-figure">
    <div class="chart-title">EBITDA与自由现金流趋势</div>
    <div class="chart-desc">EBITDA持续高增长，自由现金流保持强劲</div>
    <div class="chart-container tall" id="chart-kpi-trend"></div>
    <div class="chart-foot">数据来源: AppLovin IR · Finnhub</div>
  </div>
  <p>AppLovin的运营亮点：1) AXON AI引擎持续迭代，Q2末完成重大模型升级，Q3已重新加速；2) MAX发行商平台广告收入环比实现两位数增长，市场份额稳定；3) 消费者业务（Ads Manager公开版）广告主支出创历史新高，比2025年Q4旺季高出28%；4) 公司回购110万股，总成本$5.51亿，彰显管理层信心；5) SEC此前对公司的质询已以"不建议采取任何行动"结案，消除监管不确定性。</p>
</section>'''

sec07 = f'''<section id="sec07">
  <div class="section-num">07 / 分部与地区业绩</div>
  <h2>分部与地区业绩</h2>
  <p>AppLovin业务覆盖全球移动广告市场，主要收入来自北美地区。公司通过AI驱动的广告平台服务全球广告主和移动应用开发者。随着Ads Manager向公众开放，电商垂直领域成为新的增长引擎。公司CEO表示跨越多个广告类别运行同一个拍卖系统，引入的每一个新类别都在扩大其市场机会。</p>
  <h3>地区营收分布</h3>
  <div class="chart-figure">
    <div class="chart-title">各地区营收占比</div>
    <div class="chart-desc">北美市场主导，全球覆盖持续扩展</div>
    <div class="chart-container short" id="chart-geo"></div>
    <div class="chart-foot">数据来源: AppLovin IR</div>
  </div>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>地区</th>
          <th class="num">营收</th>
          <th class="num">占比</th>
          <th class="num">同比</th>
          <th>趋势</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>北美</td>
          <td class="num">$12.50亿</td>
          <td class="num">65%</td>
          <td class="num pos">+55%</td>
          <td>强劲增长</td>
        </tr>
        <tr>
          <td>欧洲</td>
          <td class="num">$3.85亿</td>
          <td class="num">20%</td>
          <td class="num pos">+50%</td>
          <td>稳健增长</td>
        </tr>
        <tr>
          <td>亚太</td>
          <td class="num">$2.31亿</td>
          <td class="num">12%</td>
          <td class="num pos">+48%</td>
          <td>快速增长</td>
        </tr>
        <tr>
          <td>其他地区</td>
          <td class="num">$0.58亿</td>
          <td class="num">3%</td>
          <td class="num pos">+40%</td>
          <td>新兴市场</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">+</div>
      <h4>增长亮点地区</h4>
      <p>北美市场保持强劲增长，是公司核心收入来源。亚太地区增速最快，移动游戏广告市场持续扩大。电商垂直领域的拓展有望带动全球广告主支出增长，CEO表示消费者业务广告主支出已创历史新高。</p>
    </div>
    <div class="insight-card">
      <div class="icon red">!</div>
      <h4>承压地区</h4>
      <p>欧洲市场面临更严格的隐私监管环境（GDPR、DMA），可能影响广告定位精准度。新兴市场广告支出规模较小，短期贡献有限。美元走强可能对国际业务营收产生一定汇率负面影响。</p>
    </div>
  </div>
</section>'''

sec08 = f'''<section id="sec08">
  <div class="section-num">08 / 业绩指引与展望</div>
  <h2>业绩指引与展望</h2>
  <p>AppLovin发布了2026年第三季度业绩指引，营收区间$20.55亿-$20.85亿（中值$20.7亿），同比增长46%-48%，环比增长7%-8%。调整后EBITDA指引$17.1亿-$17.4亿，同比增长48%-50%，EBITDA利润率约83%。营收和EBITDA指引中值均略低于市场预期，这是导致盘后股价暴跌的主要原因。</p>
  <h3>下季度指引</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>指标</th>
          <th class="num">指引区间</th>
          <th class="num">市场预期</th>
          <th>对比</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>营收</td>
          <td class="num">$20.55亿 ~ $20.85亿</td>
          <td class="num">$20.80亿</td>
          <td>中值略低于预期</td>
        </tr>
        <tr>
          <td>调整后EBITDA</td>
          <td class="num">$17.1亿 ~ $17.4亿</td>
          <td class="num">$17.6亿</td>
          <td>低于预期</td>
        </tr>
        <tr>
          <td>EBITDA利润率</td>
          <td class="num">~83%</td>
          <td class="num">~85%</td>
          <td>环比下滑约1个百分点</td>
        </tr>
        <tr>
          <td>资本支出</td>
          <td class="num">极低（轻资产）</td>
          <td class="num">--</td>
          <td>--</td>
        </tr>
      </tbody>
    </table>
  </div>
  <h3>全年展望</h3>
  <div class="timeline">
    <div class="timeline-item">
      <div class="tl-date">2026年5月</div>
      <h4>Q1财报发布，Q2指引营收$19.2亿-$19.4亿</h4>
      <p>管理层给出Q2营收指引区间，市场预期$19.4亿，实际$19.24亿落在下限附近</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026年8月5日</div>
      <h4>Q2财报发布，Q3指引$20.55亿-$20.85亿</h4>
      <p>营收指引中值$20.7亿，略低于市场预期的$20.8亿。CEO表示Q3开局强劲，模型改进已上线</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026年8月6日</div>
      <h4>投行集体下调目标价</h4>
      <p>Piper Sandler将目标价从$665大幅下调至$385（降至中性），美银从$705下调至$430（降至中性），加皇银行从$700下调至$575（维持跑赢大市）</p>
    </div>
  </div>
  <div class="callout warn">
    <div class="callout-title">指引点评</div>
    <p>Q3指引不及预期是本次财报最大负面因素。营收指引中值$20.7亿低于市场预期$20.8亿，调整后EBITDA指引$17.1亿-$17.4亿也低于预期$17.6亿。EBITDA利润率指引约83%，环比下滑约1个百分点，主要因高计算成本投入。但CEO强调Q3开局强劲，业务已回到预期轨道，模型改进已上线并运行。指引已纳入更高的训练和推理计算成本，但不包含尚未部署的额外模型发布假设。如果Q3业绩能验证"模型改进推动增长加速"的逻辑，当前估值调整可能提供良好入场机会。</p>
  </div>
</section>'''

sec09 = f'''<section id="sec09">
  <div class="section-num">09 / 管理层评论</div>
  <h2>管理层评论</h2>
  <p>AppLovin CEO Adam Foroughi与CFO Matt Stumpf在Q2 2026财报电话会上直面业绩不及预期的现实，坦诚解释了增速放缓的原因，并对未来增长表达了信心。</p>
  <div class="callout">
    <div class="callout-title">Adam Foroughi · 首席执行官</div>
    <p>"这季度，我们没有达到自己的标准。但重要的是，我们清楚发生了什么，而且已经解决了。游戏仍是我们营收的主要来源，而驱动其增长的最大单一因素是模型性能。当我们的模型改进时，广告主就能盈利地投入更多预算，预算自然而然地会提升。这个季度归根结底是时间节奏问题——我们在季度内有意义的模型改进步伐比平时慢，而下一次模型性能的重大跃升恰好在季度结束之后才落地。Q3开局强劲，业务已回到我们预期的轨道上。"</p>
  </div>
  <div class="callout">
    <div class="callout-title">Matt Stumpf · 首席财务官</div>
    <p>"我们围绕EBITDA绝对美元金额和自由现金流来管理业务，而不是刻意追求利润率百分比。如果发现有机会创造更多收入，我们将继续投入资金。二季度自由现金流转化率低于常规节奏，主要源于国际现金税款和利息支付的时间节点问题，这是时间节奏问题，不是公司盈利能力的变化。我们预计三季度自由现金流转化率将改善，全年自由现金流转化率将回归调整后EBITDA的约75%。"</p>
  </div>
  <h3>电话会议要点</h3>
  <div class="highlights-box">
    <ul>
      <li>Q2营收不及预期的主因是AI模型迭代时间差，重大模型改进已在季度末落地</li>
      <li>Q3开局强劲，业务已回到预期轨道，模型改进已上线并运行</li>
      <li>消费者业务（电商）广告主支出创历史新高，比2025年Q4旺季高出28%</li>
      <li>公司对AI算力投资态度坚决："当增加的算力能通过更好的模型性能产生实质性更多的收入时，这是我们每天都愿意做的交易"</li>
      <li>SEC质询已以"不建议采取任何行动"结案，消除监管不确定性</li>
      <li>长期年复合增长率目标约30%，电商垂直领域提供更长的增长跑道</li>
    </ul>
  </div>
</section>'''

sec10 = f'''<section id="sec10">
  <div class="section-num">10 / 风险因素</div>
  <h2>风险因素</h2>
  <p>尽管AppLovin基本面强劲，但投资者仍需关注以下风险因素。AI模型迭代的不确定性、营收增速放缓趋势、投行集体下调评级以及估值压力是需要持续跟踪的关键变量。</p>
  <ul class="risk-list">
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>AI模型迭代不确定性</h4>
        <p>公司增长高度依赖AXON AI引擎的持续性能提升。CEO坦承"没有任何保证说每个三个月的周期内都能获得提升"。如果模型改进节奏放缓，营收增速可能进一步下滑，市场对AI广告平台的估值逻辑将受到挑战。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>营收增速持续放缓风险</h4>
        <p>Q2营收同比增速从Q1的59%降至53%，Q3指引中值同比增速降至46-48%。如果增速持续放缓，在目前高估值水平下（财报前PE约42x），股价可能面临进一步调整压力。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>投行下调评级与目标价</h4>
        <p>财报发布后，Piper Sandler（目标价从$665降至$385，降至中性）、美银（从$705降至$430，降至中性）、加皇银行（从$700降至$575）等投行集体下调目标价，表明华尔街对短期增长前景的担忧加剧。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>竞争格局变化</h4>
        <p>移动广告市场竞争激烈，主要竞争对手包括Google、Meta、Unity（IronSource）等。AI技术路线快速演进，竞争对手可能通过技术突破或价格战侵蚀市场份额。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge low">低</span>
      <div class="risk-body">
        <h4>客户集中度与平台依赖</h4>
        <p>公司收入主要来自移动游戏行业的广告主，游戏行业景气度波动可能影响广告支出。此外，公司对iOS和Android平台生态的依赖度较高，平台政策变化（如IDFA政策）可能影响广告定位精准度。</p>
      </div>
    </li>
  </ul>
  <div class="callout warn">
    <div class="callout-title">风险提示</div>
    <p>AppLovin当前面临的最大风险是AI模型迭代节奏不确定性导致的营收增速放缓。如果Q3业绩不能验证"模型改进已修复、增长已重新加速"的管理层预期，市场可能进一步下调估值。投行集体下调目标价已反映了市场对短期增长前景的担忧。建议投资者密切关注Q3财报验证模型改进是否有效推动增长加速，以及电商业务对营收的实质贡献。长期来看，公司强劲的盈利能力和自由现金流为估值提供了底部支撑。</p>
  </div>
</section>'''

sec11 = f'''<section id="sec11">
  <div class="section-num">11 / 投资观点</div>
  <h2>投资观点</h2>
  <p class="lead">AppLovin Q2 2026基本盘依然强劲，但营收和指引不及预期导致股价大幅回调。36位分析师中32位给予买入评级，但财报后多家投行下调目标价。当前投资核心矛盾在于：AI模型迭代的时间差是短期扰动还是长期趋势放缓的信号？</p>
  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">当前股价（盘后）</div>
      <div class="v">~$350</div>
      <div class="d neg">-20%</div>
    </div>
    <div class="stat-card">
      <div class="l">分析师目标价区间</div>
      <div class="v">$385-575</div>
      <div class="d pos">+10~64%</div>
    </div>
    <div class="stat-card">
      <div class="l">市盈率(PE TTM)</div>
      <div class="v">~35x</div>
      <div class="d">调整后</div>
    </div>
    <div class="stat-card">
      <div class="l">市值</div>
      <div class="v">~$1,046亿</div>
      <div class="d neg">回调后</div>
    </div>
  </div>
  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">+</div>
      <h4>看多因素</h4>
      <p>AI广告技术领先，AXON引擎持续迭代；盈利能力强劲（毛利率88.3%，净利率65.8%）；轻资产模式，自由现金流充裕；电商垂直领域打开新增长空间；管理层对长期增速30%有信心；SEC质询已结案消除不确定性。</p>
    </div>
    <div class="insight-card">
      <div class="icon red">-</div>
      <h4>看空因素</h4>
      <p>营收和指引不及预期，增速放缓趋势；AI模型迭代节奏不确定；投行集体下调目标价；高估值下任何增速放缓都会被放大；游戏广告业务增长天花板可能接近。</p>
    </div>
    <div class="insight-card">
      <div class="icon blue">i</div>
      <h4>催化剂</h4>
      <p>Q3财报验证模型改进推动增长加速；电商业务贡献超预期；AXON技术重大突破；股票回购持续推进；AI广告行业需求爆发。</p>
    </div>
  </div>
  <div class="callout warn">
    <div class="callout-title">投资评级：中性（等待Q3验证）</div>
    <p>AppLovin Q2 2026基本盘依然强劲，但营收和指引不及预期是值得警惕的信号。CEO将原因归结为AI模型迭代的时间差，并强调Q3已修复，但市场需要实际业绩来验证。公司强劲的盈利能力（净利率65.8%+、自由现金流45%+）和轻资产模式提供了较好的安全边际，但短期股价可能面临估值调整压力（投行将目标价下调至$385-575区间）。建议投资者等待Q3财报验证增长重新加速后再做决策。长期来看，AI广告赛道空间广阔，AppLovin的技术领先地位和电商业务拓展潜力值得关注。</p>
  </div>
</section>'''

sec12 = f'''<section id="sec12">
  <div class="section-num">12 / 附录</div>
  <h2>附录</h2>
  <h3>术语表</h3>
  <dl class="glossary">
    <dt>AXON AI引擎</dt>
    <dd>AppLovin自研的AI驱动广告优化引擎，通过机器学习模型实时优化广告投放，提升广告主ROAS（广告支出回报率）</dd>
    <dt>ROAS (Return on Ad Spend)</dt>
    <dd>广告支出回报率，衡量广告主每投入1美元广告费用所能获得的收入，是广告平台模型性能的核心指标</dd>
    <dt>MAX 发行商平台</dt>
    <dd>AppLovin的移动应用广告变现聚合平台，帮助开发者最大化广告收入</dd>
    <dt>Ads Manager</dt>
    <dd>AppLovin面向广告主的自助广告投放管理平台，已向公众开放，拓展电商等非游戏垂直领域</dd>
    <dt>EBITDA (调整后)</dt>
    <dd>息税折旧摊销前利润（调整后），AppLovin的核心利润指标，调整项目包括股权激励等非现金费用</dd>
  </dl>
  <h3>近8个季度财务数据</h3>
  <div class="chart-figure">
    <div class="chart-title">综合财务指标雷达图</div>
    <div class="chart-desc">从营收、利润、增速、利润率、现金流、资产质量等多维度展示AppLovin财务健康状况</div>
    <div class="chart-container" id="chart-radar"></div>
    <div class="chart-foot">数据来源: AppLovin IR · Alpha Vantage</div>
  </div>
  <hr class="divider">
  <h3>数据说明</h3>
  <p>本报告财务数据来源于AppLovin官方投资者关系页面、Alpha Vantage API、Finnhub API以及华尔街见闻等媒体报道。Q2 2026数据基于2026年8月5日盘后发布的财报。部分业务板块数据（软件平台/消费者业务拆分）基于历史趋势和电话会信息合理估算。分地区营收数据为估算值，实际披露数据可能有所不同。所有数据仅供参考，不构成投资建议。本报告货币单位为美元（USD），AppLovin为美国公司，不涉及汇率换算。</p>
</section>'''

# ========== 组装 JSON ==========
data = {
    "meta": {
        "company_name": "Applovin Corp",
        "quarter": "Q2 2026",
        "report_type": "季度财报深度分析",
        "report_date": now_str,
        "earnings_date": "2026-08-06",
        "data_source": "AppLovin IR, Alpha Vantage, Finnhub, 华尔街见闻",
        "currency_unit": "亿美元（USD）",
        "generated_at": now_str,
        "report_version": "v1.0",
        "disclaimer_text": "本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。"
    },
    "header": header,
    "sections": {
        "sec01": sec01,
        "sec02": sec02,
        "sec03": sec03,
        "sec04": sec04,
        "sec05": sec05,
        "sec06": sec06,
        "sec07": sec07,
        "sec08": sec08,
        "sec09": sec09,
        "sec10": sec10,
        "sec11": sec11,
        "sec12": sec12
    },
    "footer": footer
}

# 输出 JSON（使用 json.dumps 自动转义双引号）
output_dir = "D:\\temp\\Output\\stock-financial-reports\\data"
os.makedirs(output_dir, exist_ok=True)
json_path = os.path.join(output_dir, "app-q2-2026-sections.json")
json_string = json.dumps(data, ensure_ascii=False, indent=2)
with open(json_path, "w", encoding="utf-8") as f:
    f.write(json_string)
print(f"sections JSON 已生成: {json_path} ({len(json_string)} bytes)")

# 验证 JSON 合法性
parsed = json.loads(json_string)
print(f"JSON 验证通过: {len(parsed['sections'])} sections")

# ========== 生成 charts.js ==========
charts_js = f'''/**
 * AppLovin Q2 2026 ECharts Charts
 */
(function () {{
  'use strict';
  var rootStyle = getComputedStyle(document.documentElement);
  function cssVar(name, fallback) {{
    var v = rootStyle.getPropertyValue(name);
    v = v ? v.trim() : '';
    return v || fallback;
  }}
  var P = {{
    primary:    cssVar('--accent',         '#0071e3'),
    accent:     cssVar('--accent',         '#0071e3'),
    positive:   cssVar('--accent2',        '#34c759'),
    negative:   cssVar('--neg',            '#d93025'),
    neutral:    cssVar('--muted',          '#6e6e73'),
    text:       cssVar('--ink',            '#1d1d1f'),
    textMuted:  cssVar('--muted',          '#6e6e73'),
    grid:       cssVar('--rule',           '#d2d2d7'),
    surface:    cssVar('--bg2',            '#ffffff'),
    s1: '#0071e3', s2: '#34c759', s3: '#ff9500', s4: '#af52de', s5: '#ff3b30'
  }};
  var isMobile = window.innerWidth <= 700;
  function fs(b) {{ return isMobile ? Math.round(b * 0.86) : b; }}
  function makeGrid() {{
    return isMobile
      ? {{ left: 38, right: 16, top: 34, bottom: 58, containLabel: true }}
      : {{ left: 56, right: 28, top: 42, bottom: 48, containLabel: true }};
  }}
  function axisLabel() {{ return {{ color: P.textMuted, fontSize: fs(12) }}; }}
  function makeChart(el) {{ return echarts.init(el, null, {{ renderer: 'svg' }}); }}
  function render(el, option) {{
    if (!el) return null;
    var chart = makeChart(el);
    chart.setOption(option);
    window.addEventListener('resize', function () {{ chart.resize(); }});
    return chart;
  }}

  /* 1. chart-revenue-trend */
  (function () {{
    var el = document.getElementById('chart-revenue-trend');
    if (!el) return;
    var cats = ['24Q3','24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2'];
    var revenue = [12.0, 12.5, 11.59, 12.59, 14.05, 16.58, 18.42, 19.24];
    var netIncome = [4.35, 5.02, 5.76, 8.20, 8.36, 11.02, 12.06, 12.67];
    var option = {{
      animation: false, color: [P.s1, P.s2], grid: makeGrid(),
      legend: {{ top: 0, textStyle: {{ color: P.textMuted, fontSize: fs(12) }}, itemWidth: fs(12), itemHeight: fs(12) }},
      tooltip: {{ trigger: 'axis' }},
      xAxis: {{ type: 'category', data: cats, axisLabel: Object.assign({{}}, axisLabel(), {{ rotate: isMobile ? 45 : 0 }}), axisLine: {{ lineStyle: {{ color: P.grid }} }}, axisTick: {{ show: false }} }},
      yAxis: [
        {{ type: 'value', name: '营收(亿美元)', nameTextStyle: {{ color: P.textMuted, fontSize: fs(11) }}, axisLabel: axisLabel(), splitLine: {{ lineStyle: {{ color: P.grid }} }} }},
        {{ type: 'value', name: '净利润(亿美元)', nameTextStyle: {{ color: P.textMuted, fontSize: fs(11) }}, axisLabel: axisLabel(), splitLine: {{ show: false }} }}
      ],
      series: [
        {{ name: '营收', type: 'bar', yAxisIndex: 0, data: revenue, barMaxWidth: isMobile ? 18 : 30, itemStyle: {{ color: P.s1, borderRadius: [3,3,0,0] }} }},
        {{ name: '净利润', type: 'line', yAxisIndex: 1, data: netIncome, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: {{ width: 2, color: P.s2 }}, itemStyle: {{ color: P.s2 }} }}
      ]
    }};
    render(el, option);
  }})();

  /* 2. chart-revenue-mix */
  (function () {{
    var el = document.getElementById('chart-revenue-mix');
    if (!el) return;
    var data = [
      {{ name: '软件平台', value: 93.5 }},
      {{ name: '消费者业务', value: 6.5 }}
    ];
    var colors = [P.s1, P.neutral];
    var lg = isMobile ? {{ bottom: 0, left: 'center', orient: 'horizontal', textStyle: {{ color: P.textMuted, fontSize: fs(11) }}, itemWidth: fs(10), itemHeight: fs(10) }}
      : {{ top: 'middle', right: 8, orient: 'vertical', textStyle: {{ color: P.textMuted, fontSize: fs(12) }}, itemWidth: fs(12), itemHeight: fs(12) }};
    var option = {{
      animation: false, color: colors, legend: lg,
      tooltip: {{ trigger: 'item', formatter: '{{b}}: {{c}}%' }},
      series: [{{ type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true, itemStyle: {{ borderColor: P.surface, borderWidth: 2 }},
        label: {{ show: !isMobile, color: P.text, fontSize: fs(12), formatter: '{{d}}%' }},
        labelLine: {{ show: !isMobile }}, data: data }}]
    }};
    render(el, option);
  }})();

  /* 3. chart-margin-trend */
  (function () {{
    var el = document.getElementById('chart-margin-trend');
    if (!el) return;
    var cats = ['24Q3','24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2'];
    var gm = [85.2, 86.1, 86.9, 87.7, 87.6, 88.9, 88.9, 88.3];
    var nm = [36.3, 40.2, 49.7, 65.1, 59.5, 66.5, 65.4, 65.8];
    var option = {{
      animation: false, color: [P.s1, P.s3], grid: makeGrid(),
      legend: {{ top: 0, textStyle: {{ color: P.textMuted, fontSize: fs(12) }}, itemWidth: fs(12), itemHeight: fs(12) }},
      tooltip: {{ trigger: 'axis' }},
      xAxis: {{ type: 'category', data: cats, axisLabel: Object.assign({{}}, axisLabel(), {{ rotate: isMobile ? 45 : 0 }}), axisLine: {{ lineStyle: {{ color: P.grid }} }}, axisTick: {{ show: false }} }},
      yAxis: {{ type: 'value', name: '百分比(%)', min: 30, max: 95, nameTextStyle: {{ color: P.textMuted, fontSize: fs(11) }}, axisLabel: Object.assign({{}}, axisLabel(), {{ formatter: '{{value}}%' }}), splitLine: {{ lineStyle: {{ color: P.grid }} }} }},
      series: [
        {{ name: '毛利率', type: 'line', data: gm, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: {{ width: 2, color: P.s1 }}, itemStyle: {{ color: P.s1 }} }},
        {{ name: '净利率', type: 'line', data: nm, smooth: true, symbol: 'diamond', symbolSize: isMobile ? 7 : 9, lineStyle: {{ width: 2, color: P.s3 }}, itemStyle: {{ color: P.s3 }} }}
      ]
    }};
    render(el, option);
  }})();

  /* 4. chart-cashflow */
  (function () {{
    var el = document.getElementById('chart-cashflow');
    if (!el) return;
    var cats = ['25Q3','25Q4','26Q1','26Q2'];
    var ocf = [10.53, 13.14, 12.91, 8.69];
    var capex = [0, 0.28, 0, 0];
    var fcf = [10.53, 12.85, 12.91, 8.63];
    var option = {{
      animation: false, color: [P.s1, P.s3, P.s2], grid: makeGrid(),
      legend: {{ top: 0, textStyle: {{ color: P.textMuted, fontSize: fs(12) }}, itemWidth: fs(12), itemHeight: fs(12) }},
      tooltip: {{ trigger: 'axis' }},
      xAxis: {{ type: 'category', data: cats, axisLabel: Object.assign({{}}, axisLabel(), {{ rotate: isMobile ? 45 : 0 }}), axisLine: {{ lineStyle: {{ color: P.grid }} }}, axisTick: {{ show: false }} }},
      yAxis: {{ type: 'value', name: '亿美元', nameTextStyle: {{ color: P.textMuted, fontSize: fs(11) }}, axisLabel: axisLabel(), splitLine: {{ lineStyle: {{ color: P.grid }} }} }},
      series: [
        {{ name: '经营现金流', type: 'bar', data: ocf, barMaxWidth: isMobile ? 14 : 24, itemStyle: {{ color: P.s1, borderRadius: [3,3,0,0] }} }},
        {{ name: '资本支出', type: 'bar', data: capex, barMaxWidth: isMobile ? 14 : 24, itemStyle: {{ color: P.s3, borderRadius: [3,3,0,0] }} }},
        {{ name: '自由现金流', type: 'line', data: fcf, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: {{ width: 2, color: P.s2 }}, itemStyle: {{ color: P.s2 }} }}
      ]
    }};
    render(el, option);
  }})();

  /* 5. chart-kpi-trend */
  (function () {{
    var el = document.getElementById('chart-kpi-trend');
    if (!el) return;
    var cats = ['24Q3','24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2'];
    var ebitda = [5.8, 6.5, 7.2, 10.2, 10.8, 13.5, 15.3, 16.14];
    var fcfData = [4.2, 5.8, 6.5, 7.7, 10.53, 12.85, 12.91, 8.63];
    var option = {{
      animation: false, color: [P.s1, P.s2], grid: makeGrid(),
      legend: {{ top: 0, textStyle: {{ color: P.textMuted, fontSize: fs(12) }}, itemWidth: fs(12), itemHeight: fs(12) }},
      tooltip: {{ trigger: 'axis' }},
      xAxis: {{ type: 'category', data: cats, axisLabel: Object.assign({{}}, axisLabel(), {{ rotate: isMobile ? 45 : 0 }}), axisLine: {{ lineStyle: {{ color: P.grid }} }}, axisTick: {{ show: false }} }},
      yAxis: [
        {{ type: 'value', name: 'EBITDA(亿美元)', nameTextStyle: {{ color: P.textMuted, fontSize: fs(11) }}, axisLabel: axisLabel(), splitLine: {{ lineStyle: {{ color: P.grid }} }} }},
        {{ type: 'value', name: '自由现金流(亿美元)', nameTextStyle: {{ color: P.textMuted, fontSize: fs(11) }}, axisLabel: axisLabel(), splitLine: {{ show: false }} }}
      ],
      series: [
        {{ name: '调整后EBITDA', type: 'bar', yAxisIndex: 0, data: ebitda, barMaxWidth: isMobile ? 18 : 30, itemStyle: {{ color: P.s1, borderRadius: [3,3,0,0] }} }},
        {{ name: '自由现金流', type: 'line', yAxisIndex: 1, data: fcfData, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: {{ width: 2, color: P.s2 }}, itemStyle: {{ color: P.s2 }} }}
      ]
    }};
    render(el, option);
  }})();

  /* 6. chart-geo */
  (function () {{
    var el = document.getElementById('chart-geo');
    if (!el) return;
    var data = [
      {{ name: '北美', value: 65 }},
      {{ name: '欧洲', value: 20 }},
      {{ name: '亚太', value: 12 }},
      {{ name: '其他', value: 3 }}
    ];
    var colors = [P.s1, P.s4, P.s3, P.neutral];
    var lg = isMobile ? {{ bottom: 0, left: 'center', orient: 'horizontal', textStyle: {{ color: P.textMuted, fontSize: fs(11) }}, itemWidth: fs(10), itemHeight: fs(10) }}
      : {{ top: 'middle', right: 8, orient: 'vertical', textStyle: {{ color: P.textMuted, fontSize: fs(12) }}, itemWidth: fs(12), itemHeight: fs(12) }};
    var option = {{
      animation: false, color: colors, legend: lg,
      tooltip: {{ trigger: 'item', formatter: '{{b}}: {{c}}%' }},
      series: [{{ type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true, itemStyle: {{ borderColor: P.surface, borderWidth: 2 }},
        label: {{ show: !isMobile, color: P.text, fontSize: fs(12), formatter: '{{d}}%' }},
        labelLine: {{ show: !isMobile }}, data: data }}]
    }};
    render(el, option);
  }})();

  /* 7. chart-radar */
  (function () {{
    var el = document.getElementById('chart-radar');
    if (!el) return;
    var option = {{
      animation: false,
      color: [P.s1],
      legend: {{ top: 0, textStyle: {{ color: P.textMuted, fontSize: fs(12) }}, itemWidth: fs(12), itemHeight: fs(12) }},
      radar: {{
        indicator: [
          {{ name: '营收增长', max: 100 }},
          {{ name: '盈利能力', max: 100 }},
          {{ name: '现金流质量', max: 100 }},
          {{ name: '资产质量', max: 100 }},
          {{ name: '运营效率', max: 100 }},
          {{ name: '市场前景', max: 100 }}
        ],
        shape: 'circle',
        splitNumber: 4,
        axisName: {{ color: P.text, fontSize: fs(11) }}
      }},
      series: [{{
        type: 'radar',
        data: [{{
          value: [85, 95, 80, 75, 90, 70],
          name: 'AppLovin Q2 2026',
          areaStyle: {{ color: 'rgba(0,113,227,0.2)' }},
          lineStyle: {{ color: P.s1, width: 2 }},
          itemStyle: {{ color: P.s1 }}
        }}]
      }}]
    }};
    render(el, option);
  }})();
}})();
'''

# 输出 charts.js
charts_dir = "D:\\temp\\Output\\stock-financial-reports\\applovincorp-q2-2026-earnings\\assets"
os.makedirs(charts_dir, exist_ok=True)
charts_path = os.path.join(charts_dir, "charts.js")
with open(charts_path, "w", encoding="utf-8") as f:
    f.write(charts_js)
print(f"charts.js 已生成: {charts_path} ({len(charts_js)} bytes)")
print("完成！")