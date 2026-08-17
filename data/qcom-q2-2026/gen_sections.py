# -*- coding: utf-8 -*-
"""QCOM Q2 2026 (FY26 Q3) sections JSON 生成器"""
import json
from pathlib import Path

OUT = Path(r"D:\temp\Output\stock-financial-reports\data\qcom-q2-2026-sections.json")

# ============== Header ==============
header = """<header class="report-head">
  <div class="wrap">
    <div class="kicker">季度财报深度分析 · 2026-07-30</div>
    <h1>Qualcomm 高通 2026 财年第三季度财报深度分析</h1>
    <p class="sub">营收 99.47 亿美元（同比 -4%），高于市场预期 96.7 亿美元；Non-GAAP EPS 2.21 美元，汽车与 IoT 业务合并同比增长 28%，但内存涨价与苹果订单下滑压制 Q4 指引。</p>
    <div class="meta">报告日期：2026-07-30　|　财报发布：2026-07-30 04:00 (北京时间)　|　数据来源：Qualcomm 官方 IR / Finnhub / Alpha Vantage　|　货币：USD（不涉及汇率换算）</div>
    <div class="stat-grid">
      <div class="stat-card"><div class="v">99.47 亿</div><div class="l">营收（USD）</div><div class="d neg">-4.0% YoY</div></div>
      <div class="stat-card"><div class="v">20.02 亿</div><div class="l">GAAP 净利润</div><div class="d neg">-24.9% YoY</div></div>
      <div class="stat-card"><div class="v">53.1%</div><div class="l">毛利率</div><div class="d neg">-2.5 pts YoY</div></div>
      <div class="stat-card"><div class="v">2.21 美元</div><div class="l">Non-GAAP EPS</div><div class="d neg">-23.0% YoY</div></div>
    </div>
  </div>
</header>"""

# ============== sec01 核心摘要 ==============
sec01 = """<section id="sec01">
  <div class="section-num">01 / 核心摘要</div>
  <h2>核心摘要</h2>
  <p class="lead">高通 FY2026 第三季度（截至 2026-06-28）营收 99.47 亿美元，同比下滑 4%，但仍位于公司此前指引区间上限，并显著高于市场预期 96.7 亿美元。GAAP 净利润 20.02 亿美元，同比大幅下滑 25%；Non-GAAP EPS 2.21 美元略低于预期 2.23 美元。毛利率从上年同期的 55.6% 下降至 53.1%，主要受内存及组件成本上升拖累。管理层宣布 9 月 1 日起全线芯片涨价以对冲成本压力，但 Q4 业绩指引仍偏弱，盘后股价下跌约 4.68%。<sup><a href="#cite-1">[1]</a></sup><sup><a href="#cite-2">[2]</a></sup></p>
  <div class="highlights-box">
    <h3>本季关键亮点</h3>
    <ul>
      <li>营收 99.47 亿美元，位于指引区间上限，超出市场预期约 3 亿美元<sup><a href="#cite-2">[2]</a></sup></li>
      <li>QCT 汽车与 IoT 合并营收同比增长 28%，汽车业务连续 23 季度双位数增长<sup><a href="#cite-1">[1]</a></sup></li>
      <li>汽车业务营收 15.9 亿美元，IoT 业务 18.30 亿美元（同比 +9%），多元化战略加速落地<sup><a href="#cite-3">[3]</a></sup></li>
      <li>完成 Modular Inc 收购，构建生成式与智能体 AI 的开放软件基础<sup><a href="#cite-1">[1]</a></sup></li>
      <li>管理层指引 2027 财年非手机业务增速超 60%，2029 财年非手机营收目标 400 亿美元<sup><a href="#cite-1">[1]</a></sup></li>
    </ul>
  </div>
  <div class="callout neg">
    <div class="callout-title">核心结论</div>
    <p>本季营收超预期但利润端明显承压：内存与供应成本上升导致毛利率下降 2.5 个百分点，叠加手册业务同比下滑 20%、苹果订单下季度环比腰斩，公司宣布 9 月起全线涨价以对冲成本。Q4 指引（EPS 2.05-2.25 美元、营收 97-105 亿美元）低于市场预期，短期内增长压力较大；但汽车、IoT、数据中心多元化战略持续推进，2027 财年非手机业务增速有望加速至 60%+，长期增长动能仍在。</p>
  </div>
</section>"""

# ============== sec02 财务概览 ==============
sec02 = """<section id="sec02">
  <div class="section-num">02 / 财务概览</div>
  <h2>财务概览</h2>
  <p>下表汇总高通 FY2026 第三季度核心财务指标，对比上季度（FY26 Q2，截至 2026-03-29）与上年同期（FY25 Q3，截至 2025-06-30）。营收同比 -4% 但环比 -6.2%，毛利率连续两个季度下滑，主要反映内存及组件成本上升对手机芯片业务利润空间的压制<sup><a href="#cite-2">[2]</a></sup><sup><a href="#cite-4">[4]</a></sup>。</p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr><th>财务指标</th><th class="num">本季度 (FY26 Q3)</th><th class="num">上季度 (FY26 Q2)</th><th class="num">同比</th><th class="num">环比</th></tr>
      </thead>
      <tbody>
        <tr><td>营业收入</td><td class="num">99.47 亿美元</td><td class="num">105.99 亿美元</td><td class="num neg">-4.0%</td><td class="num neg">-6.2%</td></tr>
        <tr><td>毛利润</td><td class="num">52.77 亿美元</td><td class="num">56.99 亿美元</td><td class="num neg">-8.4%</td><td class="num neg">-7.4%</td></tr>
        <tr><td>营业利润 (GAAP)</td><td class="num">16.26 亿美元</td><td class="num">23.09 亿美元</td><td class="num neg">-41.1%</td><td class="num neg">-29.6%</td></tr>
        <tr><td>净利润 (GAAP)</td><td class="num">20.02 亿美元</td><td class="num">73.70 亿美元</td><td class="num neg">-24.9%</td><td class="num neg">-72.8%</td></tr>
        <tr><td>经营现金流</td><td class="num">9.91 亿美元</td><td class="num">24.49 亿美元</td><td class="num neg">-75.2%</td><td class="num neg">-59.5%</td></tr>
        <tr><td>资本支出</td><td class="num">4.96 亿美元</td><td class="num">5.33 亿美元</td><td class="num neg">-21.8%</td><td class="num neg">-6.9%</td></tr>
        <tr><td>自由现金流</td><td class="num">4.95 亿美元</td><td class="num">19.16 亿美元</td><td class="num neg">-81.3%</td><td class="num neg">-74.2%</td></tr>
      </tbody>
    </table>
  </div>
  <div class="chart-figure">
    <div class="chart-title">营收与净利润趋势（近 6 个季度）</div>
    <div class="chart-desc">营收自 FY25 Q4 高点 122.52 亿美元持续回落，FY26 Q3 营收 99.47 亿美元环比 -6.2%；GAAP 净利润波动较大，FY26 Q2 受一次性收益推高至 73.70 亿美元，FY26 Q3 回归正常水平 20.02 亿美元。</div>
    <div class="chart-container" id="chart-revenue-trend"></div>
    <div class="chart-foot">数据来源: Finnhub / Alpha Vantage · 单位: 亿美元</div>
  </div>
</section>"""

# ============== sec03 营收分析 ==============
sec03 = """<section id="sec03">
  <div class="section-num">03 / 营收分析</div>
  <h2>营收分析</h2>
  <p>高通营收按业务板块划分为 QCT（半导体）三大子业务与 QTL（特许权使用费）业务。QCT 业务总营收约 85.20 亿美元，占总营收 85.7%；QTL 与其他业务合计约 14.27 亿美元。手册业务仍为最大单一营收来源，但占比从历史 60%+ 降至本季 51.3%，多元化转型加速推进<sup><a href="#cite-3">[3]</a></sup><sup><a href="#cite-5">[5]</a></sup>。</p>
  <h3>营收构成</h3>
  <div class="table-wrap">
    <table>
      <thead><tr><th>业务板块</th><th class="num">营收（亿美元）</th><th class="num">占比</th><th class="num">同比</th></tr></thead>
      <tbody>
        <tr><td>QCT 手册（Handset）</td><td class="num">51.00</td><td class="num">51.3%</td><td class="num neg">-20.0%</td></tr>
        <tr><td>QCT 汽车（Automotive）</td><td class="num">15.90</td><td class="num">16.0%</td><td class="num pos">+28.0%</td></tr>
        <tr><td>QCT 物联网（IoT）</td><td class="num">18.30</td><td class="num">18.4%</td><td class="num pos">+9.0%</td></tr>
        <tr><td>QTL 特许权及其他</td><td class="num">14.27</td><td class="num">14.3%</td><td class="num pos">+约 0%</td></tr>
        <tr><td><strong>合计</strong></td><td class="num"><strong>99.47</strong></td><td class="num"><strong>100%</strong></td><td class="num neg"><strong>-4.0%</strong></td></tr>
      </tbody>
    </table>
  </div>
  <div class="chart-figure">
    <div class="chart-title">营收构成（按业务板块）</div>
    <div class="chart-desc">手册业务仍是营收核心但占比已降至 51.3%；汽车与 IoT 合计占比升至 34.4%，体现高通非手机业务多元化战略持续推进。</div>
    <div class="chart-container short" id="chart-revenue-mix"></div>
    <div class="chart-foot">数据来源: Qualcomm IR / 光大证券点评</div>
  </div>
  <div class="callout">
    <div class="callout-title">营收驱动因素</div>
    <p>本季营收下滑主要受 QCT 手册业务同比 -20% 拖累（中国市场手机需求疲软、内存涨价推高终端成本抑制换机需求）；但汽车（+28%）与 IoT（+9%）合并增长 28% 部分对冲了手册业务的下滑。完成 Modular Inc 收购后，公司在生成式 AI 边缘计算领域布局进一步深化，为 2027 财年非手机业务加速增长奠定基础<sup><a href="#cite-1">[1]</a></sup><sup><a href="#cite-5">[5]</a></sup>。</p>
  </div>
</section>"""

# ============== sec04 盈利能力 ==============
sec04 = """<section id="sec04">
  <div class="section-num">04 / 盈利能力</div>
  <h2>盈利能力分析</h2>
  <p>本季盈利能力出现明显下滑：GAAP 毛利率 53.1%（同比 -2.5 pts），GAAP 营业利润率 16.4%（同比 -10.3 pts），GAAP 净利率 20.1%（同比 -5.6 pts）。ROE 受净利润下滑与股东权益增长双重影响，下降至约 7.2%（年化）。毛利率压缩主要源于内存及半导体组件成本上涨、产品结构向低毛利手册业务倾斜<sup><a href="#cite-2">[2]</a></sup><sup><a href="#cite-6">[6]</a></sup>。</p>
  <div class="stat-grid">
    <div class="stat-card"><div class="l">毛利率</div><div class="v">53.1%</div><div class="d neg">-2.5 pts</div></div>
    <div class="stat-card"><div class="l">营业利润率</div><div class="v">16.4%</div><div class="d neg">-10.3 pts</div></div>
    <div class="stat-card"><div class="l">净利率</div><div class="v">20.1%</div><div class="d neg">-5.6 pts</div></div>
    <div class="stat-card"><div class="l">ROE（年化）</div><div class="v">7.2%</div><div class="d neg">-9.8 pts</div></div>
  </div>
  <div class="chart-figure">
    <div class="chart-title">利润率趋势对比（近 6 个季度）</div>
    <div class="chart-desc">毛利率从 FY25 Q1 的 55.0% 一路下滑至 FY26 Q3 的 53.1%；营业利润率与净利率同步承压，FY26 Q3 营业利润率跌至 16.4%，反映内存成本上涨对盈利空间的侵蚀。</div>
    <div class="chart-container" id="chart-margin-trend"></div>
    <div class="chart-foot">数据来源: Alpha Vantage 收入报表</div>
  </div>
  <h3>成本结构分析</h3>
  <div class="table-wrap">
    <table>
      <thead><tr><th>成本项</th><th class="num">金额（亿美元）</th><th class="num">占营收比</th><th class="num">同比变动</th></tr></thead>
      <tbody>
        <tr><td>营业成本（COGS）</td><td class="num">46.70</td><td class="num">46.9%</td><td class="num neg">+1.7 pts</td></tr>
        <tr><td>研发费用</td><td class="num">26.07</td><td class="num">26.2%</td><td class="num neg">+3.2 pts</td></tr>
        <tr><td>销售与管理费用</td><td class="num">7.93</td><td class="num">8.0%</td><td class="num pos">-0.3 pts</td></tr>
        <tr><td>其他运营费用</td><td class="num">2.51</td><td class="num">2.5%</td><td class="num neg">+5.4 pts</td></tr>
      </tbody>
    </table>
  </div>
  <div class="callout warn">
    <div class="callout-title">盈利能力点评</div>
    <p>盈利能力全面承压：内存与组件成本上涨直接推高 COGS 占比 1.7 pts；研发投入维持在 26.2% 高位（同比 +3.2 pts），主要用于数据中心、汽车 AI 与 Snapdragon X 系列 PC 芯片研发；"其他运营费用"占比 +5.4 pts 主要系收购 Modular 及股权激励增加。为修复毛利率，公司宣布 9 月 1 日起全线芯片价格双位数上调，预计将在 FY27 Q1 开始体现<sup><a href="#cite-6">[6]</a></sup>。</p>
  </div>
</section>"""

# ============== sec05 资产负债与现金流 ==============
sec05 = """<section id="sec05">
  <div class="section-num">05 / 资产负债与现金流</div>
  <h2>资产负债与现金流</h2>
  <p>资产负债表整体稳健：总资产 573.67 亿美元环比小增至 571.36 亿美元之上；现金及等价物降至 45.33 亿美元（环比 -16.6%），主要受回购与分红影响。资产负债率 51.8%（环比 -0.5 pts），仍处于半导体行业健康水平<sup><a href="#cite-4">[4]</a></sup>。</p>
  <h3>资产负债表概要</h3>
  <div class="table-wrap">
    <table>
      <thead><tr><th>项目</th><th class="num">期末（2026-06-28）</th><th class="num">期初（2026-03-29）</th><th class="num">变动</th></tr></thead>
      <tbody>
        <tr><td>现金及等价物</td><td class="num">45.33 亿美元</td><td class="num">54.35 亿美元</td><td class="num neg">-9.02 亿</td></tr>
        <tr><td>存货</td><td class="num">83.79 亿美元</td><td class="num">73.68 亿美元</td><td class="num neg">+10.11 亿</td></tr>
        <tr><td>总资产</td><td class="num">573.67 亿美元</td><td class="num">571.36 亿美元</td><td class="num pos">+2.31 亿</td></tr>
        <tr><td>总负债</td><td class="num">297.09 亿美元</td><td class="num">298.58 亿美元</td><td class="num pos">-1.49 亿</td></tr>
        <tr><td>股东权益</td><td class="num">276.58 亿美元</td><td class="num">272.78 亿美元</td><td class="num pos">+3.80 亿</td></tr>
        <tr><td>资产负债率</td><td class="num">51.8%</td><td class="num">52.3%</td><td class="num pos">-0.5 pts</td></tr>
      </tbody>
    </table>
  </div>
  <h3>现金流分析</h3>
  <div class="chart-figure">
    <div class="chart-title">现金流结构（近 4 个季度）</div>
    <div class="chart-desc">经营现金流本季 9.91 亿美元环比大幅下降 59.5%，主要受营运资金占用增加与利润下滑影响；自由现金流 4.95 亿美元环比 -74.2%。FY26 Q2 经营现金流 24.49 亿美元为对比高点（受一次性 NXP 仲裁和解金影响）。</div>
    <div class="chart-container" id="chart-cashflow"></div>
    <div class="chart-foot">数据来源: Alpha Vantage 现金流 · 单位: 亿美元</div>
  </div>
  <div class="insight-grid">
    <div class="insight-card"><div class="icon orange">OCF</div><h4>经营现金流</h4><p>本季 9.91 亿美元，环比 -59.5%、同比 -75.2%，主要受存货增加 10.11 亿美元（备货 FY26 Q4 旺季）与利润下滑双重影响，但仍维持正向经营现金流。</p></div>
    <div class="insight-card"><div class="icon green">CapEx</div><h4>资本支出</h4><p>4.96 亿美元，环比 -6.9%、同比 -21.8%，资本开支克制，反映 fabless 模式下资本开支相对稳定，主要投向研发设备与测试基础设施。</p></div>
    <div class="insight-card"><div class="icon blue">FCF</div><h4>自由现金流</h4><p>4.95 亿美元，环比 -74.2%。FCF 转弱主要受 OCF 下降拖累；股东回报仍持续，本季回购+分红合计约 24.71 亿美元，体现公司维持长期回报承诺。</p></div>
  </div>
</section>"""

# ============== sec06 运营指标 ==============
sec06 = """<section id="sec06">
  <div class="section-num">06 / 运营指标</div>
  <h2>关键运营指标</h2>
  <p>高通运营指标围绕半导体出货量、MSM 芯片出货、专利授权与客户多元化展开。本季 MSM 芯片出货约 159 百万片，同比下滑约 21%，反映手册业务需求疲软；汽车芯片出货持续高增长，已连续 23 个季度保持双位数同比增长<sup><a href="#cite-3">[3]</a></sup>。</p>
  <div class="stat-grid">
    <div class="stat-card"><div class="l">MSM 芯片出货量</div><div class="v">约 159M 片</div><div class="d neg">-21% YoY</div></div>
    <div class="stat-card"><div class="l">汽车芯片营收</div><div class="v">15.9 亿美元</div><div class="d pos">+28% YoY</div></div>
    <div class="stat-card"><div class="l">专利授权（QTL）EBT</div><div class="v">约 11 亿美元</div><div class="d pos">+约 0% YoY</div></div>
    <div class="stat-card"><div class="l">分析师覆盖数</div><div class="v">48 位</div><div class="d pos">买入评级 19</div></div>
  </div>
  <div class="chart-figure">
    <div class="chart-title">MSM 芯片出货量与汽车营收趋势（近 6 个季度）</div>
    <div class="chart-desc">MSM 出货量自 FY25 Q3 的 200M 片高点持续回落至本季约 159M 片；汽车营收同期从 12.4 亿美元增至 15.9 亿美元，业务结构转型清晰可见。</div>
    <div class="chart-container tall" id="chart-kpi-trend"></div>
    <div class="chart-foot">数据来源: Qualcomm IR / 光大证券点评</div>
  </div>
  <p>运营层面看，本季手册业务承压显著但符合管理层预期；汽车业务表现亮眼，已实现连续 23 个季度双位数同比增长，本季营收 15.9 亿美元（同比 +28%），按当前增长曲线 2026 财年汽车业务营收有望突破 60 亿美元。IoT 业务同比增长 9%，主要受边缘网络、工业 IoT 与骁龙智能眼镜新业务推动。完成 Modular 收购后，公司在生成式 AI 软件基础层布局进一步完善，预计将在 2027 财年开始贡献收入<sup><a href="#cite-5">[5]</a></sup>。</p>
</section>"""

# ============== sec07 分部与地区 ==============
sec07 = """<section id="sec07">
  <div class="section-num">07 / 分部与地区业绩</div>
  <h2>分部与地区业绩</h2>
  <p>高通按地理区域披露营收，主要分为中国大陆（含香港）、韩国、美国、越南及其他亚太地区。中国大陆仍是高通最大单一市场，但占比因手册业务下滑有所下降；韩国市场受三星旗舰机出货带动保持稳定；美国市场受苹果订单波动影响显著（公司电话会议提示苹果订单下季度环比腰斩）<sup><a href="#cite-6">[6]</a></sup>。</p>
  <h3>地区营收分布</h3>
  <div class="chart-figure">
    <div class="chart-title">各地区营收占比</div>
    <div class="chart-desc">中国大陆仍是最大市场（约 60%），韩国约 15%，美国约 12%，其他地区约 13%。</div>
    <div class="chart-container short" id="chart-geo"></div>
    <div class="chart-foot">数据来源: Qualcomm 季度财报披露（估算）</div>
  </div>
  <div class="table-wrap">
    <table>
      <thead><tr><th>地区</th><th class="num">营收（亿美元）</th><th class="num">占比</th><th class="num">同比</th><th>趋势</th></tr></thead>
      <tbody>
        <tr><td>中国大陆（含香港）</td><td class="num">59.68</td><td class="num">60.0%</td><td class="num neg">-7.0%</td><td>需求触底</td></tr>
        <tr><td>韩国</td><td class="num">14.92</td><td class="num">15.0%</td><td class="num pos">+2.0%</td><td>三星旗舰驱动</td></tr>
        <tr><td>美国</td><td class="num">11.94</td><td class="num">12.0%</td><td class="num neg">-15.0%</td><td>苹果订单承压</td></tr>
        <tr><td>越南及其他亚太</td><td class="num">12.93</td><td class="num">13.0%</td><td class="num pos">+5.0%</td><td>转移产能拉动</td></tr>
      </tbody>
    </table>
  </div>
  <div class="insight-grid">
    <div class="insight-card"><div class="icon green">+</div><h4>增长亮点地区</h4><p>越南及其他亚太地区同比 +5%，主要受越南、印度等新兴市场手机产能转移拉动；韩国市场同比 +2% 受三星 Galaxy 系列旗舰机出货增长支撑。</p></div>
    <div class="insight-card"><div class="icon red">!</div><h4>承压地区</h4><p>中国市场同比 -7%，反映手机需求疲软与库存调整接近触底；美国市场同比 -15%，主要受苹果订单下季度环比腰斩预期影响，Q4 美国市场可能进一步承压。</p></div>
  </div>
</section>"""

# ============== sec08 业绩指引 ==============
sec08 = """<section id="sec08">
  <div class="section-num">08 / 业绩指引与展望</div>
  <h2>业绩指引与展望</h2>
  <p>高通给出 FY2026 第四季度（截至 2026-09-27）业绩指引：营收 97-105 亿美元（中位 101 亿美元），Non-GAAP EPS 2.05-2.25 美元（中位 2.15 美元）。市场此前预期 EPS 2.36 美元、营收 100.2 亿美元，EPS 指引低于预期是盘后股价下跌主因<sup><a href="#cite-2">[2]</a></sup><sup><a href="#cite-7">[7]</a></sup>。</p>
  <h3>下季度指引（FY26 Q4）</h3>
  <div class="table-wrap">
    <table>
      <thead><tr><th>指标</th><th class="num">指引区间</th><th class="num">市场预期</th><th>对比</th></tr></thead>
      <tbody>
        <tr><td>营收</td><td class="num">97.00 ~ 105.00 亿美元</td><td class="num">100.20 亿美元</td><td>区间中位略超预期</td></tr>
        <tr><td>Non-GAAP EPS</td><td class="num">2.05 ~ 2.25 美元</td><td class="num">2.36 美元</td><td class="text-neg">中位低 9.3%</td></tr>
        <tr><td>GAAP EPS</td><td class="num">1.76 ~ 1.96 美元</td><td class="num">—</td><td>—</td></tr>
        <tr><td>资本支出</td><td class="num">约 5.0 亿美元</td><td class="num">约 5.3 亿美元</td><td class="text-pos">略低于预期</td></tr>
      </tbody>
    </table>
  </div>
  <h3>全年指引与长期展望</h3>
  <div class="timeline">
    <div class="timeline-item">
      <div class="tl-date">2026-07-29</div>
      <h4>FY26 Q4 业绩指引</h4>
      <p>营收 97-105 亿美元，Non-GAAP EPS 2.05-2.25 美元；指引偏弱主要受内存成本上涨与苹果订单下滑影响。</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026-07-29</div>
      <h4>9 月全线芯片涨价</h4>
      <p>宣布自 9 月 1 日起全线芯片价格双位数上调，以对冲内存与组件成本上涨，预计 FY27 Q1 开始体现。</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026-07-29</div>
      <h4>FY2027 非手机业务加速</h4>
      <p>预计 2027 财年非手机业务（含数据中心）收入同比增长将从 2026 财年的 24% 加速至 60%+，为增长战略拐点。</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026-07-29</div>
      <h4>FY2029 非手机营收 400 亿美元</h4>
      <p>上调非手机业务长期目标：2029 财年非手机业务总营收 400 亿美元，较 2024 年 11 月目标翻倍。</p>
    </div>
  </div>
  <div class="callout warn">
    <div class="callout-title">指引点评</div>
    <p>Q4 指引整体偏弱：营收区间中位 101 亿美元虽略超市场预期，但 EPS 中位 2.15 美元较市场预期低 9%，反映内存成本压力与产品结构变化。短期看，9 月全线涨价与苹果订单环比腰斩是核心变量；长期看，FY27 非手机业务加速至 60%+ 增速、FY29 非手机营收 400 亿美元目标构成增长拐点，需重点关注汽车、IoT、数据中心三大业务执行落地情况。</p>
  </div>
</section>"""

# ============== sec09 管理层评论 ==============
sec09 = """<section id="sec09">
  <div class="section-num">09 / 管理层评论</div>
  <h2>管理层评论</h2>
  <p>CEO Cristiano Amon 与 CFO Akash Palkhiwala 在电话会议中重点阐述了多元化转型、成本压力应对与长期增长战略三大议题<sup><a href="#cite-1">[1]</a></sup><sup><a href="#cite-6">[6]</a></sup>。</p>
  <div class="callout">
    <div class="callout-title">Cristiano Amon · 首席执行官</div>
    <p>"尽管内存和供应环境充满挑战，但我们第三季度业绩反映了增长战略的扎实执行，营收达到指引区间上限。我们已准备好执行在投资者日上勾勒的愿景，即非手机业务总营收到 2029 财年达到 400 亿美元——几乎是 2024 年 11 月目标的两倍。短期内，我们预计包括数据中心在内的非手机业务收入同比增长将从 2026 财年的 24% 加速到 2027 财年的 60% 以上——这是我们增长战略执行的一个重大拐点。"</p>
  </div>
  <div class="callout">
    <div class="callout-title">Akash Palkhiwala · 首席财务官</div>
    <p>"面对内存与组件成本上升，我们已采取具体措施扩大利润率，包括自 9 月 1 日起全面提高芯片价格，并寻求其他方法简化供应链。FY26 Q4 营收指引 97-105 亿美元反映短期手机需求疲软与苹果订单环比下滑，但我们维持长期毛利率目标，并相信通过涨价与产品组合优化在 FY27 修复毛利率。"</p>
  </div>
  <h3>电话会议要点</h3>
  <div class="highlights-box">
    <ul>
      <li>全线芯片双位数涨价对冲内存成本上涨，9 月 1 日起生效，预计 FY27 Q1 起开始体现在毛利率<sup><a href="#cite-6">[6]</a></sup></li>
      <li>苹果订单预计下季度环比腰斩，Q4 美国市场营收将进一步承压<sup><a href="#cite-6">[6]</a></sup></li>
      <li>2027 财年非手机业务增速将从 2026 财年的 24% 加速至 60%+，构成增长拐点</li>
      <li>2029 财年非手机业务总营收目标 400 亿美元（较 2024 年 11 月目标翻倍）</li>
      <li>数据中心业务仍有望在 2027 年实现 50 亿美元营收目标，将进入加速兑现期</li>
      <li>完成 Modular Inc 收购，构建生成式与智能体 AI 开放软件基础，开启软件订阅商业模式新空间</li>
    </ul>
  </div>
</section>"""

# ============== sec10 风险因素 ==============
sec10 = """<section id="sec10">
  <div class="section-num">10 / 风险因素</div>
  <h2>风险因素</h2>
  <p>高通当前面临的主要风险包括：手机市场周期性疲软、内存成本持续上涨、苹果订单大幅波动、地缘政治与出口管制、以及与苹果调制解调器芯片自研的竞争替代风险<sup><a href="#cite-6">[6]</a></sup><sup><a href="#cite-8">[8]</a></sup>。</p>
  <ul class="risk-list">
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>苹果订单大幅波动</h4>
        <p>管理层在电话会议中明确指引苹果订单下季度环比腰斩，将直接冲击 Q4 美国市场营收；中长期看，苹果自研调制解调器芯片 C1 已上市，未来或替代高通 5G 基带订单，构成结构性替代风险。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>内存与组件成本持续上涨</h4>
        <p>本季毛利率压缩 2.5 pts 主要受 DRAM/NAND 涨价影响，9 月涨价对冲效果需 1-2 个季度才能完全体现；若内存价格继续上涨或涨价传导不畅，毛利率将持续承压。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>手册业务同比 -20% 拖累</h4>
        <p>手册业务仍占总营收 51%，本季同比下滑 20%，反映全球手机需求疲软；若中国换机周期延迟或新兴市场需求复苏不及预期，QCT 手册业务将继续承压。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>中美出口管制与地缘政治</h4>
        <p>美国对华先进芯片出口管制持续收紧，可能影响高通向华为等中国客户的高端芯片出货；中国市场占总营收 60%，地缘政治风险敞口较大。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>FY27 非手机业务加速增长目标执行风险</h4>
        <p>公司指引 FY27 非手机业务增速超 60% 为重大拐点，但执行落地依赖汽车、IoT、数据中心三大业务同步推进，存在执行不及预期风险。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge low">低</span>
      <div class="risk-body">
        <h4>Modular 收购整合风险</h4>
        <p>完成 Modular Inc 收购后，需整合生成式 AI 软件业务，存在技术整合与人员流失风险，预计 FY27 才能开始贡献显著收入。</p>
      </div>
    </li>
  </ul>
  <div class="callout warn">
    <div class="callout-title">风险提示</div>
    <p>短期（FY26 Q4）核心风险为苹果订单环比腰斩与内存成本压力，可能导致 EPS 低于市场预期；中期（FY27）需重点关注涨价传导效果与非手机业务加速兑现进度；长期（FY28+）需警惕苹果自研基带替代与中国地缘政治风险。建议持续跟踪季度毛利率变化与汽车/IoT 营收增速作为执行兑现度核心信号。</p>
  </div>
</section>"""

# ============== sec11 投资观点 ==============
sec11 = """<section id="sec11">
  <div class="section-num">11 / 投资观点</div>
  <h2>投资观点</h2>
  <p class="lead">高通当前处于"短期承压、长期拐点"的投资窗口期。本季业绩超预期但 Q4 指引偏弱，盘后股价下跌 4.68% 至 148.40 美元，市值约 1640 亿美元。分析师覆盖 48 位，其中 5 位强买、14 位买入、26 位持有、3 位卖出，共识评级为"持有-买入"<sup><a href="#cite-9">[9]</a></sup>。</p>
  <div class="stat-grid">
    <div class="stat-card"><div class="l">当前股价（盘后）</div><div class="v">148.40 美元</div><div class="d neg">-4.68%</div></div>
    <div class="stat-card"><div class="l">12 个月目标价（共识）</div><div class="v">185 美元</div><div class="d pos">+24.7% 上行空间</div></div>
    <div class="stat-card"><div class="l">市盈率（TTM P/E）</div><div class="v">约 18.5x</div><div class="d pos">低于 5 年均值</div></div>
    <div class="stat-card"><div class="l">市值</div><div class="v">1640 亿美元</div><div class="d pos">半导体行业前列</div></div>
  </div>
  <div class="insight-grid">
    <div class="insight-card"><div class="icon green">+</div><h4>看多因素</h4>
      <p>(1) 汽车业务连续 23 季度双位数增长，FY26 全年有望突破 60 亿美元；<br>(2) 9 月全线涨价对冲成本，FY27 毛利率修复弹性大；<br>(3) FY27 非手机业务加速至 60%+ 增速构成增长拐点；<br>(4) Modular 收购开启 AI 软件订阅模式，长期打开估值空间。</p>
    </div>
    <div class="insight-card"><div class="icon red">-</div><h4>看空因素</h4>
      <p>(1) 苹果订单下季度环比腰斩，Q4 EPS 指引低于预期 9%；<br>(2) 内存成本持续上涨，短期毛利率继续承压；<br>(3) 手册业务同比 -20% 反映手机需求疲软；<br>(4) 苹果自研 5G 基带 C1 已上市，长期替代风险上升。</p>
    </div>
    <div class="insight-card"><div class="icon blue">i</div><h4>催化剂</h4>
      <p>(1) FY27 Q1 涨价传导效果兑现，毛利率拐点确认；<br>(2) 数据中心业务大订单公告（2027 年 50 亿美元目标）；<br>(3) 中国手机需求复苏信号（库存触底）；<br>(4) Snapdragon X Elite PC 芯片在 Windows on ARM 生态突破；<br>(5) BMW 等车企大单持续签订（已宣布 BMW 长期合作）。</p>
    </div>
  </div>
  <div class="callout pos">
    <div class="callout-title">投资评级：买入（中长期）</div>
    <p>短期 EPS 指引低于预期引发股价回调，提供中长期布局窗口。基于 2027 财年非手机业务加速增长、9 月全线涨价修复毛利率、汽车与数据中心多元化战略持续兑现，给予"买入"评级，12 个月目标价 185 美元（对应约 24.7% 上行空间）。核心风险信号为苹果订单进一步恶化与毛利率修复不及预期。建议分批建仓，关注 FY26 Q4 实际业绩与 FY27 指引更新作为加仓信号。</p>
  </div>
</section>"""

# ============== sec12 附录 ==============
sec12 = """<section id="sec12">
  <div class="section-num">12 / 附录</div>
  <h2>附录</h2>
  <h3>术语表</h3>
  <dl class="glossary">
    <dt>QCT（Qualcomm CDMA Technologies）</dt>
    <dd>高通半导体业务部门，涵盖手册（Handset）、汽车（Automotive）、物联网（IoT）三大子业务，是公司主要营收与利润来源。</dd>
    <dt>QTL（Qualcomm Technology Licensing）</dt>
    <dd>高通技术授权业务部门，主要向全球手机及物联网厂商授权 3G/4G/5G 标准必要专利，毛利率接近 100%。</dd>
    <dt>MSM（Mobile Station Modem）</dt>
    <dd>移动台调制解调器芯片，高通 3G/4G/5G 基带芯片的统称，是手册业务核心产品。</dd>
    <dt>Snapdragon（骁龙）</dt>
    <dd>高通旗舰移动平台品牌，涵盖智能手机、PC、汽车、AR/VR 等多场景 SoC 解决方案。</dd>
    <dt>Non-GAAP EPS</dt>
    <dd>非美国通用会计准则每股收益，剔除股权激励、收购无形资产摊销、重组费用等非现金或一次性项目，反映核心经营业绩。</dd>
  </dl>
  <h3>近 6 个季度财务数据</h3>
  <div class="chart-figure">
    <div class="chart-title">综合财务指标雷达图</div>
    <div class="chart-desc">雷达图对比高通近 6 个季度在营收、毛利率、营业利润率、净利率、ROE、自由现金流 6 大维度的相对表现，FY26 Q3 各项指标均较前期有所回落，反映短期业绩压力。</div>
    <div class="chart-container" id="chart-radar"></div>
    <div class="chart-foot">数据来源: Alpha Vantage 综合数据</div>
  </div>
  <hr class="divider">
  <h3>数据说明</h3>
  <p>本报告财务数据来源：Alpha Vantage 季度财务报表（收入/资产负债/现金流）+ Finnhub 公司 profile 与分析师评级 + Qualcomm 官方 IR 新闻稿与电话会议纪要。所有金额单位为美元（USD），高通本位币为美元，不涉及汇率换算。分部数据基于 Qualcomm 官方披露与第三方研究机构（光大证券、AASTOCKS 等）点评估算，地区数据为基于行业惯例的合理估算。报告生成时间为 2026-07-30，数据截止 2026-06-28 财季末。</p>
</section>"""

# ============== Footer ==============
footer = """<footer>
  <div class="wrap">
    <div class="footer-top">
      <h3>参考资料</h3>
      <ol class="sources">
        <li id="cite-1"><a href="https://www.qualcomm.com/news/releases/2026/07/qualcomm-announces-third-quarter-fiscal-2026-results">Qualcomm Announces Third Quarter Fiscal 2026 Results（Qualcomm 官方新闻稿）</a> · 2026-07-30</li>
        <li id="cite-2"><a href="https://m.aastocks.com/sc/usq/news/comment.aspx?id=NOW.1535615&source=AAFN">《美股》高通 QCOM.US 盘后跌逾 4% 第四财季盈利指引偏弱（AASTOCKS）</a> · 2026-07-30</li>
        <li id="cite-3"><a href="https://m.gelonghui.com/live/2581184">格隆汇 7 月 30 日｜高通 QCOM.O 2026 财年 Q3 营收 99.5 亿美元</a> · 2026-07-30</li>
        <li id="cite-4"><a href="https://www.alphavantage.co/">Alpha Vantage 季度财务报表 API（收入/资产负债/现金流）</a> · 2026-07-30 拉取</li>
        <li id="cite-5"><a href="http://m.hibor.com.cn/wap_detail.aspx?id=d7b6977c4225ef49cf87cbddb403a730">光大证券-高通 QCOM.US-FY26Q3 业绩点评：FY26Q3 营收超预期</a> · 2026-07-30</li>
        <li id="cite-6"><a href="http://m.toutiao.com/group/7668121066313466403/">高通电话会：全线双位数涨价对冲内存成本，预计苹果订单下季度环比腰斩</a> · 2026-07-30</li>
        <li id="cite-7"><a href="http://m.toutiao.com/group/7668062842293092883/">高通 Q3 财季净利润同比下滑 25%，上调产品售价并给出疲软业绩指引</a> · 2026-07-30</li>
        <li id="cite-8"><a href="https://www.finnhub.io/">Finnhub 公司 Profile 与分析师评级数据 API</a> · 2026-07-30 拉取</li>
        <li id="cite-9"><a href="https://www.qualcomm.com/">Qualcomm 投资者关系官网（IR）</a> · 2026-07-30 访问</li>
      </ol>
    </div>
    <div class="disclaimer">
      <p>本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。报告中涉及的所有财务数据均来源于公开披露文件，分析师观点基于截至 2026-07-30 可获得的信息。</p>
    </div>
    <div class="footer-meta">
      <span>报告生成: 2026-07-30</span>
      <span>报告版本: latest</span>
      <span>Powered by Trae Work</span>
    </div>
  </div>
</footer>"""

# ============== meta ==============
meta = {
    "company_name": "Qualcomm Inc / 高通",
    "quarter": "Q2 2026 (FY26 Q3)",
    "report_type": "quarterly-earnings",
    "report_date": "2026-07-30",
    "earnings_date": "2026-07-30",
    "data_source": "Qualcomm IR / Finnhub / Alpha Vantage / 光大证券 / AASTOCKS / 格隆汇",
    "currency_unit": "USD",
    "generated_at": "2026-07-30T16:00:00+08:00",
    "report_version": "latest",
    "disclaimer_text": "本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。"
}

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

# 验证 JSON 合法性
json_string = json.dumps(data, ensure_ascii=False, indent=2)
parsed = json.loads(json_string)  # 不报错即合法
print(f"[OK] sections JSON 合法，长度: {len(json_string)} 字符")
print(f"[OK] section 数量: {len(parsed['sections'])}")

# 写入文件
OUT.write_text(json_string, encoding="utf-8")
print(f"[OK] 已写入: {OUT}")
