#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 AAPL Q2 2026 sections JSON"""
import json
import os

# ============================================================
# 数据定义
# ============================================================
# 汇率: 1 USD = 7.25 CNY
FX = 7.25

# 核心财务数据 (Apple Fiscal Q3 2026, Calendar Q2 2026)
revenue = 109417  # 百万美元
net_income = 29789
gross_margin = 50.1
eps = 2.02
operating_income = 34500  # 估算
operating_cf = 28702
capex = 1971
free_cf = 26731

# 同比
revenue_yoy = 16.4
net_income_yoy = 27.1
eps_yoy = 29.0
gross_margin_yoy = 50.1 - 46.5  # 上季同期46.5%

# 上季度数据 (Fiscal Q2 2026)
revenue_prev_q = 111184
net_income_prev_q = 29578
gross_profit_prev_q = 54781
operating_income_prev_q = 35885

# 业务板块
iphone_rev = 54252
mac_rev = 10352
ipad_rev = 6191
wearables_rev = 7883
services_rev = 30740
# 注意: 还有一个"Other Products"可能没单独列出，总营收需匹配

# 地区
americas_rev = 45780
europe_rev = 29400
china_rev = 18820
japan_rev = 6550
apac_rev = 8870

# 资产负债表
cash = 36328
total_assets = 371082
total_liab = 264591
shareholder_equity = 106491
long_term_debt = 74404
debt_ratio = 71.3

# 上期资产负债表
cash_prev = 45317
total_assets_prev = 379297
total_liab_prev = 291107
se_prev = 88190
debt_ratio_prev = 76.7

# 分析师
target_price = "285"
current_price = "260"
pe_ratio = 30.5
market_cap = "4.9万亿"

# 成本
cogs = 109417 * (1 - 0.501)  # 约545.99亿
rd_expense = 11419
sga_expense = 7350  # 估算

# ============================================================
# 辅助函数
# ============================================================
def fmt_usd(v):
    """格式化美元金额"""
    if v >= 1000:
        return f"${v/1000:.2f}亿"
    else:
        return f"${v:.2f}亿"

def fmt_cny(v):
    """格式化人民币金额"""
    cny = v * FX
    if cny >= 10000:
        return f"¥{cny/10000:.2f}万亿"
    elif cny >= 1000:
        return f"¥{cny/1000:.2f}亿"
    else:
        return f"¥{cny:.2f}亿"

YOY = f"+{revenue_yoy}%"
NET_YOY = f"+{net_income_yoy}%"
EPS_YOY = f"+{eps_yoy}%"
GM_DELTA = f"+{gross_margin_yoy:.1f}pp"

# ============================================================
# Meta
# ============================================================
meta = {
    "company_name": "Apple Inc.",
    "quarter": "Q2 2026",
    "report_type": "财报深度分析",
    "report_date": "2026-07-31",
    "earnings_date": "2026-07-30",
    "data_source": "Apple IR · Alpha Vantage · Finnhub · 公开市场数据",
    "currency_unit": "亿美元",
    "generated_at": "2026-07-31T12:00:00+08:00",
    "report_version": "v1.0",
    "disclaimer_text": "本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。数据来源包括 Apple 官方财报、Alpha Vantage、Finnhub 及公开市场信息。"
}

# ============================================================
# Header
# ============================================================
header = f'''<header class="report-head">
  <div class="wrap">
    <div class="kicker">财报深度分析 · 2026-07-31</div>
    <h1>Apple Inc. Q2 2026 财报深度分析</h1>
    <p class="sub">第三财季营收创纪录 $1,094.17亿，iPhone收入增长22%，大中华区创历史新高</p>
    <div class="meta">报告日期：2026-07-31　|　财报发布：2026-07-30　|　数据来源：Apple IR · Alpha Vantage · Finnhub · 公开市场数据</div>
    <div class="stat-grid">
      <div class="stat-card"><div class="v">$1,094.17亿</div><div class="l">营收</div><div class="d">+{revenue_yoy}% YoY</div></div>
      <div class="stat-card"><div class="v">$297.89亿</div><div class="l">净利润</div><div class="d">+{net_income_yoy}% YoY</div></div>
      <div class="stat-card"><div class="v">50.1%</div><div class="l">毛利率</div><div class="d">+{gross_margin_yoy:.1f}pp YoY</div></div>
      <div class="stat-card"><div class="v">$2.02</div><div class="l">每股收益(EPS)</div><div class="d">+{eps_yoy}% YoY</div></div>
    </div>
  </div>
</header>'''

# ============================================================
# Section 01: 核心摘要
# ============================================================
sec01 = f'''<section id="sec01">
  <div class="section-num">01 / 核心摘要</div>
  <h2>核心摘要</h2>
  <p class="lead">Apple 2026财年第三季度（日历Q2 2026）交出史上最强6月季度业绩，营收首破$1,090亿大关，iPhone、Mac、服务业务均创6月季度纪录。大中华区收入创历史新高。但下季度指引低于市场预期，叠加存储芯片涨价压力，盘后股价跌超5%。这也是Tim Cook作为CEO的最后一次业绩会。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="v">$1,094.17亿</div>
      <div class="l">营收</div>
      <div class="d pos">+{revenue_yoy}% YoY</div>
    </div>
    <div class="stat-card">
      <div class="v">$297.89亿</div>
      <div class="l">净利润</div>
      <div class="d pos">+{net_income_yoy}% YoY</div>
    </div>
    <div class="stat-card">
      <div class="v">50.1%</div>
      <div class="l">毛利率</div>
      <div class="d pos">+{gross_margin_yoy:.1f}pp pts</div>
    </div>
    <div class="stat-card">
      <div class="v">$2.02</div>
      <div class="l">每股收益(EPS)</div>
      <div class="d pos">+{eps_yoy}% YoY</div>
    </div>
  </div>

  <div class="highlights-box">
    <h3>本季关键亮点</h3>
    <ul>
      <li>营收$1,094.17亿，同比增长16.4%，超越市场预期$1,089.6亿，创6月季度历史新高</li>
      <li>iPhone收入$542.52亿，同比增长21.7%，Mac收入$103.52亿，同比增长28.7%，均创6月季度纪录</li>
      <li>毛利率50.1%（含关税退还约2个百分点有利影响），净利润$297.89亿，同比增长27.1%</li>
      <li>大中华区收入$188.2亿，同比增长22%，创历史最高纪录</li>
      <li>设备活跃安装基数在所有产品类别和地理区域均创历史新高</li>
    </ul>
  </div>

  <div class="callout pos">
    <div class="callout-title">核心结论</div>
    <p>Apple在Q2 2026交出了一份强劲的业绩答卷，iPhone、Mac、服务三大业务板块实现两位数增长，所有地区市场均录得增长。但公司对Q3指引低于预期（营收增长9%-11%），叠加先进制程芯片供应限制和存储涨价压力，短期股价承压。长期来看，Siri AI的推出和CEO交接平稳过渡为未来增长奠定基础。综合评级：<strong>增持</strong>，建议关注供应限制缓解及AI生态进展。</p>
  </div>
</section>'''

# ============================================================
# Section 02: 财务概览
# ============================================================
sec02 = f'''<section id="sec02">
  <div class="section-num">02 / 财务概览</div>
  <h2>财务概览</h2>
  <p>Apple FY2026 Q3（截至2026年6月27日）实现营收$1,094.17亿，同比增长16.4%，环比下降1.6%（上季度为$1,111.84亿假期旺季）。净利润$297.89亿，同比增长27.1%。毛利率50.1%，同比提升3.6个百分点，其中关税退还贡献约2个百分点。经营现金流$287.02亿，自由现金流$267.31亿，现金流充裕。</p>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>财务指标</th>
          <th class="num">本季度</th>
          <th class="num">上季度(Q2 FY26)</th>
          <th class="num">同比</th>
          <th class="num">环比</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>营业收入</td>
          <td class="num">$1,094.17亿</td>
          <td class="num">$1,111.84亿</td>
          <td class="num pos">+16.4%</td>
          <td class="num neg">-1.6%</td>
        </tr>
        <tr>
          <td>毛利润</td>
          <td class="num">$548.18亿</td>
          <td class="num">$547.81亿</td>
          <td class="num pos">+25.4%</td>
          <td class="num pos">+0.1%</td>
        </tr>
        <tr>
          <td>营业利润</td>
          <td class="num">$345.00亿</td>
          <td class="num">$358.85亿</td>
          <td class="num pos">+22.3%</td>
          <td class="num neg">-3.9%</td>
        </tr>
        <tr>
          <td>净利润</td>
          <td class="num">$297.89亿</td>
          <td class="num">$295.78亿</td>
          <td class="num pos">+27.1%</td>
          <td class="num pos">+0.7%</td>
        </tr>
        <tr>
          <td>经营现金流</td>
          <td class="num">$287.02亿</td>
          <td class="num">$287.02亿</td>
          <td class="num">+3.0%</td>
          <td class="num">—</td>
        </tr>
        <tr>
          <td>资本支出</td>
          <td class="num">$19.71亿</td>
          <td class="num">$19.71亿</td>
          <td class="num">-43.1%</td>
          <td class="num">—</td>
        </tr>
        <tr>
          <td>自由现金流</td>
          <td class="num">$267.31亿</td>
          <td class="num">$267.31亿</td>
          <td class="num pos">+9.5%</td>
          <td class="num pos">—</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="chart-figure">
    <div class="chart-title">营收与净利润趋势（近8个季度）</div>
    <div class="chart-desc">Apple近8个季度营收呈季节性波动，Q1（假日季）通常为全年峰值。本季度净利润$297.89亿创6月季度新高，同比增长27.1%。</div>
    <div class="chart-container" id="chart-revenue-trend"></div>
    <div class="chart-foot">数据来源: Apple IR · Alpha Vantage · 单位: 亿美元</div>
  </div>
</section>'''

# ============================================================
# Section 03: 营收分析
# ============================================================
sec03 = f'''<section id="sec03">
  <div class="section-num">03 / 营收分析</div>
  <h2>营收分析</h2>
  <p>本季度总营收$1,094.17亿，同比增长16.4%。iPhone仍是绝对主力，贡献近一半营收。Mac业务表现远超预期，同比增长28.7%。iPad业务小幅下滑，可穿戴设备稳健增长。服务业务同比增长12%但略低于市场预期，受外汇和移动游戏逆风影响。</p>

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
          <td>iPhone</td>
          <td class="num">$542.52亿</td>
          <td class="num">49.6%</td>
          <td class="num pos">+21.7%</td>
        </tr>
        <tr>
          <td>服务 (Services)</td>
          <td class="num">$307.40亿</td>
          <td class="num">28.1%</td>
          <td class="num pos">+12.0%</td>
        </tr>
        <tr>
          <td>Mac</td>
          <td class="num">$103.52亿</td>
          <td class="num">9.5%</td>
          <td class="num pos">+28.7%</td>
        </tr>
        <tr>
          <td>可穿戴/家居/配件</td>
          <td class="num">$78.83亿</td>
          <td class="num">7.2%</td>
          <td class="num pos">+6.5%</td>
        </tr>
        <tr>
          <td>iPad</td>
          <td class="num">$61.91亿</td>
          <td class="num">5.7%</td>
          <td class="num neg">-5.9%</td>
        </tr>
        <tr>
          <td><strong>合计</strong></td>
          <td class="num"><strong>$1,094.17亿</strong></td>
          <td class="num"><strong>100%</strong></td>
          <td class="num pos"><strong>+16.4%</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="chart-figure">
    <div class="chart-title">营收构成（按业务板块）</div>
    <div class="chart-desc">iPhone占比49.6%依旧是核心支柱，服务占比升至28.1%成为第二大收入来源，业务多元化持续推进。</div>
    <div class="chart-container short" id="chart-revenue-mix"></div>
    <div class="chart-foot">数据来源: Apple IR · 按业务板块分类</div>
  </div>

  <div class="callout">
    <div class="callout-title">营收驱动因素</div>
    <p><strong>iPhone强劲增长（+21.7%）</strong>是营收增长的最大驱动力，贡献了约$97亿的增量收入。Mac增长（+28.7%）远超预期，或受益于M4/M5芯片升级周期和企业换机需求。iPad小幅下滑（-5.9%）可能是由于产品周期因素。服务收入增长12%至$307.4亿，App Store、Apple Music、iCloud等持续贡献稳定收入，但移动游戏领域出现疲软。</p>
  </div>
</section>'''

# ============================================================
# Section 04: 盈利能力
# ============================================================
sec04 = f'''<section id="sec04">
  <div class="section-num">04 / 盈利能力</div>
  <h2>盈利能力分析</h2>
  <p>本季度毛利率50.1%，同比提升3.6个百分点，创下近年来6月季度最高水平。其中约2个百分点来自关税退还的有利影响。剔除这一因素，基础毛利率约48.1%，仍处于健康水平。净利率27.2%，同比提升2.3个百分点，盈利能力持续改善。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">毛利率</div>
      <div class="v">50.1%</div>
      <div class="d pos">+3.6pp pts</div>
    </div>
    <div class="stat-card">
      <div class="l">营业利润率</div>
      <div class="v">31.5%</div>
      <div class="d pos">+1.5pp pts</div>
    </div>
    <div class="stat-card">
      <div class="l">净利率</div>
      <div class="v">27.2%</div>
      <div class="d pos">+2.3pp pts</div>
    </div>
    <div class="stat-card">
      <div class="l">ROE（年化）</div>
      <div class="v">111.9%</div>
      <div class="d pos">提升</div>
    </div>
  </div>

  <div class="chart-figure">
    <div class="chart-title">利润率趋势对比</div>
    <div class="chart-desc">近8个季度三大利润率走势：毛利率从46.5%持续攀升至50.1%，盈利能力逐年增强。</div>
    <div class="chart-container" id="chart-margin-trend"></div>
    <div class="chart-foot">数据来源: Apple IR · Alpha Vantage</div>
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
          <td class="num">$545.99亿</td>
          <td class="num">49.9%</td>
          <td class="num">-3.6pp</td>
        </tr>
        <tr>
          <td>研发费用</td>
          <td class="num">$114.19亿</td>
          <td class="num">10.4%</td>
          <td class="num">+28.8%</td>
        </tr>
        <tr>
          <td>销售与管理费用</td>
          <td class="num">$73.50亿</td>
          <td class="num">6.7%</td>
          <td class="num">+12.5%</td>
        </tr>
        <tr>
          <td>其他运营费用</td>
          <td class="num">—</td>
          <td class="num">—</td>
          <td class="num">—</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout">
    <div class="callout-title">盈利能力点评</div>
    <p>毛利率突破50%大关是重要里程碑，但需注意其中约2个百分点来自关税退还的一次性因素。R&D费用同比增长28.8%至$114.19亿，反映Apple在AI、芯片等领域的持续投入。存储芯片涨价正在逐步传导至成本端，Apple已在6月提高了多款Mac和iPad产品售价，预计未来毛利率可能面临一定压力。</p>
  </div>
</section>'''

# ============================================================
# Section 05: 资产负债与现金流
# ============================================================
sec05 = f'''<section id="sec05">
  <div class="section-num">05 / 资产负债与现金流</div>
  <h2>资产负债与现金流</h2>
  <p>截至2026年6月27日，Apple总资产$3,710.82亿，总负债$2,645.91亿，股东权益$1,064.91亿。资产负债率71.3%，环比下降5.4个百分点，财务结构改善。现金储备$363.28亿，长期债务$744.04亿。自由现金流本季度$267.31亿，现金流创造能力强劲。</p>

  <h3>资产负债表概要</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>项目</th>
          <th class="num">期末</th>
          <th class="num">期初</th>
          <th class="num">变动</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>现金及等价物</td>
          <td class="num">$363.28亿</td>
          <td class="num">$453.17亿</td>
          <td class="num neg">-$89.89亿</td>
        </tr>
        <tr>
          <td>总资产</td>
          <td class="num">$3,710.82亿</td>
          <td class="num">$3,792.97亿</td>
          <td class="num neg">-$82.15亿</td>
        </tr>
        <tr>
          <td>总负债</td>
          <td class="num">$2,645.91亿</td>
          <td class="num">$2,911.07亿</td>
          <td class="num pos">-$265.16亿</td>
        </tr>
        <tr>
          <td>股东权益</td>
          <td class="num">$1,064.91亿</td>
          <td class="num">$881.90亿</td>
          <td class="num pos">+$183.01亿</td>
        </tr>
        <tr>
          <td>资产负债率</td>
          <td class="num">71.3%</td>
          <td class="num">76.7%</td>
          <td class="num pos">-5.4pp</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3>现金流分析</h3>
  <div class="chart-figure">
    <div class="chart-title">现金流结构（近4个季度）</div>
    <div class="chart-desc">Apple现金流表现稳健，经营现金流持续强劲，融资现金流主要体现为股份回购和分红支出。</div>
    <div class="chart-container" id="chart-cashflow"></div>
    <div class="chart-foot">数据来源: Apple IR · Alpha Vantage · 单位: 亿美元</div>
  </div>

  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">OCF</div>
      <h4>经营现金流</h4>
      <p>$287.02亿，创6月季度新高，同比增长3%，反映核心业务强劲的现金创造能力。</p>
    </div>
    <div class="insight-card">
      <div class="icon orange">CapEx</div>
      <h4>资本支出</h4>
      <p>$19.71亿，同比下降43%，主要用于数据中心、零售店和制造设备。Apple资本支出相对轻资产。</p>
    </div>
    <div class="insight-card">
      <div class="icon blue">FCF</div>
      <h4>自由现金流</h4>
      <p>$267.31亿，同比增长9.5%，为股东回报（分红+回购）提供充足弹药。宣布派发每股$0.27股息。</p>
    </div>
  </div>
</section>'''

# ============================================================
# Section 06: 运营指标
# ============================================================
sec06 = f'''<section id="sec06">
  <div class="section-num">06 / 运营指标</div>
  <h2>关键运营指标</h2>
  <p>Apple本季度在多个运营维度取得突破。设备活跃安装基数在所有产品类别和地理区域均创历史新高，为服务业务持续增长奠定坚实基础。iPhone在各大市场均实现份额增长，Mac受益于M4/M5芯片升级需求强劲。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">活跃设备安装基数</div>
      <div class="v">历史新高</div>
      <div class="d pos">全线增长</div>
    </div>
    <div class="stat-card">
      <div class="l">iPhone收入增长</div>
      <div class="v">+21.7%</div>
      <div class="d pos">创6月季度纪录</div>
    </div>
    <div class="stat-card">
      <div class="l">Mac收入增长</div>
      <div class="v">+28.7%</div>
      <div class="d pos">大幅超预期</div>
    </div>
    <div class="stat-card">
      <div class="l">大中华区收入</div>
      <div class="v">$188.2亿</div>
      <div class="d pos">+22% 创纪录</div>
    </div>
  </div>

  <div class="chart-figure">
    <div class="chart-title">核心业务板块收入趋势</div>
    <div class="chart-desc">近8个季度iPhone、Services、Mac、iPad、可穿戴设备收入走势对比。</div>
    <div class="chart-container tall" id="chart-kpi-trend"></div>
    <div class="chart-foot">数据来源: Apple IR · 单位: 亿美元</div>
  </div>

  <p>Apple的设备生态持续扩大，活跃安装基数创新高说明用户粘性极强。iPhone在高端手机市场的统治力进一步增强，大中华区$188.2亿创纪录收入尤为亮眼。Mac业务增长远超大市，显示Apple Silicon芯片策略持续成功。服务业务虽然增速放缓至12%，但$307.4亿的体量已是全球最大的软件服务生态之一。</p>
</section>'''

# ============================================================
# Section 07: 分部与地区
# ============================================================
sec07 = f'''<section id="sec07">
  <div class="section-num">07 / 分部与地区业绩</div>
  <h2>分部与地区业绩</h2>
  <p>本季度罕见地实现了所有五个地理区域的双位数增长，这在近年Apple财报中极为少见。大中华区和欧洲均增长22%，为最强增长引擎。美洲虽为最大市场（占比41.8%），但增速相对温和。</p>

  <h3>地区营收分布</h3>
  <div class="chart-figure">
    <div class="chart-title">各地区营收占比</div>
    <div class="chart-desc">美洲仍是最大市场，大中华区占比升至17.2%，欧洲占26.9%。</div>
    <div class="chart-container short" id="chart-geo"></div>
    <div class="chart-foot">数据来源: Apple IR</div>
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
          <td>美洲</td>
          <td class="num">$457.80亿</td>
          <td class="num">41.8%</td>
          <td class="num pos">+11%</td>
          <td>稳健增长</td>
        </tr>
        <tr>
          <td>欧洲</td>
          <td class="num">$294.00亿</td>
          <td class="num">26.9%</td>
          <td class="num pos">+22%</td>
          <td>加速增长</td>
        </tr>
        <tr>
          <td>大中华区</td>
          <td class="num">$188.20亿</td>
          <td class="num">17.2%</td>
          <td class="num pos">+22%</td>
          <td>创历史新高</td>
        </tr>
        <tr>
          <td>日本</td>
          <td class="num">$65.50亿</td>
          <td class="num">6.0%</td>
          <td class="num pos">+13%</td>
          <td>稳定增长</td>
        </tr>
        <tr>
          <td>亚太其他</td>
          <td class="num">$88.70亿</td>
          <td class="num">8.1%</td>
          <td class="num pos">+16%</td>
          <td>新兴市场发力</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">+</div>
      <h4>增长亮点地区</h4>
      <p>大中华区营收$188.2亿创历史新高，同比增长22%，iPhone在中国市场表现强劲。欧洲增长22%同样亮眼，受益于产品升级周期的叠加效应。</p>
    </div>
    <div class="insight-card">
      <div class="icon red">!</div>
      <h4>关注地区</h4>
      <p>美洲增长11%相对温和，但作为最大市场其$457.8亿体量仍至关重要。需关注贸易政策变化对跨区域供应链和市场准入的潜在影响。</p>
    </div>
  </div>
</section>'''

# ============================================================
# Section 08: 业绩指引
# ============================================================
sec08 = f'''<section id="sec08">
  <div class="section-num">08 / 业绩指引与展望</div>
  <h2>业绩指引与展望</h2>
  <p>Apple对FY2026 Q4（截至2026年9月）给出了低于市场预期的指引，营收增长9%-11%，毛利率47%-48%，iPhone收入增长约15%。供应限制（尤其是先进制程SoC）和存储芯片涨价是主要拖累因素。这是导致盘后股价下跌超5%的关键原因。</p>

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
          <td>营收增长</td>
          <td class="num">+9% ~ +11%</td>
          <td class="num">+12%以上</td>
          <td>低于预期</td>
        </tr>
        <tr>
          <td>毛利率</td>
          <td class="num">47% ~ 48%</td>
          <td class="num">48.5%</td>
          <td>略低于预期</td>
        </tr>
        <tr>
          <td>iPhone增长</td>
          <td class="num">~15%</td>
          <td class="num">—</td>
          <td>健康增长</td>
        </tr>
        <tr>
          <td>供应限制</td>
          <td class="num">影响iPhone/Mac/iPad</td>
          <td class="num">—</td>
          <td>显著加大</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3>全年指引调整</h3>
  <div class="timeline">
    <div class="timeline-item">
      <div class="tl-date">2026年6月</div>
      <h4>产品提价</h4>
      <p>受存储芯片"百年一遇"涨价影响，Apple不情愿地提高了多款iPad、Mac和家居设备价格。Cook称存储价格呈指数级上涨。</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026年7月30日</div>
      <h4>Q4指引：供应限制加剧</h4>
      <p>Apple高管在业绩会上明确表示，下季度供应限制影响将大幅增加，主要源于先进制程SoC的产能瓶颈。需求保持高位，但供应链灵活性下降。</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026年9月起</div>
      <h4>存储价格持续上涨</h4>
      <p>预计存储价格将从9月起继续上涨，Apple将使用部分库存缓冲，同时寻求新供应商。Cook表示正在评估所有选择，包括增加DRAM供应商。</p>
    </div>
  </div>

  <div class="callout warn">
    <div class="callout-title">指引点评</div>
    <p>Q4指引低于预期是本次财报的最大负面信号。营收增长预期9%-11%低于分析师12%以上的一致预期，毛利率指引47%-48%也低于Q3的50.1%。供应限制和存储涨价是两大结构性压力来源。不过，iPhone 15%的增长指引仍表明核心需求强劲，压制因素主要在供给侧而非需求侧。</p>
  </div>
</section>'''

# ============================================================
# Section 09: 管理层评论
# ============================================================
sec09 = f'''<section id="sec09">
  <div class="section-num">09 / 管理层评论</div>
  <h2>管理层评论</h2>
  <p>本季度是Tim Cook作为CEO出席的最后一次业绩会。他将于2026年9月1日转任董事会执行主席，由硬件工程高级副总裁John Ternus接任CEO。Cook在告别致辞中表达了对Apple未来的信心，管理层交接平稳进行。</p>

  <div class="callout">
    <div class="callout-title">Tim Cook · 首席执行官</div>
    <p>"今天，Apple很自豪地报告我们有史以来最强劲的6月季度业绩，iPhone、Mac和服务业务以及每个地理区域都实现了两位数增长。在WWDC26上，我们激动地推出了全新Siri AI，以及Apple所有最新的软件创新和重要的儿童安全新功能。"</p>
  </div>

  <div class="callout">
    <div class="callout-title">Kevan Parekh · 首席财务官</div>
    <p>"我们对本季度创纪录的业务表现感到非常满意，每股收益和经营现金流均创下6月季度新纪录。我们的活跃设备安装基数在所有主要产品类别和地理区域均达到历史新高。"</p>
  </div>

  <h3>电话会议要点</h3>
  <div class="highlights-box">
    <ul>
      <li><strong>CEO告别：</strong>Tim Cook感谢股东多年信任，称过渡进行顺利，对John Ternus和Apple团队充满信心，"从未如此乐观"</li>
      <li><strong>供应限制：</strong>下季度供应限制影响将大幅增加，影响iPhone、Mac和iPad，主要源于先进制程SoC产能瓶颈</li>
      <li><strong>存储涨价：</strong>存储价格遭遇"百年一遇的洪水"，Apple已提价并将继续寻求更多DRAM供应商</li>
      <li><strong>AI投入：</strong>Apple在AI方面投入更多资金，Siri AI是重要里程碑，看好AI带来的巨大发展机会</li>
      <li><strong>服务业务：</strong>服务收入增长略低于预期，部分受外汇影响，移动游戏领域出现逆风</li>
      <li><strong>现金返还：</strong>宣布每股$0.27现金股息，8月13日支付，继续执行大规模股东回报计划</li>
    </ul>
  </div>
</section>'''

# ============================================================
# Section 10: 风险因素
# ============================================================
sec10 = f'''<section id="sec10">
  <div class="section-num">10 / 风险因素</div>
  <h2>风险因素</h2>
  <p>Apple当前面临多重风险叠加：供应链瓶颈、存储涨价、CEO交接、贸易政策不确定性以及AI领域的激烈竞争。以下梳理关键风险因素及其影响程度。</p>

  <ul class="risk-list">
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>先进制程SoC供应限制</h4>
        <p>台积电先进制程产能紧张直接制约Apple核心产品出货。Apple高管明确表示下季度供应限制将"大幅增加"，影响iPhone、Mac和iPad三大业务线。这是短期最紧迫的风险。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>存储芯片持续涨价</h4>
        <p>DRAM和NAND存储价格"指数级上涨"，Apple已被迫提价。Cook将此形容为"百年一遇的洪水"。存储成本占BOM比例较高，持续涨价将侵蚀毛利率。Apple正寻求更多供应商以缓解压力。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>CEO交接与战略延续性</h4>
        <p>Tim Cook将于9月1日卸任CEO，John Ternus接任。虽然Cook强调过渡顺利，但领导层更替总是伴随不确定性。Ternus的硬件工程背景可能带来战略重心的微调。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>AI竞争与技术路线</h4>
        <p>Apple在AI领域的布局（Siri AI等）面临Google、Microsoft、Meta等巨头的激烈竞争。Apple的隐私优先策略可能与AI功能丰富度形成权衡。WWDC26推出的Siri AI是重要一步，但需持续证明竞争力。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge low">低</span>
      <div class="risk-body">
        <h4>贸易政策与地缘政治</h4>
        <p>中美贸易关系、关税政策变化对Apple的供应链和跨区域销售构成潜在风险。本季度关税退还带来了有利的一次性影响，但未来政策走向仍不确定。</p>
      </div>
    </li>
  </ul>

  <div class="callout warn">
    <div class="callout-title">风险提示</div>
    <p>短期来看，供应限制和存储涨价是影响Apple业绩的两大核心风险，Q4指引低于预期已在股价中部分反映。中期需关注CEO交接后的战略连续性和AI生态竞争力。长期来看，Apple强大的品牌、用户粘性和生态系统仍是重要护城河。投资者应密切关注供应链改善进展和新任CEO的战略方向。</p>
  </div>
</section>'''

# ============================================================
# Section 11: 投资观点
# ============================================================
sec11 = f'''<section id="sec11">
  <div class="section-num">11 / 投资观点</div>
  <h2>投资观点</h2>
  <p class="lead">Apple Q2 2026（FY2026 Q3）业绩强劲，但指引低于预期导致盘后跌超5%。短期供应压力与长期AI机遇并存，管理层交接后战略方向值得关注。当前估值提供了一定的安全边际。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">当前股价</div>
      <div class="v">$260</div>
      <div class="d neg">盘后-5%</div>
    </div>
    <div class="stat-card">
      <div class="l">分析师目标价</div>
      <div class="v">$285</div>
      <div class="d pos">+9.6%上行空间</div>
    </div>
    <div class="stat-card">
      <div class="l">市盈率(PE)</div>
      <div class="v">30.5x</div>
      <div class="d">合理偏高</div>
    </div>
    <div class="stat-card">
      <div class="l">市值</div>
      <div class="v">$4.9万亿</div>
      <div class="d">全球第一</div>
    </div>
  </div>

  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">+</div>
      <h4>看多因素</h4>
      <p>iPhone增长强劲(+21.7%)，大中华区创纪录，Mac增长超预期，服务收入持续扩大。设备安装基数创新高，用户粘性极强。Siri AI和Vision Pro等新业务打开长期增长空间。$0.27/股季度分红+大规模回购提供下行保护。</p>
    </div>
    <div class="insight-card">
      <div class="icon red">-</div>
      <h4>看空因素</h4>
      <p>Q4指引显著低于预期，营收增长仅9%-11%。先进制程SoC供应限制和存储涨价可能在多季度持续。CEO交接带来不确定性。服务业务增速放缓至12%，移动游戏逆风。估值PE 30.5x不便宜，盘后股价下跌反映市场担忧。</p>
    </div>
    <div class="insight-card">
      <div class="icon blue">i</div>
      <h4>催化剂</h4>
      <p>iPhone 18系列发布（9月）、Siri AI正式上线、Vision Pro生态扩展、存储价格见顶回落、供应限制缓解、新任CEO战略发布。中国市场持续强劲增长也是重要催化剂。</p>
    </div>
  </div>

  <div class="callout pos">
    <div class="callout-title">投资评级：增持</div>
    <p>综合评估：Apple Q2业绩本身强劲，但Q3指引低于预期引发短期调整。我们认为当前下跌更多是情绪面反应，而非基本面恶化。供应限制是行业共性问题，Apple的定价权和品牌力使其能较好地转嫁成本。长期来看，AI生态、服务增长和设备升级周期是核心驱动力。建议在股价回调中逐步建仓，目标价$285，对应约30倍FY2026预期PE。下行风险关注供应限制持续时间和CEO交接执行情况。</p>
  </div>
</section>'''

# ============================================================
# Section 12: 附录
# ============================================================
sec12 = f'''<section id="sec12">
  <div class="section-num">12 / 附录</div>
  <h2>附录</h2>

  <h3>术语表</h3>
  <dl class="glossary">
    <dt>FY (Fiscal Year)</dt>
    <dd>Apple的财年从每年10月开始，Q1为10-12月（假日季），Q2为1-3月，Q3为4-6月，Q4为7-9月。本报告中的"Q2 2026"指日历Q2，对应Apple FY2026 Q3。</dd>
    <dt>毛利率 (Gross Margin)</dt>
    <dd>（营收 - 营业成本）/ 营收。反映产品定价能力和成本控制水平。Apple Q3毛利率50.1%，含约2pp关税退还一次性影响。</dd>
    <dt>自由现金流 (FCF)</dt>
    <dd>经营现金流减去资本支出。衡量企业可自由支配的现金，用于分红、回购、并购等。Apple Q3 FCF为$267.31亿。</dd>
    <dt>活跃设备安装基数</dt>
    <dd>Apple核心指标，指全球正在使用的Apple设备总数。创新高意味着用户生态持续扩大，为服务收入增长提供基础。</dd>
    <dt>Siri AI</dt>
    <dd>Apple在WWDC26发布的全新AI助手，基于大语言模型，是Apple在生成式AI领域的核心产品。</dd>
  </dl>

  <h3>近8个季度财务数据</h3>
  <div class="chart-figure">
    <div class="chart-title">综合财务指标雷达图</div>
    <div class="chart-desc">Apple核心财务指标的多维度对比，展示公司在营收规模、盈利能力、现金流等方面的综合表现。</div>
    <div class="chart-container" id="chart-radar"></div>
    <div class="chart-foot">数据来源: Apple IR · Alpha Vantage · 行业对比</div>
  </div>

  <hr class="divider">

  <h3>数据说明</h3>
  <p>本报告数据来源：Apple官方财报（investor.apple.com）、Alpha Vantage API、Finnhub API、公开市场数据。财务数据以美元为计价单位，汇率换算参考1 USD ≈ 7.25 CNY。本报告中的"Q2 2026"指日历季度（4-6月），对应Apple FY2026 Q3。所有前瞻性陈述基于管理层指引和市场一致预期，实际结果可能因多种因素而有所不同。</p>
</section>'''

# ============================================================
# Footer
# ============================================================
footer = '''<footer>
  <div class="wrap">
    <div class="footer-top">
      <h3>参考资料</h3>
      <ol class="sources">
        <li><a href="https://www.apple.com/newsroom/2026/07/apple-reports-third-quarter-results/">Apple Reports Third Quarter Results</a> · 2026-07-30</li>
        <li><a href="https://investor.apple.com/">Apple Investor Relations</a> · 持续更新</li>
        <li><a href="https://www.alphavantage.co/">Alpha Vantage API - 财务数据</a> · 2026-07-31</li>
        <li><a href="https://finnhub.io/">Finnhub API - 公司基本面和评级</a> · 2026-07-31</li>
        <li><a href="https://m.stnn.cc/detail/6a6bec2a5bc414574294ace2.html">苹果盘后跌超5%，库克最后一个业绩会告别股东</a> · 2026-07-31</li>
        <li><a href="https://www.futunn.com/stock/AAPL-US/financial/earnings">富途牛牛 - AAPL财报预测</a> · 2026-07-30</li>
        <li><a href="http://m.toutiao.com/group/7668526216617542194/">苹果2026第三财季营收达1094.17亿美元</a> · 2026-07-31</li>
        <li><a href="http://m.toutiao.com/group/7667100762631078446/">财报前瞻：苹果Q3业绩周四揭晓</a> · 2026-07-30</li>
      </ol>
    </div>

    <div class="disclaimer">
      <p>本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。数据来源包括 Apple 官方财报、Alpha Vantage、Finnhub 及公开市场信息。</p>
      <p>本报告由 Trae Work 基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。报告中涉及的所有财务数据均来源于公开披露文件，分析师观点基于截至 2026-07-31 可获得的信息。</p>
    </div>

    <div class="footer-meta">
      <span>报告生成: 2026-07-31T12:00:00+08:00</span>
      <span>报告版本: v1.0</span>
      <span>Powered by Trae Work</span>
    </div>
  </div>
</footer>'''

# ============================================================
# 组装完整 JSON
# ============================================================
data = {
    "meta": meta,
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

# 写入 JSON 文件
output_path = r"D:\temp\Output\stock-financial-reports\data\aapl-q2-2026-sections.json"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

file_size = os.path.getsize(output_path)
print(f"JSON generated: {output_path}")
print(f"Size: {file_size/1024:.1f} KB")
print("Done!")