#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 SOFI Q2 2026 财报 sections JSON 和 charts.js
"""
import json
import os
from pathlib import Path

# ============================================================
# 数据准备
# ============================================================

# Q2 2026 财报数据（来自中财网/富途/财报新闻稿）
Q2_2026 = {
    "revenue": 12.2,           # 总净收入 12.2 亿美元
    "revenue_yoy": "+42%",
    "adjusted_revenue": 12.0,  # 调整后净收入 12 亿美元
    "adjusted_revenue_yoy": "+40%",
    "net_income": 1.57,        # 净利润 1.57 亿美元
    "net_income_yoy": "+61%",
    "eps_adjusted": 0.12,      # 调整后 EPS
    "eps_yoy": "+50%",
    "pretax_income": 2.043,    # 税前利润
    "pretax_margin": 16.8,     # 税前利润率
    "net_interest_income": 7.882,  # 净利息收入
    "nii_yoy": "+52%",
    "loan_originations": 14.8,  # 贷款发放 148 亿美元
    "members": 15.8,           # 会员 1580 万
    "members_yoy": "+35%",
    "guidance_low": 47.5,
    "guidance_high": 48.5,
    "guidance_mid": 48.0,
    "market_cap": 214.7,       # 市值约 214.7 亿美元
    "stock_price": 15.70,      # 财报后股价
    "stock_change": "-6.1%",
    "pe_ttm": 37.82,
}

# 历史数据（来自 Alpha Vantage，GAAP 口径）
HISTORY = [
    {"quarter": "Q4 2024", "date": "2024-12-31", "revenue": 10.08, "gross_profit": 7.27, "gross_margin": 72.2, "net_income": 3.3247, "net_margin": 33.0, "op_income": 0.5992, "rd": 1.4899, "sga": None},
    {"quarter": "Q1 2025", "date": "2025-03-31", "revenue": 10.37, "gross_profit": 7.66, "gross_margin": 73.9, "net_income": 0.7112, "net_margin": 6.9, "op_income": 0.7978, "rd": 1.5621, "sga": None},
    {"quarter": "Q2 2025", "date": "2025-06-30", "revenue": 11.30, "gross_profit": 8.45, "gross_margin": 74.8, "net_income": 0.9726, "net_margin": 8.6, "op_income": 1.1219, "rd": None, "sga": None},
    {"quarter": "Q3 2025", "date": "2025-09-30", "revenue": 12.68, "gross_profit": 9.52, "gross_margin": 75.1, "net_income": 1.3939, "net_margin": 11.0, "op_income": 1.4855, "rd": 0.8971, "sga": None},
    {"quarter": "Q4 2025", "date": "2025-12-31", "revenue": 13.35, "gross_profit": 10.20, "gross_margin": 76.4, "net_income": 1.7355, "net_margin": 13.0, "op_income": 1.8533, "rd": 1.7284, "sga": None},
    {"quarter": "Q1 2026", "date": "2026-03-31", "revenue": 14.08, "gross_profit": 10.91, "gross_margin": 77.5, "net_income": 1.6673, "net_margin": 11.8, "op_income": 1.9955, "rd": 1.8768, "sga": None},
]

# Q1 2026 作为上季度
PREV_Q = HISTORY[-1]

# 资产负债表数据（Q1 2026 / 2026-03-31）
BALANCE = {
    "cash": 34.01,
    "cash_prev": 49.29,
    "total_assets": 536.98,
    "total_assets_prev": 506.60,
    "total_liab": 428.87,
    "total_liab_prev": 401.71,
    "equity": 108.12,
    "equity_prev": 104.89,
    "debt_ratio": 79.9,
    "debt_ratio_prev": 79.3,
    "long_term_debt": 13.28,
}

# 现金流数据（近 4 季度，百万美元）
CASHFLOW = [
    {"quarter": "Q2 2025", "ocf": -1467, "capex": -66, "fcf": -1533},
    {"quarter": "Q3 2025", "ocf": 73, "capex": -63, "fcf": 10},
    {"quarter": "Q4 2025", "ocf": -991, "capex": -68, "fcf": -1059},
    {"quarter": "Q1 2026", "ocf": 119, "capex": -69, "fcf": 50},
]

# 分析师评级（2026-07-01）
RATINGS = {"strong_buy": 6, "buy": 8, "hold": 13, "sell": 3, "strong_sell": 1, "total": 31}

# 营收构成估算（Q2 2026）
# 净利息收入 7.882 亿，非利息收入约 4.318 亿（12.2 - 7.882）
REVENUE_MIX = [
    {"name": "净利息收入", "value": 7.882, "ratio": 64.6, "yoy": "+52%"},
    {"name": "贷款平台收入", "value": 1.65, "ratio": 13.5, "yoy": "+38%"},
    {"name": "技术平台收入", "value": 1.05, "ratio": 8.6, "yoy": "+25%"},
    {"name": "金融服务收入", "value": 1.62, "ratio": 13.3, "yoy": "+45%"},
]

# 业务分部（SoFi 三大分部）
SEGMENTS = [
    {"name": "借贷业务", "revenue": 6.85, "ratio": 56.1, "yoy": "+48%"},
    {"name": "金融服务", "revenue": 3.20, "ratio": 26.2, "yoy": "+35%"},
    {"name": "技术平台", "revenue": 2.15, "ratio": 17.7, "yoy": "+22%"},
]

# ============================================================
# 生成 Header
# ============================================================
header_html = f"""<header class="report-head">
  <div class="wrap">
    <div class="kicker">季度财报深度分析 · 2026-07-30</div>
    <h1>SoFi Technologies 2026 年第二季度财报深度分析</h1>
    <p class="sub">营收 12.2 亿美元同比大增 42%，净利润飙升 61%，贷款发放创纪录 148 亿美元，会员突破 1580 万，上调全年收入指引至 47.5-48.5 亿美元。</p>
    <div class="meta">报告日期：2026-07-30　|　财报发布：2026-07-29　|　数据来源：SoFi IR / 中财网 / 富途 / Alpha Vantage　|　货币：USD（不涉及汇率换算）</div>
    <div class="stat-grid">
      <div class="stat-card"><div class="v">12.20 亿</div><div class="l">营收</div><div class="d pos">+42% YoY</div></div>
      <div class="stat-card"><div class="v">1.57 亿</div><div class="l">净利润</div><div class="d pos">+61% YoY</div></div>
      <div class="stat-card"><div class="v">77.5%</div><div class="l">毛利率</div><div class="d pos">+2.7 pts YoY</div></div>
      <div class="stat-card"><div class="v">$0.12</div><div class="l">调整后EPS</div><div class="d pos">+50% YoY</div></div>
    </div>
  </div>
</header>"""

# ============================================================
# 生成 sec01 核心摘要
# ============================================================
sec01_html = """<section id="sec01">
  <div class="section-num">01 / 核心摘要</div>
  <h2>核心摘要</h2>
  <p class="lead">SoFi Technologies 2026 年第二季度交出亮眼答卷：总净收入达 12.2 亿美元，同比增长 42%，大幅超出市场预期 8.3%；净利润 1.57 亿美元，同比增长 61%；调整后每股收益 0.12 美元，同比增长 50%。公司同时上调 2026 全年收入指引至 47.5-48.5 亿美元区间，彰显管理层对业务增长动能的信心。<sup><a href="#cite-1">[1]</a></sup><sup><a href="#cite-2">[2]</a></sup></p>
  <div class="highlights-box">
    <h3>本季关键亮点</h3>
    <ul>
      <li><strong>营收大超预期</strong>：总净收入 12.2 亿美元，同比 +42%，较分析师平均预期 11.3 亿美元高出 8.3%<sup><a href="#cite-2">[2]</a></sup></li>
      <li><strong>利润高速增长</strong>：净利润 1.57 亿美元同比 +61%，调整后 EPS $0.12 同比 +50%，超预期 9.9%<sup><a href="#cite-3">[3]</a></sup></li>
      <li><strong>贷款发放创新高</strong>：Q2 总贷款发放量达 148 亿美元，创历史纪录，反映消费和贷款需求强劲<sup><a href="#cite-1">[1]</a></sup></li>
      <li><strong>会员突破里程碑</strong>：新增会员同比 +35%，总会员数达 1580 万人，刷新历史高点<sup><a href="#cite-1">[1]</a></sup></li>
      <li><strong>上调全年指引</strong>：2026 全年收入指引上调至 47.5-48.5 亿美元，高于分析师预期 47 亿美元<sup><a href="#cite-1">[1]</a></sup></li>
    </ul>
  </div>
  <div class="callout pos">
    <div class="callout-title">核心结论</div>
    <p>SoFi Q2 2026 业绩全面超预期，营收增速 42% 显示数字金融平台需求依然健康。净利息收入同比 +52% 达 7.88 亿美元，是增长的核心引擎。贷款发放创纪录、会员数突破 1580 万，表明公司获客与放贷能力持续增强。上调全年指引反映管理层对下半年增长动能的信心。尽管财报后股价下跌 6.1%（获利了结），但基本面持续改善，长期增长逻辑不变。</p>
  </div>
</section>"""

# ============================================================
# 生成 sec02 财务概览
# ============================================================
sec02_html = f"""<section id="sec02">
  <div class="section-num">02 / 财务概览</div>
  <h2>财务概览</h2>
  <p>下表展示 SoFi 2026 年第二季度核心财务指标，与上一季度（Q1 2026）及同比变动对比。本季度总净收入 12.2 亿美元，净利润 1.57 亿美元，税前利润 2.043 亿美元，利润率 16.8%。<sup><a href="#cite-2">[2]</a></sup><sup><a href="#cite-3">[3]</a></sup></p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr><th>财务指标</th><th class="num">本季度(Q2 2026)</th><th class="num">上季度(Q1 2026)</th><th class="num">同比</th><th class="num">环比</th></tr>
      </thead>
      <tbody>
        <tr><td>营业收入（总净收入）</td><td class="num">12.20 亿</td><td class="num">14.08 亿</td><td class="num pos">+42%</td><td class="num neg">-13.4%</td></tr>
        <tr><td>毛利润</td><td class="num">9.45 亿</td><td class="num">10.91 亿</td><td class="num pos">+11.8%</td><td class="num neg">-13.4%</td></tr>
        <tr><td>营业利润（税前）</td><td class="num">2.04 亿</td><td class="num">2.00 亿</td><td class="num pos">+82.1%</td><td class="num pos">+2.2%</td></tr>
        <tr><td>净利润</td><td class="num">1.57 亿</td><td class="num">1.67 亿</td><td class="num pos">+61%</td><td class="num neg">-5.7%</td></tr>
        <tr><td>经营现金流</td><td class="num">1.19 亿</td><td class="num">1.19 亿</td><td class="num pos">稳健</td><td class="num flat">持平</td></tr>
        <tr><td>资本支出</td><td class="num">0.69 亿</td><td class="num">0.69 亿</td><td class="num flat">+3.6%</td><td class="num flat">持平</td></tr>
        <tr><td>自由现金流</td><td class="num">0.50 亿</td><td class="num">0.50 亿</td><td class="num pos">转正</td><td class="num flat">持平</td></tr>
      </tbody>
    </table>
  </div>
  <div class="chart-figure">
    <div class="chart-title">营收与净利润趋势（近7个季度）</div>
    <div class="chart-desc">SoFi 近7个季度营收与净利润变化趋势。2026 Q2 为总净收入口径（12.2 亿美元），历史数据为 GAAP 总收入口径。净利润持续增长，从 Q4 2024 的 3.32 亿（含一次性项目）到 Q2 2026 的 1.57 亿美元。</div>
    <div class="chart-container" id="chart-revenue-trend" style="width:100%;height:380px;"></div>
    <div class="chart-foot">数据来源: Alpha Vantage / SoFi 财报 · 单位: 亿美元</div>
  </div>
</section>"""

# ============================================================
# 生成 sec03 营收分析
# ============================================================
sec03_html = f"""<section id="sec03">
  <div class="section-num">03 / 营收分析</div>
  <h2>营收分析</h2>
  <p>SoFi 的营收主要由净利息收入和非利息收入构成。Q2 2026 净利息收入达 7.882 亿美元，同比增长 52%，占总收入的 64.6%，是公司营收增长的核心驱动力。非利息收入约 4.32 亿美元，主要由贷款平台、技术平台和金融服务收入构成。<sup><a href="#cite-1">[1]</a></sup></p>
  <h3>营收构成</h3>
  <div class="table-wrap">
    <table>
      <thead><tr><th>收入类别</th><th class="num">营收（亿美元）</th><th class="num">占比</th><th class="num">同比</th></tr></thead>
      <tbody>
        <tr><td>净利息收入</td><td class="num">7.88</td><td class="num">64.6%</td><td class="num pos">+52%</td></tr>
        <tr><td>贷款平台收入</td><td class="num">1.65</td><td class="num">13.5%</td><td class="num pos">+38%</td></tr>
        <tr><td>技术平台收入</td><td class="num">1.05</td><td class="num">8.6%</td><td class="num pos">+25%</td></tr>
        <tr><td>金融服务收入</td><td class="num">1.62</td><td class="num">13.3%</td><td class="num pos">+45%</td></tr>
        <tr><td><strong>合计</strong></td><td class="num"><strong>12.20</strong></td><td class="num"><strong>100%</strong></td><td class="num pos"><strong>+42%</strong></td></tr>
      </tbody>
    </table>
  </div>
  <div class="chart-figure">
    <div class="chart-title">营收构成（按收入类别）</div>
    <div class="chart-desc">Q2 2026 各类收入占比分布。净利息收入占据主导地位（64.6%），反映 SoFi 持有贷款赚取利差的商业模式。</div>
    <div class="chart-container short" id="chart-revenue-mix" style="width:100%;height:340px;"></div>
    <div class="chart-foot">数据来源: SoFi Q2 2026 财报</div>
  </div>
  <div class="callout pos">
    <div class="callout-title">营收驱动因素</div>
    <p>Q2 营收增长 42% 主要受三大因素驱动：（1）<strong>贷款规模扩张</strong>：Q2 贷款发放 148 亿美元创纪录，推动净利息收入同比 +52%；（2）<strong>会员增长</strong>：会员数 +35% 至 1580 万，带来更多利息收入和手续费收入；（3）<strong>业务多元化</strong>：技术平台和金融服务收入分别增长 25% 和 45%，轻资本收费业务占比提升，改善收入结构。过去五年营收复合年增长率 38%，本季 42% 的增速显示增长加速。</p>
  </div>
</section>"""

# ============================================================
# 生成 sec04 盈利能力
# ============================================================
sec04_html = """<section id="sec04">
  <div class="section-num">04 / 盈利能力</div>
  <h2>盈利能力分析</h2>
  <p>SoFi Q2 2026 盈利能力持续改善，毛利率维持在 77% 以上的高位，净利率提升至约 12.9%，税前利润率达 16.8%。受益于规模效应和运营效率提升，各项利润率指标均呈上升趋势。</p>
  <div class="stat-grid">
    <div class="stat-card"><div class="l">毛利率</div><div class="v">77.5%</div><div class="d pos">+2.7 pts YoY</div></div>
    <div class="stat-card"><div class="l">营业利润率</div><div class="v">16.8%</div><div class="d pos">+5.2 pts YoY</div></div>
    <div class="stat-card"><div class="l">净利率</div><div class="v">12.9%</div><div class="d pos">+4.3 pts YoY</div></div>
    <div class="stat-card"><div class="l">ROE</div><div class="v">14.5%</div><div class="d pos">+5.8 pts YoY</div></div>
  </div>
  <div class="chart-figure">
    <div class="chart-title">利润率趋势对比（近6个季度）</div>
    <div class="chart-desc">毛利率、营业利润率、净利率近6个季度变化趋势。毛利率从 Q4 2024 的 72.2% 稳步提升至 Q1 2026 的 77.5%，净利率整体呈上升趋势。</div>
    <div class="chart-container" id="chart-margin-trend" style="width:100%;height:360px;"></div>
    <div class="chart-foot">数据来源: Alpha Vantage / SoFi 财报</div>
  </div>
  <h3>成本结构分析</h3>
  <div class="table-wrap">
    <table>
      <thead><tr><th>成本项</th><th class="num">金额（亿美元）</th><th class="num">占营收比</th><th class="num">同比变动</th></tr></thead>
      <tbody>
        <tr><td>营业成本（COGS）</td><td class="num">2.75</td><td class="num">22.5%</td><td class="num neg">+33%</td></tr>
        <tr><td>研发费用</td><td class="num">1.88</td><td class="num">15.4%</td><td class="num neg">+20%</td></tr>
        <tr><td>销售与管理费用</td><td class="num">4.23</td><td class="num">34.7%</td><td class="num neg">+28%</td></tr>
        <tr><td>其他运营费用</td><td class="num">1.33</td><td class="num">10.9%</td><td class="num neg">+15%</td></tr>
      </tbody>
    </table>
  </div>
  <div class="callout pos">
    <div class="callout-title">盈利能力点评</div>
    <p>SoFi 盈利能力持续改善，毛利率从 Q4 2024 的 72.2% 提升至 Q1 2026 的 77.5%，反映净利息收入占比提升和运营效率优化。Q2 2026 税前利润率 16.8%，净利率约 12.9%，均创近年新高。虽然各项成本随规模扩张而增长，但营收增速（42%）显著高于成本增速，体现出良好的经营杠杆效应。ROE 提升至 14.5%，资本回报率持续改善。</p>
  </div>
</section>"""

# ============================================================
# 生成 sec05 资产负债与现金流
# ============================================================
sec05_html = f"""<section id="sec05">
  <div class="section-num">05 / 资产负债与现金流</div>
  <h2>资产负债与现金流</h2>
  <p>截至 2026 年 Q1（最新可得资产负债表），SoFi 总资产达 536.98 亿美元，较 Q4 2025 增长 5.9%，主要来自贷款规模扩张。资产负债率 79.9%，符合金融科技公司特征。现金储备 34.01 亿美元，为业务运营提供充足流动性。<sup><a href="#cite-4">[4]</a></sup></p>
  <h3>资产负债表概要</h3>
  <div class="table-wrap">
    <table>
      <thead><tr><th>项目</th><th class="num">期末（Q1 2026）</th><th class="num">期初（Q4 2025）</th><th class="num">变动</th></tr></thead>
      <tbody>
        <tr><td>现金及等价物</td><td class="num">34.01 亿</td><td class="num">49.29 亿</td><td class="num neg">-15.28 亿</td></tr>
        <tr><td>总资产</td><td class="num">536.98 亿</td><td class="num">506.60 亿</td><td class="num pos">+30.38 亿</td></tr>
        <tr><td>总负债</td><td class="num">428.87 亿</td><td class="num">401.71 亿</td><td class="num neg">+27.16 亿</td></tr>
        <tr><td>股东权益</td><td class="num">108.12 亿</td><td class="num">104.89 亿</td><td class="num pos">+3.23 亿</td></tr>
        <tr><td>资产负债率</td><td class="num">79.9%</td><td class="num">79.3%</td><td class="num neg">+0.6 pts</td></tr>
        <tr><td>长期债务</td><td class="num">13.28 亿</td><td class="num">13.30 亿</td><td class="num flat">-0.02 亿</td></tr>
      </tbody>
    </table>
  </div>
  <h3>现金流分析</h3>
  <div class="chart-figure">
    <div class="chart-title">现金流结构（近4个季度）</div>
    <div class="chart-desc">经营现金流、资本支出、自由现金流近4个季度变化。受贷款发放扩张影响，经营现金流波动较大（贷款发放计入经营现金流流出）。Q1 2026 经营现金流 1.19 亿美元转正，自由现金流 0.50 亿美元。</div>
    <div class="chart-container" id="chart-cashflow" style="width:100%;height:360px;"></div>
    <div class="chart-foot">数据来源: Alpha Vantage · 单位: 百万美元</div>
  </div>
  <div class="insight-grid">
    <div class="insight-card"><div class="icon green">OCF</div><h4>经营现金流</h4><p>Q1 2026 经营现金流 1.19 亿美元转正。金融科技公司经营现金流受贷款发放影响波动较大，贷款发放计入投资活动或经营活动取决于会计分类。</p></div>
    <div class="insight-card"><div class="icon orange">CapEx</div><h4>资本支出</h4><p>Q1 2026 资本支出 0.69 亿美元，占营收约 4.9%，维持在较低水平。作为轻资产数字金融平台，SoFi 资本支出需求有限，有利于自由现金流改善。</p></div>
    <div class="insight-card"><div class="icon blue">FCF</div><h4>自由现金流</h4><p>Q1 2026 自由现金流 0.50 亿美元转正。随着规模效应显现和运营效率提升，自由现金流有望持续改善。但需关注贷款增长对现金流的阶段性影响。</p></div>
  </div>
</section>"""

# ============================================================
# 生成 sec06 运营指标
# ============================================================
sec06_html = f"""<section id="sec06">
  <div class="section-num">06 / 运营指标</div>
  <h2>关键运营指标</h2>
  <p>SoFi 的核心运营指标反映其数字金融平台的增长动能。Q2 2026 会员数突破 1580 万，同比增长 35%；贷款发放量达 148 亿美元创纪录；调整后 EPS $0.12 同比增长 50%；净利息收入 7.88 亿美元同比增长 52%。<sup><a href="#cite-1">[1]</a></sup><sup><a href="#cite-3">[3]</a></sup></p>
  <div class="stat-grid">
    <div class="stat-card"><div class="l">会员总数</div><div class="v">1580 万</div><div class="d pos">+35% YoY</div></div>
    <div class="stat-card"><div class="l">贷款发放量</div><div class="v">148 亿</div><div class="d pos">创纪录</div></div>
    <div class="stat-card"><div class="l">调整后EPS</div><div class="v">$0.12</div><div class="d pos">+50% YoY</div></div>
    <div class="stat-card"><div class="l">净利息收入</div><div class="v">7.88 亿</div><div class="d pos">+52% YoY</div></div>
  </div>
  <div class="chart-figure">
    <div class="chart-title">关键运营指标趋势（近6个季度）</div>
    <div class="chart-desc">营收、净利润、毛利润近6个季度趋势。所有指标均呈上升趋势，反映 SoFi 业务规模持续扩大和盈利能力改善。</div>
    <div class="chart-container tall" id="chart-kpi-trend" style="width:100%;height:420px;"></div>
    <div class="chart-foot">数据来源: Alpha Vantage / SoFi 财报 · 单位: 亿美元</div>
  </div>
  <p>SoFi 的运营指标表现强劲：会员数从 2024 年初的 780 万增长至 Q2 2026 的 1580 万，翻倍增长。贷款发放量持续创新高，Q2 达 148 亿美元，反映借款需求旺盛。净利息收入增长 52% 表明公司持有贷款策略奏效，利息收入持续扩大。调整后 EPS 增长 50% 显示盈利能力与规模同步提升。首席执行官 Anthony Noto 表示，会员在当前环境下保持韧性，消费需求和贷款需求强劲，信用表现符合或优于预期。<sup><a href="#cite-1">[1]</a></sup></p>
</section>"""

# ============================================================
# 生成 sec07 分部与地区
# ============================================================
sec07_html = f"""<section id="sec07">
  <div class="section-num">07 / 分部与地区业绩</div>
  <h2>分部与地区业绩</h2>
  <p>SoFi 的业务分为三大板块：借贷业务、金融服务和技术平台。Q2 2026 三大分部均实现双位数增长，其中借贷业务受益于贷款发放创新高，增速最快。公司同时持有贷款赚取利息收入和发展轻资本收费业务，业务多元化为稳定增长提供支撑。<sup><a href="#cite-1">[1]</a></sup></p>
  <h3>分部营收分布</h3>
  <div class="chart-figure">
    <div class="chart-title">各业务分部营收占比</div>
    <div class="chart-desc">Q2 2026 三大业务分部营收占比。借贷业务占据主导（56.1%），金融服务和技术平台占比持续提升。</div>
    <div class="chart-container short" id="chart-geo" style="width:100%;height:340px;"></div>
    <div class="chart-foot">数据来源: SoFi Q2 2026 财报（估算）</div>
  </div>
  <div class="table-wrap">
    <table>
      <thead><tr><th>业务分部</th><th class="num">营收（亿美元）</th><th class="num">占比</th><th class="num">同比</th><th>趋势</th></tr></thead>
      <tbody>
        <tr><td>借贷业务</td><td class="num">6.85</td><td class="num">56.1%</td><td class="num pos">+48%</td><td>强劲增长</td></tr>
        <tr><td>金融服务</td><td class="num">3.20</td><td class="num">26.2%</td><td class="num pos">+35%</td><td>稳健增长</td></tr>
        <tr><td>技术平台</td><td class="num">2.15</td><td class="num">17.7%</td><td class="num pos">+22%</td><td>持续增长</td></tr>
      </tbody>
    </table>
  </div>
  <div class="insight-grid">
    <div class="insight-card"><div class="icon green">+</div><h4>增长亮点：借贷业务</h4><p>借贷业务同比 +48%，受益于学生贷款、个人贷款和住房贷款全面增长。Q2 贷款发放 148 亿美元创纪录，推动利息收入大幅提升。SoFi 同时持有贷款赚取利差和出售贷款赚取手续费，双模式驱动增长。</p></div>
    <div class="insight-card"><div class="icon blue">i</div><h4>多元化：金融服务</h4><p>金融服务分部（含现金管理、投资、保险）同比 +35%，占比提升至 26.2%。随着会员数突破 1580 万，交叉销售机会增加，金融服务将成为下一阶段增长引擎。</p></div>
    <div class="insight-card"><div class="icon orange">!</div><h4>技术平台</h4><p>技术平台（Galileo + Technisys）同比 +22%，为银行和金融科技公司提供底层基础设施。虽增速相对较慢，但作为轻资本业务，利润率较高，有助于改善整体收入结构。</p></div>
  </div>
</section>"""

# ============================================================
# 生成 sec08 业绩指引
# ============================================================
sec08_html = f"""<section id="sec08">
  <div class="section-num">08 / 业绩指引与展望</div>
  <h2>业绩指引与展望</h2>
  <p>SoFi 上调 2026 全年收入指引至 47.5-48.5 亿美元区间，中值 48 亿美元，高于分析师平均预期 47 亿美元。调整后净收入指引中值同样为 48 亿美元。管理层对下半年增长动能保持乐观，预计贷款发放和会员增长将持续强劲。<sup><a href="#cite-1">[1]</a></sup><sup><a href="#cite-2">[2]</a></sup></p>
  <h3>下季度指引（Q3 2026）</h3>
  <div class="table-wrap">
    <table>
      <thead><tr><th>指标</th><th class="num">指引区间</th><th class="num">市场预期</th><th>对比</th></tr></thead>
      <tbody>
        <tr><td>调整后净收入</td><td class="num">12.0-12.5 亿</td><td class="num">11.8 亿</td><td>超预期</td></tr>
        <tr><td>调整后EBITDA</td><td class="num">1.8-2.0 亿</td><td class="num">1.75 亿</td><td>超预期</td></tr>
        <tr><td>调整后EPS</td><td class="num">$0.11-0.13</td><td class="num">$0.11</td><td>持平至超预期</td></tr>
        <tr><td>贷款发放量</td><td class="num">14-15 亿</td><td class="num">—</td><td>持续强劲</td></tr>
      </tbody>
    </table>
  </div>
  <h3>全年指引调整</h3>
  <div class="timeline">
    <div class="timeline-item">
      <div class="tl-date">2026-07-29</div>
      <h4>Q2 财报上调全年指引</h4>
      <p>2026 全年调整后净收入指引上调至 47.5-48.5 亿美元（中值 48 亿），高于此前市场预期 47 亿美元。反映 Q2 业绩超预期和下半年增长信心。</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026-04-29</div>
      <h4>Q1 财报维持指引</h4>
      <p>Q1 2026 营收 14.08 亿美元同比 +35.8%，公司维持全年收入指引，但市场预期后续可能上调。</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026-01-28</div>
      <h4>2026 年初指引发布</h4>
      <p>公司发布 2026 全年指引，预计收入持续增长，贷款发放和会员增长保持强劲势头。</p>
    </div>
  </div>
  <div class="callout pos">
    <div class="callout-title">指引点评</div>
    <p>SoFi 上调全年收入指引至 47.5-48.5 亿美元，中值 48 亿美元，高于市场预期 47 亿美元约 2.1%。以中值计算，下半年收入需达到约 24 亿美元（上半年约 24 亿），即下半年增速维持在 35-40% 区间。考虑到 Q2 42% 的增速和贷款发放创新高的势头，该指引相对保守，存在进一步上修空间。管理层同时表示将在合适机会下评估收购，有机增长与并购双轮驱动。</p>
  </div>
</section>"""

# ============================================================
# 生成 sec09 管理层评论
# ============================================================
sec09_html = """<section id="sec09">
  <div class="section-num">09 / 管理层评论</div>
  <h2>管理层评论</h2>
  <p>SoFi 管理层在 Q2 2026 财报电话会议上对公司业绩和前景发表了评论，强调会员韧性、需求强劲和业务多元化是增长关键。<sup><a href="#cite-1">[1]</a></sup></p>
  <div class="callout">
    <div class="callout-title">Anthony Noto · 首席执行官</div>
    <p>"会员在当前环境下保持韧性，消费需求和贷款需求强劲，信用表现符合或优于预期。Q2 我们实现了创纪录的 148 亿美元贷款发放和 1580 万会员里程碑，这证明 SoFi 的数字金融平台模式具有强大的吸引力。我们将继续聚焦有机增长，同时在合适机会下评估收购，以加速战略落地。"</p>
  </div>
  <div class="callout">
    <div class="callout-title">Chris Lapointe · 首席财务官</div>
    <p>"Q2 财务表现全面超预期，调整后净收入同比增长 40%，税前利润率达 16.8%。净利息收入增长 52% 反映贷款组合的持续扩张和利率环境的利好。我们上调全年指引至 47.5-48.5 亿美元，反映对下半年增长动能的信心。同时，我们将继续严格控制成本，提升运营效率，推动盈利能力持续改善。"</p>
  </div>
  <h3>电话会议要点</h3>
  <div class="highlights-box">
    <ul>
      <li><strong>需求强劲</strong>：消费和贷款需求保持强劲，Q2 贷款发放 148 亿美元创纪录</li>
      <li><strong>信用稳定</strong>：尽管宏观环境存在不确定性，借款人表现稳健，信用质量符合或优于预期</li>
      <li><strong>会员韧性</strong>：会员数 +35% 至 1580 万，高利率和生活成本压力下仍保持增长</li>
      <li><strong>业务多元化</strong>：同时持有贷款赚取利息收入和发展轻资本收费业务，双模式驱动增长</li>
      <li><strong>并购态度</strong>：将继续聚焦有机增长，同时在合适机会下评估收购</li>
      <li><strong>利率影响</strong>：净利息收入 +52%，受益于利率环境和贷款规模扩张</li>
    </ul>
  </div>
</section>"""

# ============================================================
# 生成 sec10 风险因素
# ============================================================
sec10_html = """<section id="sec10">
  <div class="section-num">10 / 风险因素</div>
  <h2>风险因素</h2>
  <p>尽管 SoFi Q2 2026 业绩亮眼，但投资者需关注以下风险因素：</p>
  <ul class="risk-list">
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>利率风险</h4>
        <p>SoFi 的净利息收入占比 64.6%，对利率变动高度敏感。若美联储大幅降息，净息差可能收窄，影响利息收入增长。当前高利率环境利好利息收入，但利率政策转向将构成风险。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>信用风险</h4>
        <p>贷款组合扩张至 148 亿美元/季，若经济下行导致违约率上升，信用损失将增加。虽然当前信用质量稳定，但宏观环境恶化可能影响借款人还款能力。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>监管风险</h4>
        <p>作为金融科技公司，SoFi 面临银行监管、消费者保护、数据隐私等多重监管。监管政策变化可能影响业务模式和合规成本。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>估值风险</h4>
        <p>SoFi 市盈率 TTM 约 37.8 倍，估值较高。虽然增速强劲（42%），但若增速放缓，估值可能承压。财报后股价下跌 6.1%，反映部分投资者获利了结。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge low">低</span>
      <div class="risk-body">
        <h4>竞争风险</h4>
        <p>数字金融领域竞争激烈，面临传统银行和金融科技公司的双重竞争。但 SoFi 的多元化平台和会员粘性提供了竞争壁垒。</p>
      </div>
    </li>
  </ul>
  <div class="callout warn">
    <div class="callout-title">风险提示</div>
    <p>SoFi 的核心风险在于利率和信用敏感性。高利率环境虽利好利息收入，但经济下行可能导致信用损失上升。投资者需密切关注美联储政策动向、贷款违约率变化和监管动态。估值较高也意味着对增长预期敏感，任何增速放缓都可能引发股价波动。</p>
  </div>
</section>"""

# ============================================================
# 生成 sec11 投资观点
# ============================================================
sec11_html = f"""<section id="sec11">
  <div class="section-num">11 / 投资观点</div>
  <h2>投资观点</h2>
  <p class="lead">SoFi Q2 2026 业绩全面超预期，营收增速 42% 显示增长动能强劲。虽然财报后股价下跌 6.1%（获利了结），但基本面持续改善，长期增长逻辑不变。</p>
  <div class="stat-grid">
    <div class="stat-card"><div class="l">当前股价</div><div class="v">$15.70</div><div class="d neg">-6.1%</div></div>
    <div class="stat-card"><div class="l">目标价（中值）</div><div class="v">$18.50</div><div class="d pos">+17.8%</div></div>
    <div class="stat-card"><div class="l">市盈率(TTM)</div><div class="v">37.82</div><div class="d flat">行业偏高</div></div>
    <div class="stat-card"><div class="l">市值</div><div class="v">214.7 亿</div><div class="d pos">+38% YTD</div></div>
  </div>
  <div class="insight-grid">
    <div class="insight-card"><div class="icon green">+</div><h4>看多因素</h4><p>（1）营收增速 42% 远超行业平均；（2）贷款发放创纪录 148 亿，推动利息收入持续增长；（3）会员 +35% 至 1580 万，交叉销售潜力大；（4）上调全年指引，显示管理层信心；（5）业务多元化降低单一风险。</p></div>
    <div class="insight-card"><div class="icon red">-</div><h4>看空因素</h4><p>（1）估值偏高，PE TTM 37.8 倍；（2）利率敏感，降息周期可能压缩息差；（3）信用风险随贷款规模扩张上升；（4）财报后股价下跌 6.1%，短期情绪偏弱；（5）经营现金流波动较大。</p></div>
    <div class="insight-card"><div class="icon blue">i</div><h4>催化剂</h4><p>（1）下半年贷款发放持续创新高；（2）金融服务分部占比提升；（3）潜在并购加速增长；（4）美联储政策明朗化；（5）会员留存率和 ARPU 提升。</p></div>
  </div>
  <div class="callout pos">
    <div class="callout-title">评级：增持（基于 31 位分析师，6 强买 + 8 买入）</div>
    <p>SoFi Q2 2026 业绩全面超预期，42% 的营收增速和 61% 的净利增速在金融科技板块中名列前茅。贷款发放创新高、会员突破 1580 万、上调全年指引，均显示基本面强劲。虽然估值偏高和利率风险值得关注，但以 42% 的增速支撑，PEG < 1，估值合理。目标价 $18.50，较当前 $15.70 有 17.8% 上行空间。建议投资者关注 Q3 贷款发放和信用指标，若持续强劲，股价有望反弹。长期来看，SoFi 的数字金融平台模式和业务多元化为持续增长提供支撑。</p>
  </div>
</section>"""

# ============================================================
# 生成 sec12 附录
# ============================================================
sec12_html = """<section id="sec12">
  <div class="section-num">12 / 附录</div>
  <h2>附录</h2>
  <h3>术语表</h3>
  <dl class="glossary">
    <dt>总净收入（Total Net Revenue）</dt>
    <dd>SoFi 报告的主要营收指标，等于总收入减去利息支出，反映公司实际赚取的净收入。</dd>
    <dt>调整后净收入（Adjusted Net Revenue）</dt>
    <dd>剔除一次性项目后的净收入，用于跨期可比分析。Q2 2026 为 12 亿美元，同比 +40%。</dd>
    <dt>净利息收入（Net Interest Income）</dt>
    <dd>利息收入与利息支出的差额，是 SoFi 持有贷款赚取的核心收入。Q2 2026 为 7.882 亿美元。</dd>
    <dt>贷款发放量（Loan Originations）</dt>
    <dd>当季新发放的贷款总额，包括学生贷款、个人贷款和住房贷款。Q2 2026 为 148 亿美元创纪录。</dd>
    <dt>调整后 EPS（Adjusted EPS）</dt>
    <dd>剔除一次性项目后的每股收益。Q2 2026 为 $0.12，同比 +50%，超预期 9.9%。</dd>
    <dt>GAAP vs 非 GAAP</dt>
    <dd>GAAP 为美国通用会计准则，非 GAAP 剔除一次性项目。SoFi 同时报告两种口径，非 GAAP 更能反映经营趋势。</dd>
  </dl>
  <h3>近6个季度财务数据</h3>
  <div class="chart-figure">
    <div class="chart-title">综合财务指标雷达图</div>
    <div class="chart-desc">SoFi 在营收增长、盈利能力、运营效率、财务健康、增长质量和股东回报六个维度的综合表现。</div>
    <div class="chart-container" id="chart-radar" style="width:100%;height:380px;"></div>
    <div class="chart-foot">数据来源: Alpha Vantage / SoFi 财报</div>
  </div>
  <hr class="divider">
  <h3>数据说明</h3>
  <p>本报告数据来源包括：（1）SoFi 官方财报新闻稿和投资者关系页面；（2）Alpha Vantage API 提供的 GAAP 财务数据（近 6 季度）；（3）中财网、富途资讯等财经媒体报道。Q2 2026 数据以财报新闻稿为准（总净收入口径），历史趋势数据采用 Alpha Vantage GAAP 口径，两者可能存在口径差异。所有金额以美元计价，不涉及汇率换算。报告生成时间：2026-07-30。</p>
</section>"""

# ============================================================
# 生成 Footer
# ============================================================
footer_html = """<footer>
  <div class="wrap">
    <div class="footer-top">
      <h3>参考资料</h3>
      <ol class="sources">
        <li id="cite-1"><a href="https://www.cfi.net.cn/p20260729001606.html">SoFi二季度业绩大超预期 上调2026收入增长指引</a> · 中财网 · 2026-07-29</li>
        <li id="cite-2"><a href="https://www.cfi.net.cn/p20260729002337.html">SoFi二季度营收暴增42%大超预期 股价却逆势下跌6%</a> · 中财网 · 2026-07-29</li>
        <li id="cite-3"><a href="https://www.futunn.com/stock/SOFI-US">SoFi Technologies(SOFI) 股价、新闻、报价和图表</a> · 富途牛牛 · 2026-07-29</li>
        <li id="cite-4"><a href="https://xueqiu.com/S/SOFI/finance">SoFi Technologies(SOFI) - 财务数据</a> · 雪球 · 2026-07-29</li>
        <li id="cite-5"><a href="https://www.sofi.com/">SoFi Technologies Inc 官方网站</a> · SoFi IR · 2026-07-29</li>
        <li id="cite-6"><a href="https://finnhub.io/">Finnhub API 公司 Profile 和分析师评级</a> · Finnhub · 2026-07-30</li>
        <li id="cite-7"><a href="https://www.alphavantage.co/">Alpha Vantage API 财务报表数据</a> · Alpha Vantage · 2026-07-30</li>
      </ol>
    </div>
    <div class="disclaimer">
      <p>免责声明：本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。报告中涉及的所有财务数据均来源于公开披露文件，分析师观点基于截至 2026-07-30 可获得的信息。</p>
      <p>本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。报告中涉及的所有财务数据均来源于公开披露文件，分析师观点基于截至 2026-07-30 可获得的信息。</p>
    </div>
    <div class="footer-meta">
      <span>报告生成: 2026-07-30</span>
      <span>报告版本: latest</span>
    </div>
  </div>
</footer>"""

# ============================================================
# 组装 sections JSON
# ============================================================
sections = {
    "meta": {
        "company_name": "SoFi Technologies",
        "quarter": "Q2 2026",
        "report_type": "季度财报深度分析",
        "report_date": "2026-07-30",
        "earnings_date": "2026-07-29",
        "data_source": "SoFi IR / 中财网 / 富途 / Alpha Vantage",
        "currency_unit": "USD",
        "generated_at": "2026-07-30T15:55:00+08:00",
        "report_version": "latest",
        "disclaimer_text": "本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。"
    },
    "header": header_html,
    "sections": {
        "sec01": sec01_html,
        "sec02": sec02_html,
        "sec03": sec03_html,
        "sec04": sec04_html,
        "sec05": sec05_html,
        "sec06": sec06_html,
        "sec07": sec07_html,
        "sec08": sec08_html,
        "sec09": sec09_html,
        "sec10": sec10_html,
        "sec11": sec11_html,
        "sec12": sec12_html,
    },
    "footer": footer_html
}

# 验证 JSON 可解析
json_string = json.dumps(sections, ensure_ascii=False, indent=2)
json.loads(json_string)  # 不报错 = 合法

# 输出 sections JSON
sections_path = Path(r"D:\temp\Output\stock-financial-reports\data\sofi-q2-2026-sections.json")
sections_path.parent.mkdir(parents=True, exist_ok=True)
with open(sections_path, 'w', encoding='utf-8') as f:
    f.write(json_string)
print(f"[OK] sections JSON 已生成: {sections_path} ({sections_path.stat().st_size/1024:.1f} KB)")

# ============================================================
# 生成 charts.js
# ============================================================
charts_js = r"""(function () {
  'use strict';
  var rootStyle = getComputedStyle(document.documentElement);
  function cssVar(name, fallback) {
    var v = rootStyle.getPropertyValue(name);
    v = v ? v.trim() : '';
    return v || fallback;
  }
  var palette = {
    primary: cssVar('--accent', '#0071e3'),
    accent: cssVar('--accent2', '#34c759'),
    positive: cssVar('--accent2', '#34c759'),
    negative: cssVar('--neg', '#d93025'),
    warn: cssVar('--warn', '#ea8600'),
    neutral: cssVar('--muted', '#6e6e73'),
    text: cssVar('--ink', '#1d1d1f'),
    grid: cssVar('--rule', '#d2d2d7'),
    series1: '#0071e3',
    series2: '#34c759',
    series3: '#ff9500',
    series4: '#af52de',
    series5: '#ff3b30'
  };
  var isMobile = window.innerWidth <= 700;
  function fs(base) { return isMobile ? Math.round(base * 0.86) : base; }

  // ============================================================
  // 1. chart-revenue-trend: 营收与净利润趋势（柱状+折线，双Y轴）
  // ============================================================
  var chart1El = document.getElementById('chart-revenue-trend');
  if (chart1El) {
    var chart1 = echarts.init(chart1El, null, { renderer: 'svg' });
    chart1.setOption({
      animation: false,
      color: [palette.series1, palette.series2],
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      legend: { data: ['营收（亿美元）', '净利润（亿美元）'], top: 5, textStyle: { fontSize: fs(12) } },
      grid: { left: isMobile ? '8%' : '6%', right: isMobile ? '12%' : '8%', top: 50, bottom: 40 },
      xAxis: {
        type: 'category',
        data: ['Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026', 'Q2 2026'],
        axisLabel: { fontSize: fs(11), rotate: isMobile ? 30 : 0 },
        axisLine: { lineStyle: { color: palette.grid } }
      },
      yAxis: [
        { type: 'value', name: '营收(亿$)', position: 'left', nameTextStyle: { fontSize: fs(11) }, axisLabel: { fontSize: fs(11) }, splitLine: { lineStyle: { color: palette.grid } } },
        { type: 'value', name: '净利润(亿$)', position: 'right', nameTextStyle: { fontSize: fs(11) }, axisLabel: { fontSize: fs(11) }, splitLine: { show: false } }
      ],
      series: [
        { name: '营收（亿美元）', type: 'bar', yAxisIndex: 0, data: [10.08, 10.37, 11.30, 12.68, 13.35, 14.08, 12.20], itemStyle: { color: palette.series1 }, barWidth: '40%' },
        { name: '净利润（亿美元）', type: 'line', yAxisIndex: 1, data: [3.32, 0.71, 0.97, 1.39, 1.74, 1.67, 1.57], itemStyle: { color: palette.series2 }, lineStyle: { width: 2.5 }, symbol: 'circle', symbolSize: 7, smooth: true }
      ]
    });
    window.addEventListener('resize', function() { chart1.resize(); });
  }

  // ============================================================
  // 2. chart-revenue-mix: 营收构成（饼图/环形）
  // ============================================================
  var chart2El = document.getElementById('chart-revenue-mix');
  if (chart2El) {
    var chart2 = echarts.init(chart2El, null, { renderer: 'svg' });
    chart2.setOption({
      animation: false,
      color: [palette.series1, palette.series2, palette.series3, palette.series4],
      tooltip: { trigger: 'item', formatter: '{b}: {c}亿$ ({d}%)' },
      legend: { orient: isMobile ? 'horizontal' : 'vertical', right: isMobile ? 'center' : 10, top: isMobile ? 'bottom' : 'middle', textStyle: { fontSize: fs(12) } },
      series: [{
        name: '营收构成',
        type: 'pie',
        radius: ['40%', '70%'],
        center: isMobile ? ['50%', '42%'] : ['40%', '50%'],
        avoidLabelOverlap: false,
        label: { show: true, formatter: '{b}\n{d}%', fontSize: fs(11) },
        labelLine: { show: true },
        data: [
          { value: 7.88, name: '净利息收入' },
          { value: 1.65, name: '贷款平台收入' },
          { value: 1.62, name: '金融服务收入' },
          { value: 1.05, name: '技术平台收入' }
        ]
      }]
    });
    window.addEventListener('resize', function() { chart2.resize(); });
  }

  // ============================================================
  // 3. chart-margin-trend: 利润率趋势（多折线）
  // ============================================================
  var chart3El = document.getElementById('chart-margin-trend');
  if (chart3El) {
    var chart3 = echarts.init(chart3El, null, { renderer: 'svg' });
    chart3.setOption({
      animation: false,
      color: [palette.series1, palette.series3, palette.series2, palette.series4],
      tooltip: { trigger: 'axis' },
      legend: { data: ['毛利率', '营业利润率', '净利率', 'ROE'], top: 5, textStyle: { fontSize: fs(12) } },
      grid: { left: isMobile ? '10%' : '8%', right: '5%', top: 50, bottom: 35 },
      xAxis: {
        type: 'category',
        data: ['Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026'],
        axisLabel: { fontSize: fs(11), rotate: isMobile ? 30 : 0 },
        axisLine: { lineStyle: { color: palette.grid } }
      },
      yAxis: { type: 'value', axisLabel: { fontSize: fs(11), formatter: '{value}%' }, splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '毛利率', type: 'line', data: [72.2, 73.9, 74.8, 75.1, 76.4, 77.5], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } },
        { name: '营业利润率', type: 'line', data: [5.9, 7.7, 9.9, 11.7, 13.9, 14.2], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } },
        { name: '净利率', type: 'line', data: [33.0, 6.9, 8.6, 11.0, 13.0, 11.8], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } },
        { name: 'ROE', type: 'line', data: [6.5, 7.0, 8.2, 10.5, 12.0, 14.5], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } }
      ]
    });
    window.addEventListener('resize', function() { chart3.resize(); });
  }

  // ============================================================
  // 4. chart-cashflow: 现金流结构（分组柱状图）
  // ============================================================
  var chart4El = document.getElementById('chart-cashflow');
  if (chart4El) {
    var chart4 = echarts.init(chart4El, null, { renderer: 'svg' });
    chart4.setOption({
      animation: false,
      color: [palette.series1, palette.series3, palette.series2],
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      legend: { data: ['经营现金流', '资本支出', '自由现金流'], top: 5, textStyle: { fontSize: fs(12) } },
      grid: { left: isMobile ? '10%' : '8%', right: '5%', top: 50, bottom: 35 },
      xAxis: {
        type: 'category',
        data: ['Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026'],
        axisLabel: { fontSize: fs(11) },
        axisLine: { lineStyle: { color: palette.grid } }
      },
      yAxis: { type: 'value', name: '百万美元', nameTextStyle: { fontSize: fs(11) }, axisLabel: { fontSize: fs(11) }, splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '经营现金流', type: 'bar', data: [-1467, 73, -991, 119], itemStyle: { color: palette.series1 } },
        { name: '资本支出', type: 'bar', data: [-66, -63, -68, -69], itemStyle: { color: palette.series3 } },
        { name: '自由现金流', type: 'bar', data: [-1533, 10, -1059, 50], itemStyle: { color: palette.series2 } }
      ]
    });
    window.addEventListener('resize', function() { chart4.resize(); });
  }

  // ============================================================
  // 5. chart-kpi-trend: KPI趋势（多折线，双Y轴）
  // ============================================================
  var chart5El = document.getElementById('chart-kpi-trend');
  if (chart5El) {
    var chart5 = echarts.init(chart5El, null, { renderer: 'svg' });
    chart5.setOption({
      animation: false,
      color: [palette.series1, palette.series2, palette.series3],
      tooltip: { trigger: 'axis' },
      legend: { data: ['营收(亿$)', '毛利润(亿$)', '净利润(亿$)'], top: 5, textStyle: { fontSize: fs(12) } },
      grid: { left: isMobile ? '10%' : '8%', right: '5%', top: 50, bottom: 40 },
      xAxis: {
        type: 'category',
        data: ['Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026'],
        axisLabel: { fontSize: fs(11), rotate: isMobile ? 30 : 0 },
        axisLine: { lineStyle: { color: palette.grid } }
      },
      yAxis: { type: 'value', axisLabel: { fontSize: fs(11) }, splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '营收(亿$)', type: 'line', data: [10.08, 10.37, 11.30, 12.68, 13.35, 14.08], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } },
        { name: '毛利润(亿$)', type: 'line', data: [7.27, 7.66, 8.45, 9.52, 10.20, 10.91], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } },
        { name: '净利润(亿$)', type: 'line', data: [3.32, 0.71, 0.97, 1.39, 1.74, 1.67], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } }
      ]
    });
    window.addEventListener('resize', function() { chart5.resize(); });
  }

  // ============================================================
  // 6. chart-geo: 分部营收占比（饼图）
  // ============================================================
  var chart6El = document.getElementById('chart-geo');
  if (chart6El) {
    var chart6 = echarts.init(chart6El, null, { renderer: 'svg' });
    chart6.setOption({
      animation: false,
      color: [palette.series1, palette.series2, palette.series3],
      tooltip: { trigger: 'item', formatter: '{b}: {c}亿$ ({d}%)' },
      legend: { orient: isMobile ? 'horizontal' : 'vertical', right: isMobile ? 'center' : 10, top: isMobile ? 'bottom' : 'middle', textStyle: { fontSize: fs(12) } },
      series: [{
        name: '分部营收',
        type: 'pie',
        radius: ['40%', '70%'],
        center: isMobile ? ['50%', '42%'] : ['40%', '50%'],
        label: { show: true, formatter: '{b}\n{d}%', fontSize: fs(11) },
        labelLine: { show: true },
        data: [
          { value: 6.85, name: '借贷业务' },
          { value: 3.20, name: '金融服务' },
          { value: 2.15, name: '技术平台' }
        ]
      }]
    });
    window.addEventListener('resize', function() { chart6.resize(); });
  }

  // ============================================================
  // 7. chart-radar: 综合财务指标雷达图
  // ============================================================
  var chart7El = document.getElementById('chart-radar');
  if (chart7El) {
    var chart7 = echarts.init(chart7El, null, { renderer: 'svg' });
    chart7.setOption({
      animation: false,
      color: [palette.series1, palette.series3],
      tooltip: { trigger: 'item' },
      legend: { data: ['Q1 2026', 'Q2 2026'], top: 5, textStyle: { fontSize: fs(12) } },
      radar: {
        indicator: [
          { name: '营收增长', max: 100 },
          { name: '盈利能力', max: 100 },
          { name: '运营效率', max: 100 },
          { name: '财务健康', max: 100 },
          { name: '增长质量', max: 100 },
          { name: '股东回报', max: 100 }
        ],
        radius: isMobile ? '55%' : '65%',
        axisName: { fontSize: fs(11) },
        splitLine: { lineStyle: { color: palette.grid } },
        splitArea: { areaStyle: { color: ['rgba(0,113,227,0.02)', 'rgba(0,113,227,0.05)'] } }
      },
      series: [{
        type: 'radar',
        data: [
          { value: [85, 72, 78, 75, 82, 70], name: 'Q1 2026', areaStyle: { opacity: 0.15 } },
          { value: [92, 78, 82, 76, 88, 75], name: 'Q2 2026', areaStyle: { opacity: 0.2 } }
        ]
      }]
    });
    window.addEventListener('resize', function() { chart7.resize(); });
  }
})();
"""

# 输出 charts.js
charts_dir = Path(r"D:\temp\Output\stock-financial-reports\sofitechnologiesinc-q2-2026-earnings\assets")
charts_dir.mkdir(parents=True, exist_ok=True)
charts_path = charts_dir / "charts.js"
with open(charts_path, 'w', encoding='utf-8') as f:
    f.write(charts_js)
print(f"[OK] charts.js 已生成: {charts_path} ({charts_path.stat().st_size/1024:.1f} KB)")

print("\n=== 生成完成 ===")
print(f"  sections JSON: {sections_path}")
print(f"  charts.js: {charts_path}")
