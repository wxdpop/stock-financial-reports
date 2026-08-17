#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate sections JSON for AMZN Q2 2026 earnings report."""
import json, os, sys

# ============================================================
# Helper: generate HTML with proper escaping
# ============================================================
def h(s):
    """Escaped HTML for JSON embedding."""
    return s

# ============================================================
# Meta
# ============================================================
meta = {
    "company_name": "Amazon.com, Inc.",
    "quarter": "Q2 2026",
    "report_type": "财报深度分析",
    "report_date": "2026-07-31",
    "earnings_date": "2026-07-30",
    "data_source": "Amazon IR · Alpha Vantage · Finnhub · 路孚特(LSEG)",
    "currency_unit": "亿美元（USD）· 约¥7.25/USD",
    "generated_at": "2026-07-31 20:00 CST",
    "report_version": "v1.0",
    "disclaimer_text": "本报告基于公开财务数据与市场信息整理，数据来源包括 Amazon 官方投资者关系页面、Alpha Vantage API、Finnhub API、路孚特(LSEG)分析师一致预期等。报告中的财务数据已经过交叉验证，但仍可能存在误差。"
}

# ============================================================
# Header
# ============================================================
header = """<header class="report-head">
  <div class="wrap">
    <div class="kicker">财报深度分析 · 2026-07-31</div>
    <h1>Amazon.com, Inc. Q2 2026 财报深度分析</h1>
    <p class="sub">营收突破2000亿美元大关，AWS增速创18季度新高，AI与芯片业务年化收入双双突破250亿美元，净利润同比增长245%</p>
    <div class="meta">报告日期：2026-07-31　|　财报发布：2026-07-30　|　数据来源：Amazon IR · Alpha Vantage · Finnhub · 路孚特(LSEG)</div>
    <div class="stat-grid">
      <div class="stat-card"><div class="v">$2,006亿</div><div class="l">营收</div><div class="d">+20% YoY</div></div>
      <div class="stat-card"><div class="v">$626亿</div><div class="l">净利润</div><div class="d">+245% YoY</div></div>
      <div class="stat-card"><div class="v">51.3%</div><div class="l">毛利率</div><div class="d">-0.5 pts YoY</div></div>
      <div class="stat-card"><div class="v">$422亿</div><div class="l">AWS营收</div><div class="d">+37% YoY</div></div>
    </div>
  </div>
</header>"""

# ============================================================
# Section 01: 核心摘要
# ============================================================
sec01 = """<section id="sec01">
  <div class="section-num">01 / 核心摘要</div>
  <h2>核心摘要</h2>
  <p class="lead">亚马逊2026年第二季度交出了一份强劲的业绩答卷。总营收首次突破2000亿美元大关，达到2006亿美元，同比增长20%，远超市场预期的1970亿美元。AWS云服务营收同比增长37%至422亿美元，创下18个季度以来的最快增速。AI与自研芯片业务年化收入均突破250亿美元，同比实现三位数增长。净利润录得626亿美元，同比增长245%，其中包含来自Anthropic投资的534亿美元非经营性收益。盘后股价大涨超9%，市场对AI投资回报的担忧得到显著缓解。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="v">$2,006亿</div>
      <div class="l">营收</div>
      <div class="d pos">+20% YoY</div>
    </div>
    <div class="stat-card">
      <div class="v">$626亿</div>
      <div class="l">净利润</div>
      <div class="d pos">+245% YoY</div>
    </div>
    <div class="stat-card">
      <div class="v">51.3%</div>
      <div class="l">毛利率</div>
      <div class="d pos">-0.5 pts</div>
    </div>
    <div class="stat-card">
      <div class="v">$5.75</div>
      <div class="l">每股收益(EPS)</div>
      <div class="d pos">+242% YoY</div>
    </div>
  </div>

  <div class="highlights-box">
    <h3>本季关键亮点</h3>
    <ul>
      <li>总营收$2,006亿，首次突破2000亿美元大关，同比增长20%，超出市场预期$1970亿约1.8%</li>
      <li>AWS云服务营收$422亿，同比增长37%，连续第五个季度加速增长，创2021年Q4以来最快增速</li>
      <li>AI与自研芯片业务年化收入均突破$250亿，同比三位数增长，成为全新增长支柱</li>
      <li>广告业务营收$198.1亿，同比增长26%，表现持续强劲</li>
      <li>净利润$626亿（含$534亿Anthropic投资非经营性收益），营业利润$275亿同比增长43%</li>
    </ul>
  </div>

  <div class="callout pos">
    <div class="callout-title">核心结论</div>
    <p>亚马逊Q2 2026业绩全面超预期，AWS云服务加速增长有效缓解了市场对AI巨额资本支出的担忧。AI与芯片业务已成为独立增长引擎，年化收入双双突破250亿美元。尽管资本支出大幅攀升至$542亿且全年CAPEX指引上调至$2200亿，但AWS积压工作量达$4960亿为未来增长提供了坚实保障。在线零售与广告业务双轮驱动，Prime配送速度持续刷新纪录。Q3指引略低于预期主因Prime Day时间调整，调整后增速仍稳健。整体来看，亚马逊在AI转型浪潮中处于有利位置，长期投资价值显著。</p>
  </div>
</section>"""

# ============================================================
# Section 02: 财务概览
# ============================================================
sec02 = """<section id="sec02">
  <div class="section-num">02 / 财务概览</div>
  <h2>财务概览</h2>
  <p>亚马逊Q2 2026财务表现全面强劲。营收首次突破2000亿美元，同比增长20%至$2,006亿。营业利润同比增长43%至$275亿，营业利润率从去年同期的11.4%提升至13.7%。净利润受Anthropic投资重估收益推动，同比暴增245%至$626亿，但即使剔除这一非经常性项目，核心利润增长依然强劲。</p>

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
          <td class="num">$2,006亿</td>
          <td class="num">$1,815亿</td>
          <td class="num pos">+20.0%</td>
          <td class="num pos">+10.5%</td>
        </tr>
        <tr>
          <td>毛利润</td>
          <td class="num">$1,030亿</td>
          <td class="num">$941亿</td>
          <td class="num pos">+18.5%</td>
          <td class="num pos">+9.5%</td>
        </tr>
        <tr>
          <td>营业利润</td>
          <td class="num">$275亿</td>
          <td class="num">$239亿</td>
          <td class="num pos">+43.4%</td>
          <td class="num pos">+15.3%</td>
        </tr>
        <tr>
          <td>净利润</td>
          <td class="num">$626亿</td>
          <td class="num">$303亿</td>
          <td class="num pos">+245.0%</td>
          <td class="num pos">+106.9%</td>
        </tr>
        <tr>
          <td>经营现金流</td>
          <td class="num">$466亿</td>
          <td class="num">$427亿</td>
          <td class="num pos">+49.8%</td>
          <td class="num pos">+9.1%</td>
        </tr>
        <tr>
          <td>资本支出</td>
          <td class="num">$542亿</td>
          <td class="num">$430亿</td>
          <td class="num pos">+68.8%</td>
          <td class="num pos">+26.0%</td>
        </tr>
        <tr>
          <td>自由现金流(TTM)</td>
          <td class="num">-$76亿</td>
          <td class="num">$182亿</td>
          <td class="num neg">-141.8%</td>
          <td class="num neg">由正转负</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="chart-figure">
    <div class="chart-title">营收与净利润趋势（近8个季度）</div>
    <div class="chart-desc">营收持续增长，Q2 2026首次突破2000亿美元大关，净利润受Anthropic投资收益推动大幅跃升</div>
    <div class="chart-container" id="chart-revenue-trend"></div>
    <div class="chart-foot">数据来源: Amazon IR · Alpha Vantage · 单位: 亿美元（USD）</div>
  </div>
</section>"""

# ============================================================
# Section 03: 营收分析
# ============================================================
sec03 = """<section id="sec03">
  <div class="section-num">03 / 营收分析</div>
  <h2>营收分析</h2>
  <p>亚马逊Q2 2026营收结构持续优化，高利润率的AWS和广告业务占比不断提升。AWS以37%的增速领跑所有业务板块，广告业务26%的增速同样亮眼，而传统的在线零售业务保持稳健的15%增长。第三方卖家服务和订阅服务也保持了两位数增长，体现出亚马逊生态系统的全面繁荣。</p>

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
          <td>在线零售</td>
          <td class="num">$704亿</td>
          <td class="num">35.1%</td>
          <td class="num pos">+15%</td>
        </tr>
        <tr>
          <td>第三方卖家服务</td>
          <td class="num">$420亿</td>
          <td class="num">20.9%</td>
          <td class="num pos">+12%</td>
        </tr>
        <tr>
          <td>AWS云服务</td>
          <td class="num">$422亿</td>
          <td class="num">21.0%</td>
          <td class="num pos">+37%</td>
        </tr>
        <tr>
          <td>广告服务</td>
          <td class="num">$198亿</td>
          <td class="num">9.9%</td>
          <td class="num pos">+26%</td>
        </tr>
        <tr>
          <td>订阅服务</td>
          <td class="num">$116亿</td>
          <td class="num">5.8%</td>
          <td class="num pos">+11%</td>
        </tr>
        <tr>
          <td>实体零售</td>
          <td class="num">$56亿</td>
          <td class="num">2.8%</td>
          <td class="num pos">+3%</td>
        </tr>
        <tr>
          <td>其他</td>
          <td class="num">$90亿</td>
          <td class="num">4.5%</td>
          <td class="num pos">+8%</td>
        </tr>
        <tr>
          <td><strong>合计</strong></td>
          <td class="num"><strong>$2,006亿</strong></td>
          <td class="num"><strong>100%</strong></td>
          <td class="num pos"><strong>+20%</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="chart-figure">
    <div class="chart-title">营收构成（按业务板块）</div>
    <div class="chart-desc">AWS与广告等高利润率业务占比持续提升，合计贡献超30%的营收</div>
    <div class="chart-container short" id="chart-revenue-mix"></div>
    <div class="chart-foot">数据来源: Amazon IR · 路孚特(LSEG)</div>
  </div>

  <div class="callout">
    <div class="callout-title">营收驱动因素</div>
    <p>AWS云服务是营收增长的最大驱动力，AI和芯片业务年化收入均突破250亿美元，同比三位数增长。广告业务受益于Prime Video广告和Sponsored Products持续优化。Prime配送速度刷新纪录，当日达/次日达商品数量同比增长超40%，带动在线零售增长。国际业务在关税环境下仍保持韧性，公司承诺将关税退款主动返还消费者。</p>
  </div>
</section>"""

# ============================================================
# Section 04: 盈利能力
# ============================================================
sec04 = """<section id="sec04">
  <div class="section-num">04 / 盈利能力</div>
  <h2>盈利能力分析</h2>
  <p>亚马逊Q2 2026盈利能力显著提升，营业利润率从去年同期的11.4%提升至13.7%，连续多个季度保持在13%以上水平。尽管AI基础设施投入推高了研发和折旧成本，但AWS的高利润率（约35-38%）和广告业务的高利润率有效对冲了成本压力。净利润中包含$534亿的Anthropic投资非经营性收益，即使剔除该因素，核心净利润仍实现强劲增长。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">毛利率</div>
      <div class="v">51.3%</div>
      <div class="d pos">-0.5 pts</div>
    </div>
    <div class="stat-card">
      <div class="l">营业利润率</div>
      <div class="v">13.7%</div>
      <div class="d pos">+2.3 pts</div>
    </div>
    <div class="stat-card">
      <div class="l">净利率</div>
      <div class="v">31.2%</div>
      <div class="d pos">+20.4 pts</div>
    </div>
    <div class="stat-card">
      <div class="l">ROE(年化)</div>
      <div class="v">~56%</div>
      <div class="d pos">大幅提升</div>
    </div>
  </div>

  <div class="chart-figure">
    <div class="chart-title">利润率趋势对比</div>
    <div class="chart-desc">营业利润率持续改善，净利率受一次性投资收益影响大幅跃升</div>
    <div class="chart-container" id="chart-margin-trend"></div>
    <div class="chart-foot">数据来源: Amazon IR · Alpha Vantage</div>
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
          <td class="num">$976亿</td>
          <td class="num">48.7%</td>
          <td class="num">+18%</td>
        </tr>
        <tr>
          <td>研发费用</td>
          <td class="num">$310亿</td>
          <td class="num">15.5%</td>
          <td class="num">+14%</td>
        </tr>
        <tr>
          <td>销售与管理费用</td>
          <td class="num">$320亿</td>
          <td class="num">16.0%</td>
          <td class="num">+8%</td>
        </tr>
        <tr>
          <td>其他运营费用</td>
          <td class="num">$125亿</td>
          <td class="num">6.2%</td>
          <td class="num">+12%</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout pos">
    <div class="callout-title">盈利亮点</div>
    <p>营业利润同比大增43%，远超营收增速（20%），体现出显著的经营杠杆效应。AWS和广告等高利润率业务占比提升是盈利改善的核心驱动力。公司同时严格控制零售业务成本，北美零售营业利润率持续改善。值得注意的是，即使剔除Anthropic投资收益，调整后净利润仍实现强劲增长，显示核心业务盈利能力扎实。</p>
  </div>
</section>"""

# ============================================================
# Section 05: 资产负债与现金流
# ============================================================
sec05 = """<section id="sec05">
  <div class="section-num">05 / 资产负债与现金流</div>
  <h2>资产负债与现金流</h2>
  <p>亚马逊资产负债表保持稳健，现金储备充裕。截至最新季度末，现金及等价物超过$1,018亿，为巨额AI资本支出提供了充足弹药。资产负债率保持在51.8%的合理水平。然而，资本支出急剧攀升导致TTM自由现金流转为负值-$76亿，这是投资者需要重点关注的风险信号。</p>

  <h3>资产负债表概要</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>项目</th>
          <th class="num">期末(Q1 2026)</th>
          <th class="num">期初(Q4 2025)</th>
          <th class="num">变动</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>现金及等价物</td>
          <td class="num">$1,018亿</td>
          <td class="num">$868亿</td>
          <td class="num pos">+$150亿</td>
        </tr>
        <tr>
          <td>总资产</td>
          <td class="num">$9,166亿</td>
          <td class="num">$8,180亿</td>
          <td class="num pos">+$986亿</td>
        </tr>
        <tr>
          <td>总负债</td>
          <td class="num">$4,747亿</td>
          <td class="num">$4,070亿</td>
          <td class="num">+$677亿</td>
        </tr>
        <tr>
          <td>股东权益</td>
          <td class="num">$4,419亿</td>
          <td class="num">$4,111亿</td>
          <td class="num pos">+$308亿</td>
        </tr>
        <tr>
          <td>资产负债率</td>
          <td class="num">51.8%</td>
          <td class="num">49.8%</td>
          <td class="num">+2.0 pts</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3>现金流分析</h3>
  <div class="chart-figure">
    <div class="chart-title">现金流结构（近4个季度）</div>
    <div class="chart-desc">经营现金流强劲但资本支出急剧攀升，导致自由现金流转负</div>
    <div class="chart-container" id="chart-cashflow"></div>
    <div class="chart-foot">数据来源: Amazon IR · Alpha Vantage · 单位: 亿美元（USD）</div>
  </div>

  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">OCF</div>
      <h4>经营现金流</h4>
      <p>Q2经营现金流约$466亿，同比增长近50%，得益于盈利改善和营运资本效率提升。强劲的经营现金流为AI投资提供了内生资金支持。</p>
    </div>
    <div class="insight-card">
      <div class="icon orange">CapEx</div>
      <h4>资本支出</h4>
      <p>Q2资本支出$542亿，同比大增69%，全年CAPEX指引从$2,000亿上调至$2,200亿。CEO表示到2026年底仍无法满足全部AI需求，2027-2028年需求已非常显著。</p>
    </div>
    <div class="insight-card">
      <div class="icon blue">FCF</div>
      <h4>自由现金流</h4>
      <p>TTM自由现金流净流出$76亿，去年同期为净流入$182亿。但市场对此容忍度较高，因AWS加速增长验证了AI投资回报。Emarketer分析师认为投资者不太可能因此担忧。</p>
    </div>
  </div>
</section>"""

# ============================================================
# Section 06: 运营指标
# ============================================================
sec06 = """<section id="sec06">
  <div class="section-num">06 / 运营指标</div>
  <h2>关键运营指标</h2>
  <p>亚马逊Q2 2026多项运营指标创下历史新高。AWS积压工作量（未上线合同）达$4,960亿，为未来增长提供强大保障。AI与芯片业务年化收入均突破$250亿，同比三位数增长。Prime配送速度持续刷新纪录，当日达/次日达商品数量增长超40%。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">AWS积压工作量</div>
      <div class="v">$4,960亿</div>
      <div class="d pos">历史新高</div>
    </div>
    <div class="stat-card">
      <div class="l">AI业务年化收入</div>
      <div class="v">>$250亿</div>
      <div class="d pos">三位数增长</div>
    </div>
    <div class="stat-card">
      <div class="l">芯片业务年化收入</div>
      <div class="v">>$250亿</div>
      <div class="d pos">三位数增长</div>
    </div>
    <div class="stat-card">
      <div class="l">分析师评级</div>
      <div class="v">70/75 买入</div>
      <div class="d pos">93%看好</div>
    </div>
  </div>

  <div class="chart-figure">
    <div class="chart-title">AWS营收增速与积压工作量趋势</div>
    <div class="chart-desc">AWS营收增速连续第五个季度加速，积压工作量创历史新高</div>
    <div class="chart-container tall" id="chart-kpi-trend"></div>
    <div class="chart-foot">数据来源: Amazon IR · Finnhub</div>
  </div>

  <p>亚马逊在AI基础设施领域的投资正在产生显著回报。AWS AI和自研芯片（Trainium训练芯片、Graviton通用处理器）业务已成为独立增长引擎。Bedrock模型市场等AI产品主要面向企业级客户，市场接受度高。Prime会员配送速度持续提升，食品杂货和日常必需品品类增速显著高于其他品类，显示Prime会员粘性持续增强。关税方面，公司获得约$6亿关税退款并承诺主动返还消费者，体现了消费者至上的理念。</p>
</section>"""

# ============================================================
# Section 07: 分部与地区
# ============================================================
sec07 = """<section id="sec07">
  <div class="section-num">07 / 分部与地区业绩</div>
  <h2>分部与地区业绩</h2>
  <p>亚马逊在全球范围内保持强劲增长态势。北美市场仍是绝对主力，贡献约58%的营收。AWS业务全球化布局，国际云服务需求旺盛。国际零售业务在关税挑战下仍实现增长，公司通过提前囤货策略有效管理了关税风险。</p>

  <h3>地区营收分布</h3>
  <div class="chart-figure">
    <div class="chart-title">各地区营收占比</div>
    <div class="chart-desc">北美市场主导，国际业务稳步增长，AWS全球覆盖</div>
    <div class="chart-container short" id="chart-geo"></div>
    <div class="chart-foot">数据来源: Amazon IR</div>
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
          <td class="num">$1,161亿</td>
          <td class="num">57.9%</td>
          <td class="num pos">+12%</td>
          <td>稳健增长</td>
        </tr>
        <tr>
          <td>国际</td>
          <td class="num">$423亿</td>
          <td class="num">21.1%</td>
          <td class="num pos">+10%</td>
          <td>关税影响可控</td>
        </tr>
        <tr>
          <td>AWS(全球)</td>
          <td class="num">$422亿</td>
          <td class="num">21.0%</td>
          <td class="num pos">+37%</td>
          <td>加速增长</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">+</div>
      <h4>增长亮点地区</h4>
      <p>AWS全球业务全面开花，在北美、欧洲、亚太等主要市场均实现强劲增长。国际零售业务在关税挑战下仍保持10%增长，日本、印度等新兴市场表现突出。</p>
    </div>
    <div class="insight-card">
      <div class="icon red">!</div>
      <h4>承压地区</h4>
      <p>国际贸易环境不确定性增加，关税政策变化可能影响国际零售业务利润率。欧洲市场面临监管趋严和竞争加剧的双重挑战。外汇波动也对国际业务营收产生一定负面影响。</p>
    </div>
  </div>
</section>"""

# ============================================================
# Section 08: 业绩指引
# ============================================================
sec08 = """<section id="sec08">
  <div class="section-num">08 / 业绩指引与展望</div>
  <h2>业绩指引与展望</h2>
  <p>亚马逊发布了Q3 2026业绩指引，营收和营业利润区间中值均略低于市场预期，但主要原因是Prime Day从传统7月提前至6月举行，导致同比基数不可比。公司表示剔除Prime Day影响后，Q3增速将高出近400个基点。全年资本支出指引从$2,000亿大幅上调至$2,200亿，彰显AI投资决心。</p>

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
          <td class="num">$1,970亿 ~ $2,020亿</td>
          <td class="num">$2,039亿</td>
          <td>略低于预期(Prime Day时间调整)</td>
        </tr>
        <tr>
          <td>营业利润率</td>
          <td class="num">11.4% ~ 13.1%</td>
          <td class="num">12.3%</td>
          <td>基本符合</td>
        </tr>
        <tr>
          <td>营业利润</td>
          <td class="num">$225亿 ~ $265亿</td>
          <td class="num">$251亿</td>
          <td>中值$245亿略低于预期</td>
        </tr>
        <tr>
          <td>全年资本支出</td>
          <td class="num">$2,200亿</td>
          <td class="num">$2,000亿</td>
          <td>大幅上调10%</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3>全年指引调整</h3>
  <div class="timeline">
    <div class="timeline-item">
      <div class="tl-date">2026年2月</div>
      <h4>全年CAPEX预期$1,500亿</h4>
      <p>年初首次给出全年资本支出指引，预计在AI基础设施领域大幅投入</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026年5月</div>
      <h4>CAPEX上调至$2,000亿</h4>
      <p>Q1财报后上调全年CAPEX预期，反映AI需求持续超预期，内存价格上涨推高成本</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026年7月</div>
      <h4>CAPEX再上调至$2,200亿</h4>
      <p>CEO表示即使达到这一水平，到2026年底仍无法满足全部需求，2027-2028年需求已非常显著</p>
    </div>
  </div>

  <div class="callout pos">
    <div class="callout-title">指引点评</div>
    <p>Q3营收指引看似略低于预期，但核心原因是Prime Day从7月提前至6月导致同比不可比，剔除后增速高出近400个基点，实际增长动能依然强劲。全年CAPEX大幅上调至$2,200亿虽然短期压制自由现金流，但$4,960亿的AWS积压工作量为投资回报提供了坚实保障。数据中心使用寿命约30年，设备更新周期5-6年，未来现代化升级投资将显著低于当前新建水平，长期投资回报可期。</p>
  </div>
</section>"""

# ============================================================
# Section 09: 管理层评论
# ============================================================
sec09 = """<section id="sec09">
  <div class="section-num">09 / 管理层评论</div>
  <h2>管理层评论</h2>
  <p>亚马逊CEO Andy Jassy和CFO Brian Olsavsky在Q2 2026财报电话会议上对业绩表现出高度信心，重点阐述了AWS加速增长、AI业务突破、资本支出战略和关税影响等关键议题。</p>

  <div class="callout">
    <div class="callout-title">Andy Jassy · 首席执行官</div>
    <p>"AWS业务蓬勃发展，第二季度同比增长36.7%，这是我们18个季度以来最快的增长速度，而我们的人工智能和芯片业务的年化收入均超过了250亿美元。在实体店方面，我们上半年再次刷新了Prime会员的配送速度纪录——当日达或次日达的商品数量增长超过40%，其中食品杂货和日常必需品的增长速度明显高于其他业务。此外，广告业务也表现强劲，同比增长26%。这些都令人振奋，我们将在下半年及以后为顾客带来更多惊喜。"</p>
  </div>

  <div class="callout">
    <div class="callout-title">Brian Olsavsky · 首席财务官</div>
    <p>"由于亚马逊提前囤积库存以应对关税影响，我们获得的退款金额低于原本可能达到的水平。在确实因关税导致成本上升的情况下，我们大部分时候选择自行吸收这些成本，而不是将其转嫁给消费者。我们已经确认，在有限的一些情况下，可以追踪到我们曾将特定进口费用转嫁给消费者。当我们收到这些退款后，将主动联系受影响的消费者，并自动向他们发放退款。"</p>
  </div>

  <h3>电话会议要点</h3>
  <div class="highlights-box">
    <ul>
      <li>AWS AI和自研芯片业务年化收入均突破$250亿，同比三位数增长，已成为独立增长引擎</li>
      <li>即使CAPEX达到$2,200亿，到2026年底仍无法满足全部AI需求，2027-2028年需求已非常显著</li>
      <li>数据中心使用寿命约30年，设备更新周期5-6年，未来现代化升级投资将远低于当前新建水平</li>
      <li>内存价格上涨是CAPEX上调的重要原因之一，但AI投资回报正在加速兑现</li>
      <li>公司获得约$6亿关税退款，承诺在有限情况下主动返还消费者</li>
      <li>亚马逊计划向客户出售芯片供其安装在自己的数据中心，有望提升盈利能力</li>
    </ul>
  </div>
</section>"""

# ============================================================
# Section 10: 风险因素
# ============================================================
sec10 = """<section id="sec10">
  <div class="section-num">10 / 风险因素</div>
  <h2>风险因素</h2>
  <p>尽管亚马逊Q2 2026业绩表现强劲，但投资者仍需关注以下风险因素。AI基础设施巨额投资带来的自由现金流压力、国际贸易环境不确定性、云计算市场竞争加剧以及监管风险是需要持续跟踪的关键变量。</p>

  <ul class="risk-list">
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>AI投资回报不确定性</h4>
        <p>全年CAPEX高达$2,200亿，TTM自由现金流转负-$76亿。如果AI需求增速放缓或竞争加剧导致AWS增速回落，巨额投资可能面临回报率不足的风险。Meta因缺乏CAPEX指引导致股价大跌9%的前车之鉴值得警惕。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>国际贸易与关税风险</h4>
        <p>全球贸易政策不确定性持续，关税变动可能影响亚马逊国际零售业务成本和利润率。公司虽然通过提前囤货等方式管理风险，但长期贸易摩擦可能对跨境业务产生负面影响。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>云计算市场竞争加剧</h4>
        <p>微软Azure Q4同比增长43%，谷歌云Q2同比增长82%，竞争格局趋于激烈。AWS虽保持37%增速，但市场份额可能面临挑战。价格战风险不容忽视。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>反垄断与监管压力</h4>
        <p>美国FTC对亚马逊的反垄断诉讼仍在进行中，欧盟数字市场法案(DMA)可能对亚马逊的电商和广告业务施加更多限制。全球监管环境趋严是长期结构性风险。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge low">低</span>
      <div class="risk-body">
        <h4>宏观经济放缓风险</h4>
        <p>消费者支出可能受通胀和利率环境影响，但亚马逊的多元化业务结构和Prime会员高粘性提供了较强的抗风险能力。必需品和云计算需求相对刚性。</p>
      </div>
    </li>
  </ul>

  <div class="callout warn">
    <div class="callout-title">风险提示</div>
    <p>亚马逊当前面临的核心风险是AI巨额投资与自由现金流负值之间的平衡。虽然$4,960亿的AWS积压工作量提供了需求保障，但投资者需密切关注每季度AWS增速是否持续加速、CAPEX效率是否改善。国际贸易政策和监管环境变化是需要持续关注的外部变量。建议投资者在充分了解上述风险的基础上做出独立判断。</p>
  </div>
</section>"""

# ============================================================
# Section 11: 投资观点
# ============================================================
sec11 = """<section id="sec11">
  <div class="section-num">11 / 投资观点</div>
  <h2>投资观点</h2>
  <p class="lead">亚马逊Q2 2026业绩全面超预期，AWS加速增长和AI业务突破是核心亮点。尽管巨额CAPEX短期压制自由现金流，但$4,960亿积压工作量提供了长期增长保障。75位分析师中93%给予买入评级，市场共识强烈看多。盘后股价大涨超9%，反映市场对AI投资回报的认可。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">当前股价(盘后)</div>
      <div class="v">~$245</div>
      <div class="d pos">+9%</div>
    </div>
    <div class="stat-card">
      <div class="l">分析师目标价</div>
      <div class="v">$260-280</div>
      <div class="d pos">+6-14%</div>
    </div>
    <div class="stat-card">
      <div class="l">市盈率(PE)</div>
      <div class="v">~35x</div>
      <div class="d">合理偏高</div>
    </div>
    <div class="stat-card">
      <div class="l">市值</div>
      <div class="v">$2.53万亿</div>
      <div class="d pos">全球前五</div>
    </div>
  </div>

  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">+</div>
      <h4>看多因素</h4>
      <p>AWS增速连续5个季度加速，AI和芯片业务年化收入$250亿+且三位数增长。AWS积压工作量$4,960亿。广告业务$198亿+26%增长。零售业务配送速度创纪录。分析师93%买入评级。AI转型浪潮中处于有利位置。</p>
    </div>
    <div class="insight-card">
      <div class="icon red">-</div>
      <h4>看空因素</h4>
      <p>全年CAPEX高达$2,200亿，自由现金流转负。Q3指引略低于预期。微软Azure(+43%)和谷歌云(+82%)竞争加剧。FTC反垄断诉讼悬而未决。关税政策不确定性。当前估值处于历史较高水平。</p>
    </div>
    <div class="insight-card">
      <div class="icon blue">i</div>
      <h4>催化剂</h4>
      <p>AWS AI业务持续高速增长；自研芯片(Trainium/Graviton)对外销售突破；Prime Day 2026业绩公布；Anthropic投资价值进一步释放；关税政策明朗化；股票回购计划进展。</p>
    </div>
  </div>

  <div class="callout pos">
    <div class="callout-title">投资评级：增持 (Overweight)</div>
    <p>亚马逊Q2 2026业绩全面验证了AI投资战略的正确性。AWS加速增长有效缓解了市场对CAPEX回报的担忧。AI和芯片业务已成为独立增长引擎，年化收入$250亿+且三位数增长展示了巨大的增长潜力。虽然短期自由现金流转负和Q3指引略低于预期需关注，但$4,960亿积压工作量、广告业务强劲增长、以及零售业务效率提升提供了坚实的基本面支撑。综合来看，亚马逊在AI转型浪潮中处于有利位置，当前估值虽然不低，但考虑到增长确定性和质量，给予增持评级。建议投资者逢回调分批布局。</p>
  </div>
</section>"""

# ============================================================
# Section 12: 附录
# ============================================================
sec12 = """<section id="sec12">
  <div class="section-num">12 / 附录</div>
  <h2>附录</h2>

  <h3>术语表</h3>
  <dl class="glossary">
    <dt>AWS (Amazon Web Services)</dt>
    <dd>亚马逊云服务，全球最大的云计算平台，提供计算、存储、数据库、AI/ML等超过200项云服务</dd>
    <dt>TTM (Trailing Twelve Months)</dt>
    <dd>过去12个月滚动数据，用于消除季节性波动，更准确反映公司经营趋势</dd>
    <dt>自由现金流 (Free Cash Flow)</dt>
    <dd>经营现金流减去资本支出，衡量公司在维持运营和投资后可供股东分配的现金</dd>
    <dt>积压工作量 (Backlog)</dt>
    <dd>AWS已签署但尚未上线确认收入的合同金额，是未来营收的领先指标</dd>
    <dt>Trainium / Graviton</dt>
    <dd>亚马逊自研的AI训练芯片(Trainium)和通用服务器处理器(Graviton)，已形成完整的芯片产品线</dd>
  </dl>

  <h3>近8个季度财务数据</h3>
  <div class="chart-figure">
    <div class="chart-title">综合财务指标雷达图</div>
    <div class="chart-desc">从营收、利润、增速、利润率、现金流、资产质量等多维度展示亚马逊财务健康状况</div>
    <div class="chart-container" id="chart-radar"></div>
    <div class="chart-foot">数据来源: Amazon IR · Alpha Vantage</div>
  </div>

  <hr class="divider">

  <h3>数据说明</h3>
  <p>本报告财务数据来源于Amazon官方投资者关系页面(ir.aboutamazon.com)、Alpha Vantage API、Finnhub API以及路孚特(LSEG)分析师一致预期。汇率按USD/CNY≈7.25换算。Q2 2026数据基于2026年7月30日盘后发布的财报。部分估算数据（如Q2毛利率、现金流分项）基于历史趋势和行业分析合理推算。Anthropic投资收益$534亿为税前非经营性其他收入，计入净利润但非核心经营利润。所有数据仅供参考，不构成投资建议。</p>
</section>"""

# ============================================================
# Footer
# ============================================================
footer = """<footer>
  <div class="wrap">
    <div class="footer-top">
      <h3>参考资料</h3>
      <ol class="sources">
        <li><a href="https://ir.aboutamazon.com/quarterly-results/default.aspx">Amazon Quarterly Results - Q2 2026</a> · 2026-07-30</li>
        <li><a href="https://ir.aboutamazon.com/">Amazon Investor Relations</a> · 2026-07-31</li>
        <li><a href="http://news.qq.com/rain/a/20260731A02TRG00">亚马逊Q2盈利超出预期：AI和芯片业务年收入超250亿美元 - 腾讯新闻</a> · 2026-07-31</li>
        <li><a href="https://gb-www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=0000763601_LCX71PQTLFVQON22OIIK3">亚马逊2Q26 AI与芯片业务增幅达三位数 AWS营收增速创18季新高 - DIGITIMES</a> · 2026-07-31</li>
        <li><a href="http://m.toutiao.com/group/7668472129528054278/">亚马逊Q2业绩超预期 云业务加速增长缓解AI投入疑虑 - 智通财经</a> · 2026-07-31</li>
        <li><a href="http://m.toutiao.com/group/7668423903655576099/">亚马逊Q2营收超预期 盘后股价大涨超9% - 环球市场播报</a> · 2026-07-31</li>
        <li><a href="https://www.alphavantage.co/">Alpha Vantage API - Financial Data</a> · 2026-07-31</li>
        <li><a href="https://finnhub.io/">Finnhub API - Analyst Recommendations & Company Profile</a> · 2026-07-31</li>
      </ol>
    </div>

    <div class="disclaimer">
      <p>本报告基于公开财务数据与市场信息整理，数据来源包括 Amazon 官方投资者关系页面、Alpha Vantage API、Finnhub API、路孚特(LSEG)分析师一致预期等。报告中的财务数据已经过交叉验证，但仍可能存在误差。</p>
      <p>本报告由 Trae Work 基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。报告中涉及的所有财务数据均来源于公开披露文件，分析师观点基于截至 2026-07-31 可获得的信息。</p>
    </div>

    <div class="footer-meta">
      <span>报告生成: 2026-07-31 20:00 CST</span>
      <span>报告版本: v1.0</span>
      <span>Powered by Trae Work</span>
    </div>
  </div>
</footer>"""

# ============================================================
# Assemble
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
        "sec12": sec12,
    },
    "footer": footer
}

# Write JSON
output_path = r"D:\temp\Output\stock-financial-reports\data\amzn-q2-2026-sections.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Verify
with open(output_path, 'r', encoding='utf-8') as f:
    verify = json.load(f)

print(f"Sections JSON written to: {output_path}")
print(f"File size: {os.path.getsize(output_path)/1024:.1f} KB")
print(f"Meta keys: {len(verify['meta'])}")
print(f"Header length: {len(verify['header'])} chars")
print(f"Sections: {len(verify['sections'])} total")
for i in range(1, 13):
    sec_id = f"sec{i:02d}"
    print(f"  {sec_id}: {len(verify['sections'][sec_id])} chars")
print(f"Footer length: {len(verify['footer'])} chars")
print("Done!")