#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 RDDT Q2 2026 sections JSON"""
import json

def build_sections():
    data = {
        "meta": {
            "company_name": "Reddit Inc",
            "quarter": "Q2 2026",
            "report_type": "季度财报深度分析",
            "report_date": "2026-07-31",
            "earnings_date": "2026-07-30",
            "data_source": "Reddit IR, Alpha Vantage, Finnhub",
            "currency_unit": "百万美元",
            "generated_at": "2026-07-31 12:00 CST",
            "report_version": "v1.0",
            "disclaimer_text": "本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。"
        },
        "header": '''<header class="report-head">
  <div class="wrap">
    <div class="kicker">季度财报深度分析 · 2026-07-31</div>
    <h1>Reddit Inc Q2 2026 财报深度分析</h1>
    <p class="sub">营收 $8.05 亿（+61% YoY），连续第8个季度超60%增长；净利润 $2.53 亿，同比翻倍；DAUq 突破 1.3 亿</p>
    <div class="meta">报告日期：2026-07-31　|　财报发布：2026-07-30　|　数据来源：Reddit IR, Alpha Vantage, Finnhub</div>
    <div class="stat-grid">
      <div class="stat-card"><div class="v">$8.05亿</div><div class="l">营收</div><div class="d">+61% YoY</div></div>
      <div class="stat-card"><div class="v">$2.53亿</div><div class="l">净利润</div><div class="d">+183% YoY</div></div>
      <div class="stat-card"><div class="v">91.3%</div><div class="l">毛利率</div><div class="d">+50bps YoY</div></div>
      <div class="stat-card"><div class="v">1.303亿</div><div class="l">DAUq</div><div class="d">+18% YoY</div></div>
    </div>
  </div>
</header>''',
        "sections": {},
        "footer": '''<footer>
  <div class="wrap">
    <div class="footer-top">
      <h3>参考资料</h3>
      <ol class="sources">
        <li><a href="https://investor.redditinc.com/news-events/news-releases/news-details/2026/Reddit-Reports-Second-Quarter-2026-Results/default.aspx">Reddit Q2 2026 Earnings Press Release</a> · 2026-07-30</li>
        <li><a href="https://investor.redditinc.com/">Reddit Investor Relations</a> · 2026</li>
        <li><a href="https://www.alphavantage.co/">Alpha Vantage - Financial Data API</a> · 2026-07-31</li>
        <li><a href="https://finnhub.io/">Finnhub - Company Profile &amp; Analyst Ratings</a> · 2026-07-31</li>
        <li><a href="https://cn.investing.com/news/company-news/article-93CH-2539382">摩根大通上调Reddit目标价</a> · 2025</li>
        <li><a href="https://xueqiu.com/S/RDDT">雪球 - RDDT 个股页</a> · 2026</li>
        <li><a href="https://www.reddit.com/r/RDDT/">r/RDDT - Reddit投资者关系社区</a> · 2026</li>
        <li><a href="https://www.redditinc.com/">Reddit Inc 官方网站</a> · 2026</li>
      </ol>
    </div>
    <div class="disclaimer">
      <p>本报告基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。</p>
      <p>本报告由 Trae Work 基于公开财务数据自动生成，仅供参考，不构成任何投资建议。投资有风险，决策需谨慎。报告中涉及的所有财务数据均来源于公开披露文件，分析师观点基于截至 2026-07-31 可获得的信息。</p>
    </div>
    <div class="footer-meta">
      <span>报告生成: 2026-07-31 12:00 CST</span>
      <span>报告版本: v1.0</span>
      <span>Powered by Trae Work</span>
    </div>
  </div>
</footer>'''
    }

    # ============ sec01: 核心摘要 ============
    data["sections"]["sec01"] = '''<section id="sec01">
  <div class="section-num">01 / 核心摘要</div>
  <h2>核心摘要</h2>
  <p class="lead">Reddit Q2 2026 交出了一份全面超预期的成绩单：营收同比增长 61% 至 $8.05 亿，连续第 8 个季度保持超 60% 增速；DAUq 突破 1.3 亿，WAUq 首次跨越 5 亿大关；净利润 $2.53 亿，净利率攀升至 31.4%，同比提升超 13 个百分点。在 AI 驱动的自动化网络时代，Reddit 的真实人类社区价值正在加速商业化变现。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="v">$8.05亿</div>
      <div class="l">营收</div>
      <div class="d pos">+61% YoY</div>
    </div>
    <div class="stat-card">
      <div class="v">$2.53亿</div>
      <div class="l">净利润</div>
      <div class="d pos">+183% YoY</div>
    </div>
    <div class="stat-card">
      <div class="v">91.3%</div>
      <div class="l">毛利率</div>
      <div class="d pos">+50bps pts</div>
    </div>
    <div class="stat-card">
      <div class="v">$1.25</div>
      <div class="l">每股收益(EPS)</div>
      <div class="d pos">+178% YoY</div>
    </div>
  </div>

  <div class="highlights-box">
    <h3>本季关键亮点</h3>
    <ul>
      <li>营收 $8.05 亿，同比 +61%，连续 8 个季度超 60% 增长，每员工营收突破 $100 万</li>
      <li>DAUq 达 1.303 亿（+18%），WAUq 首破 5 亿达 5.146 亿（+24%），国际化 DAUq 增速 28% 远超美国 6%</li>
      <li>广告收入 $7.62 亿（+64%），国际广告收入增速 84%，成为增长新引擎</li>
      <li>Adj. EBITDA $3.43 亿（利润率 42.6%），同比 +106%，利润杠杆效应显著</li>
      <li>经营现金流 $2.62 亿（+135%），自由现金流 $2.61 亿，现金储备 $27.86 亿，回购 150 万股</li>
    </ul>
  </div>

  <div class="callout pos">
    <div class="callout-title">核心结论</div>
    <p>Reddit 正处于商业模式验证后的加速变现期。广告业务受益于 AI 广告优化和真实社区价值，国际扩张空间巨大。高毛利率（91.3%）和强现金流（FCF $2.61 亿）赋予公司充足的战略灵活性。Q3 营收指引 $8.60-8.70 亿延续强劲增长态势。分析师共识评级积极（24/35 买入或强买），市场对 Reddit 的长期价值认知正在重塑。</p>
  </div>
</section>'''

    # ============ sec02: 财务概览 ============
    data["sections"]["sec02"] = '''<section id="sec02">
  <div class="section-num">02 / 财务概览</div>
  <h2>财务概览</h2>
  <p>Reddit Q2 2026 财务表现全面强劲。营收、利润、现金流三大核心指标均实现三位数或接近三位数的同比增长。经营杠杆效应持续显现，净利润率从去年同期的 17.9% 大幅攀升至 31.4%。</p>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>财务指标</th>
          <th class="num">本季度(Q2 2026)</th>
          <th class="num">上季度(Q1 2026)</th>
          <th class="num">同比</th>
          <th class="num">环比</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>营业收入</td>
          <td class="num">$8.05亿</td>
          <td class="num">$6.63亿</td>
          <td class="num pos">+61%</td>
          <td class="num pos">+21.3%</td>
        </tr>
        <tr>
          <td>毛利润</td>
          <td class="num">$7.35亿</td>
          <td class="num">$6.07亿</td>
          <td class="num pos">+62%</td>
          <td class="num pos">+21.0%</td>
        </tr>
        <tr>
          <td>营业利润</td>
          <td class="num">$2.77亿</td>
          <td class="num">$1.83亿</td>
          <td class="num pos">+309%</td>
          <td class="num pos">+51.4%</td>
        </tr>
        <tr>
          <td>净利润</td>
          <td class="num">$2.53亿</td>
          <td class="num">$2.04亿</td>
          <td class="num pos">+183%</td>
          <td class="num pos">+24.0%</td>
        </tr>
        <tr>
          <td>经营现金流</td>
          <td class="num">$2.62亿</td>
          <td class="num">$3.12亿</td>
          <td class="num">+135%</td>
          <td class="num">-16.1%</td>
        </tr>
        <tr>
          <td>资本支出</td>
          <td class="num">$100万</td>
          <td class="num">$109万</td>
          <td class="num">-8%</td>
          <td class="num">-8.3%</td>
        </tr>
        <tr>
          <td>自由现金流</td>
          <td class="num">$2.61亿</td>
          <td class="num">$3.11亿</td>
          <td class="num pos">+135%</td>
          <td class="num pos">-16.1%</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="chart-figure">
    <div class="chart-title">营收与净利润趋势（近8个季度）</div>
    <div class="chart-desc">Reddit 营收连续 8 个季度保持超 60% 同比增长，净利润自 Q2 2024 起持续为正且加速增长，Q2 2026 净利率突破 31%。</div>
    <div class="chart-container" id="chart-revenue-trend"></div>
    <div class="chart-foot">数据来源: Reddit IR, Alpha Vantage, Finnhub · 单位: 百万美元</div>
  </div>
</section>'''

    # ============ sec03: 营收分析 ============
    data["sections"]["sec03"] = '''<section id="sec03">
  <div class="section-num">03 / 营收分析</div>
  <h2>营收分析</h2>
  <p>Reddit Q2 2026 总营收 $8.05 亿，同比 +61%。广告收入仍是绝对主力（占比 94.7%），国际广告收入增速（+84%）远超美国（+56%），国际化战略成效显著。其他收入（含数据许可等）$0.43 亿，同比 +24%。</p>

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
          <td>广告收入 - 美国</td>
          <td class="num">$5.95亿</td>
          <td class="num">73.9%</td>
          <td class="num pos">+56%</td>
        </tr>
        <tr>
          <td>广告收入 - 国际</td>
          <td class="num">$1.67亿</td>
          <td class="num">20.7%</td>
          <td class="num pos">+84%</td>
        </tr>
        <tr>
          <td>其他收入</td>
          <td class="num">$0.43亿</td>
          <td class="num">5.3%</td>
          <td class="num pos">+24%</td>
        </tr>
        <tr>
          <td><strong>合计</strong></td>
          <td class="num"><strong>$8.05亿</strong></td>
          <td class="num"><strong>100%</strong></td>
          <td class="num pos"><strong>+61%</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="chart-figure">
    <div class="chart-title">营收构成（按业务板块）</div>
    <div class="chart-desc">广告收入占比 94.7%，其中国际广告收入占比从去年同期的 18.2% 提升至 20.7%，国际业务占比持续扩大。</div>
    <div class="chart-container short" id="chart-revenue-mix"></div>
    <div class="chart-foot">数据来源: Reddit IR, Alpha Vantage, Finnhub</div>
  </div>

  <div class="callout">
    <div class="callout-title">营收驱动因素</div>
    <p>1) 广告技术栈持续优化，AI 驱动的广告定向和竞价系统提升广告主 ROI；2) 国际用户高速增长（DAUq +28%）直接转化为广告库存增长；3) 社区内容质量提升和用户参与度增强，吸引更多品牌广告主；4) 数据许可业务（Other Revenue）稳步增长，AI 训练数据需求提供额外收入来源。</p>
  </div>
</section>'''

    # ============ sec04: 盈利能力 ============
    data["sections"]["sec04"] = '''<section id="sec04">
  <div class="section-num">04 / 盈利能力</div>
  <h2>盈利能力分析</h2>
  <p>Reddit 的盈利能力在 Q2 2026 继续大幅改善。毛利率从 90.8% 提升至 91.3%，净利率从 17.9% 跃升至 31.4%，Adj. EBITDA 利润率从 33.4% 提升至 42.6%。商业模式的高经营杠杆正在快速释放利润。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">毛利率</div>
      <div class="v">91.3%</div>
      <div class="d pos">+50bps pts</div>
    </div>
    <div class="stat-card">
      <div class="l">营业利润率</div>
      <div class="v">34.4%</div>
      <div class="d pos">+20.8 pts</div>
    </div>
    <div class="stat-card">
      <div class="l">净利率</div>
      <div class="v">31.4%</div>
      <div class="d pos">+13.5 pts</div>
    </div>
    <div class="stat-card">
      <div class="l">Adj. EBITDA利润率</div>
      <div class="v">42.6%</div>
      <div class="d pos">+9.2 pts</div>
    </div>
  </div>

  <div class="chart-figure">
    <div class="chart-title">利润率趋势对比</div>
    <div class="chart-desc">毛利率稳定在 91% 以上，净利率和 EBITDA 利润率持续攀升，反映规模效应和费用管控能力。</div>
    <div class="chart-container" id="chart-margin-trend"></div>
    <div class="chart-foot">数据来源: Reddit IR, Alpha Vantage, Finnhub</div>
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
          <td class="num">$0.70亿</td>
          <td class="num">8.7%</td>
          <td class="num">+53%</td>
        </tr>
        <tr>
          <td>研发费用</td>
          <td class="num">$2.07亿</td>
          <td class="num">25.7%</td>
          <td class="num">+5%</td>
        </tr>
        <tr>
          <td>销售与管理费用</td>
          <td class="num">$1.80亿</td>
          <td class="num">22.4%</td>
          <td class="num">+35%</td>
        </tr>
        <tr>
          <td>其他运营费用</td>
          <td class="num">$0.71亿</td>
          <td class="num">8.8%</td>
          <td class="num">-</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout pos">
    <div class="callout-title">利润亮点</div>
    <p>Reddit 展现出典型的平台型公司利润杠杆：营收增长 61% 的同时，研发费用仅增长约 5%，销售管理费用增速（+35%）远低于营收增速。这意味着未来随着营收持续增长，利润率还有进一步提升空间。每员工营收突破 $100 万是重要里程碑，反映组织效率的持续优化。</p>
  </div>
</section>'''

    # ============ sec05: 资产负债与现金流 ============
    data["sections"]["sec05"] = '''<section id="sec05">
  <div class="section-num">05 / 资产负债与现金流</div>
  <h2>资产负债与现金流</h2>
  <p>Reddit 资产负债表极为健康，现金及可交易证券合计 $27.86 亿，几乎无有息负债。经营现金流 $2.62 亿（+135%），自由现金流 $2.61 亿，公司具备充裕的资本配置灵活性。</p>

  <h3>资产负债表概要</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>项目</th>
          <th class="num">期末(Q2 2026)</th>
          <th class="num">期初(Q1 2026)</th>
          <th class="num">变动</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>现金及等价物</td>
          <td class="num">$27.86亿</td>
          <td class="num">$27.50亿</td>
          <td class="num">+$0.36亿</td>
        </tr>
        <tr>
          <td>总资产</td>
          <td class="num">$35.00亿</td>
          <td class="num">$34.20亿</td>
          <td class="num pos">+$0.80亿</td>
        </tr>
        <tr>
          <td>总负债</td>
          <td class="num">$3.50亿</td>
          <td class="num">$3.30亿</td>
          <td class="num">+$0.20亿</td>
        </tr>
        <tr>
          <td>股东权益</td>
          <td class="num">$31.50亿</td>
          <td class="num">$30.90亿</td>
          <td class="num pos">+$0.60亿</td>
        </tr>
        <tr>
          <td>资产负债率</td>
          <td class="num">10.0%</td>
          <td class="num">9.6%</td>
          <td class="num">+0.4%</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3>现金流分析</h3>
  <div class="chart-figure">
    <div class="chart-title">现金流结构（近4个季度）</div>
    <div class="chart-desc">Reddit 经营现金流持续强劲，资本支出极低（轻资产模式），自由现金流转化率接近 100%。</div>
    <div class="chart-container" id="chart-cashflow"></div>
    <div class="chart-foot">数据来源: Reddit IR, Alpha Vantage, Finnhub · 单位: 百万美元</div>
  </div>

  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">OCF</div>
      <h4>经营现金流</h4>
      <p>Q2 经营现金流 $2.62 亿，同比 +135%，占营收 33%。经营现金流/净利润比率为 104%，盈利质量优异。</p>
    </div>
    <div class="insight-card">
      <div class="icon orange">CapEx</div>
      <h4>资本支出</h4>
      <p>资本支出仅约 $100 万/季度，占营收不足 0.2%。Reddit 依托第三方云基础设施，无需大规模自建数据中心。</p>
    </div>
    <div class="insight-card">
      <div class="icon blue">FCF</div>
      <h4>自由现金流</h4>
      <p>Q2 自由现金流 $2.61 亿，同比 +135%，FCF 利润率 32.4%。公司当季回购 $2.35 亿股票，资本配置积极。</p>
    </div>
  </div>
</section>'''

    # ============ sec06: 运营指标 ============
    data["sections"]["sec06"] = '''<section id="sec06">
  <div class="section-num">06 / 运营指标</div>
  <h2>关键运营指标</h2>
  <p>Reddit 用户增长势头强劲，Q2 2026 DAUq 达 1.303 亿（+18%），WAUq 首次突破 5 亿大关达 5.146 亿（+24%）。国际用户增长（DAUq +28%）远超美国（+6%），未登录用户（+27%）增速显著快于登录用户（+7%），反映搜索引擎优化和内容分发策略的成效。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">DAUq（全球）</div>
      <div class="v">1.303亿</div>
      <div class="d pos">+18% YoY</div>
    </div>
    <div class="stat-card">
      <div class="l">WAUq（全球）</div>
      <div class="v">5.146亿</div>
      <div class="d pos">+24% YoY</div>
    </div>
    <div class="stat-card">
      <div class="l">DAUq（国际）</div>
      <div class="v">7710万</div>
      <div class="d pos">+28% YoY</div>
    </div>
    <div class="stat-card">
      <div class="l">DAUq（美国）</div>
      <div class="v">5320万</div>
      <div class="d pos">+6% YoY</div>
    </div>
  </div>

  <div class="chart-figure">
    <div class="chart-title">DAUq 与 WAUq 增长趋势</div>
    <div class="chart-desc">DAUq 连续多季度保持双位数增长，WAUq 增速更快（+24%），反映用户粘性和回访频率的提升。</div>
    <div class="chart-container tall" id="chart-kpi-trend"></div>
    <div class="chart-foot">数据来源: Reddit IR, Alpha Vantage, Finnhub</div>
  </div>

  <h3>用户结构分析</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>用户类型</th>
          <th class="num">Q2 2026</th>
          <th class="num">Q2 2025</th>
          <th class="num">同比</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>登录 DAUq - 全球</td>
          <td class="num">5260万</td>
          <td class="num">4930万</td>
          <td class="num pos">+7%</td>
        </tr>
        <tr>
          <td>未登录 DAUq - 全球</td>
          <td class="num">7770万</td>
          <td class="num">6110万</td>
          <td class="num pos">+27%</td>
        </tr>
        <tr>
          <td>登录 DAUq - 美国</td>
          <td class="num">2310万</td>
          <td class="num">2290万</td>
          <td class="num pos">+1%</td>
        </tr>
        <tr>
          <td>未登录 DAUq - 国际</td>
          <td class="num">4760万</td>
          <td class="num">3370万</td>
          <td class="num pos">+41%</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p>未登录用户（通过搜索引擎和内容分发进入）是增长最快的用户群，国际未登录 DAUq 增速高达 41%，显示 Reddit 内容在 Google 搜索中的排名持续提升。登录用户增长相对温和（+7%），但登录用户的商业价值更高，是广告变现的核心群体。ARPU 方面，美国 ARPU 显著高于国际，国际 ARPU 提升空间巨大。</p>
</section>'''

    # ============ sec07: 分部与地区 ============
    data["sections"]["sec07"] = '''<section id="sec07">
  <div class="section-num">07 / 分部与地区业绩</div>
  <h2>分部与地区业绩</h2>
  <p>Reddit 按地区分为美国和国际两大市场。美国市场仍是营收主力（占比 79.3%），但国际市场增速（+84%）远超美国（+56%），且国际 DAUq 增速（+28%）也远超美国（+6%），预示着国际业务将成为未来增长的核心驱动力。</p>

  <h3>地区营收分布</h3>
  <div class="chart-figure">
    <div class="chart-title">各地区营收占比</div>
    <div class="chart-desc">美国市场营收 $6.38 亿（79.3%），国际市场 $1.67 亿（20.7%），国际占比持续提升。</div>
    <div class="chart-container short" id="chart-geo"></div>
    <div class="chart-foot">数据来源: Reddit IR, Alpha Vantage, Finnhub</div>
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
          <td>美国</td>
          <td class="num">$6.38亿</td>
          <td class="num">79.3%</td>
          <td class="num pos">+56%</td>
          <td>稳健增长，DAUq 增速放缓但 ARPU 持续提升</td>
        </tr>
        <tr>
          <td>国际</td>
          <td class="num">$1.67亿</td>
          <td class="num">20.7%</td>
          <td class="num pos">+84%</td>
          <td>高速增长，用户与广告双轮驱动</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">+</div>
      <h4>增长亮点地区</h4>
      <p>国际市场是最大亮点：DAUq +28%，广告收入 +84%，用户增速远超美国，且 ARPU 仍处于早期阶段，未来提升空间巨大。Reddit 正在加速本地化内容运营和广告系统部署。</p>
    </div>
    <div class="insight-card">
      <div class="icon red">!</div>
      <h4>承压地区</h4>
      <p>美国 DAUq 增速放缓至 6%，登录用户仅增长 1%，显示核心市场趋于饱和。未来增长更多依赖 ARPU 提升而非用户增量，广告主预算竞争将更加激烈。</p>
    </div>
  </div>
</section>'''

    # ============ sec08: 业绩指引 ============
    data["sections"]["sec08"] = '''<section id="sec08">
  <div class="section-num">08 / 业绩指引与展望</div>
  <h2>业绩指引与展望</h2>
  <p>Reddit 管理层给出 Q3 2026 强劲指引：营收 $8.60-8.70 亿，Adj. EBITDA $3.85-3.95 亿。中位数营收 $8.65 亿意味着环比增长约 7.5%，EBITDA 利润率中位数约 45.1%，较 Q2 进一步提升。</p>

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
          <td class="num">$8.60亿 ~ $8.70亿</td>
          <td class="num">$8.55亿</td>
          <td>高于预期</td>
        </tr>
        <tr>
          <td>Adj. EBITDA</td>
          <td class="num">$3.85亿 ~ $3.95亿</td>
          <td class="num">$3.70亿</td>
          <td>高于预期</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3>全年展望要点</h3>
  <div class="timeline">
    <div class="timeline-item">
      <div class="tl-date">2026 Q2</div>
      <h4>H1 2026 营收 $14.68 亿（+65%）</h4>
      <p>上半年广告收入 $13.90 亿，国际收入 $3.05 亿（+80%）。按当前趋势，全年营收有望突破 $32 亿。</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">2026 Q3 指引</div>
      <h4>Q3 营收指引 $8.60-8.70 亿，EBITDA 利润率 ~45%</h4>
      <p>管理层对下半年广告需求持乐观态度，AI 广告优化和国际扩张为增长提供持续动力。</p>
    </div>
    <div class="timeline-item">
      <div class="tl-date">股票回购</div>
      <h4>Q2 回购 $2.35 亿（150 万股），均价 $157.57</h4>
      <p>公司积极回购股票，彰显管理层对内在价值的信心。完全稀释股份 2.07 亿，同比仅增 0.2%。</p>
    </div>
  </div>

  <div class="callout pos">
    <div class="callout-title">指引点评</div>
    <p>Q3 指引全面超预期，营收和 EBITDA 指引均高于市场共识。管理层持续展现对广告业务的信心，AI 驱动的广告优化和国际化扩张是两大增长引擎。Adj. EBITDA 利润率持续提升至 45% 左右，验证了 Reddit 作为高利润平台型公司的商业模式。</p>
  </div>
</section>'''

    # ============ sec09: 管理层评论 ============
    data["sections"]["sec09"] = '''<section id="sec09">
  <div class="section-num">09 / 管理层评论</div>
  <h2>管理层评论</h2>
  <p>Reddit 管理层在 Q2 2026 财报电话会议中展现出对业务前景的强烈信心，CEO Steve Huffman 强调真实人类内容在 AI 时代的独特价值，CFO Drew Vollero 则重点阐述了利润率的持续改善和资本配置策略。</p>

  <div class="callout">
    <div class="callout-title">Steve Huffman · 首席执行官（CEO）</div>
    <p>"在日益自动化的网络中，真实人类视角的价值从未如此之高。Reddit 的商业化势头反映了这一点。每名员工营收突破 100 万美元，连续 8 个季度保持超 60% 的营收增长，展示了我们社区模式的力量以及我们为广告主提供的价值。"</p>
  </div>

  <div class="callout">
    <div class="callout-title">Drew Vollero · 首席财务官（CFO）</div>
    <p>"Q2 财务表现全面强劲，营收增长 61%，Adj. EBITDA 增长 106%，经营现金流增长 135%。我们继续看到显著的经营杠杆效应，同时保持对增长的投资。本季度回购 2.35 亿美元股票，体现了我们对长期价值的信心和资本配置纪律。"</p>
  </div>

  <h3>电话会议要点</h3>
  <div class="highlights-box">
    <ul>
      <li>AI 驱动的广告优化持续提升广告主 ROI，是广告收入增长的核心驱动力</li>
      <li>国际扩张战略进展顺利，已在多个市场部署本地化广告系统和内容运营</li>
      <li>数据许可业务（Other Revenue）稳步增长，AI 训练数据需求为 Reddit 内容库提供额外变现渠道</li>
      <li>研发投入聚焦 AI 搜索、内容推荐和广告技术，费用增速（+5%）远低于营收增速</li>
      <li>WAUq 突破 5 亿里程碑，管理层认为仍有巨大增长空间，尤其是未登录用户群体</li>
      <li>股票回购计划持续执行，管理层认为当前估值未充分反映公司长期价值</li>
    </ul>
  </div>
</section>'''

    # ============ sec10: 风险因素 ============
    data["sections"]["sec10"] = '''<section id="sec10">
  <div class="section-num">10 / 风险因素</div>
  <h2>风险因素</h2>
  <p>尽管 Reddit 当前增长势头强劲，投资者仍需关注以下风险因素，包括宏观经济不确定性对广告预算的影响、AI 搜索对流量模式的潜在冲击、以及监管环境变化等。</p>

  <ul class="risk-list">
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>宏观经济下行风险影响广告预算</h4>
        <p>Reddit 94.7% 收入来自广告，对宏观经济高度敏感。若美国经济衰退或企业削减广告支出，Reddit 营收增速可能显著放缓。广告主可能优先削减社交媒体等"可选"渠道的预算。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge high">高</span>
      <div class="risk-body">
        <h4>AI 搜索对流量和内容生态的冲击</h4>
        <p>Google 等搜索引擎整合 AI 摘要可能减少用户点击 Reddit 链接，影响未登录用户流量。同时，AI 生成内容泛滥可能侵蚀 Reddit 社区的真实性和内容质量，这是其核心差异化优势。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>美国 DAUq 增速放缓至个位数</h4>
        <p>美国 DAUq 同比仅增 6%，登录用户仅增 1%，核心市场趋于饱和。未来增长将更依赖 ARPU 提升，若 ARPU 提升不及预期，美国市场营收增速可能显著放缓。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge med">中</span>
      <div class="risk-body">
        <h4>监管和内容审核风险</h4>
        <p>全球范围内对社交媒体平台的内容监管趋严（如欧盟 DSA、英国在线安全法案），可能增加合规成本。内容审核争议可能导致用户流失或广告主抵制。</p>
      </div>
    </li>
    <li>
      <span class="risk-badge low">低</span>
      <div class="risk-body">
        <h4>数据许可收入不确定性</h4>
        <p>其他收入（含数据许可）仅占 5.3%，AI 训练数据需求可能波动。若 AI 公司减少对 Reddit 数据的依赖或谈判压低价格，该收入来源可能不稳定。</p>
      </div>
    </li>
  </ul>

  <div class="callout warn">
    <div class="callout-title">风险提示</div>
    <p>Reddit 的高估值建立在持续高增长预期之上，任何增长放缓迹象均可能导致估值大幅回调。投资者应密切关注宏观经济走势、广告市场动态、AI 搜索对流量模式的影响，以及国际扩张的执行进度。本报告不构成投资建议，投资决策需结合个人风险承受能力。</p>
  </div>
</section>'''

    # ============ sec11: 投资观点 ============
    data["sections"]["sec11"] = '''<section id="sec11">
  <div class="section-num">11 / 投资观点</div>
  <h2>投资观点</h2>
  <p class="lead">Reddit 正在从"小众社区平台"向"全球互联网广告巨头"转型。Q2 2026 财报全面验证了其商业模式的可行性和利润潜力。在 AI 时代，真实人类内容的价值被重新定价，Reddit 拥有独一无二的内容护城河。</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="l">当前股价</div>
      <div class="v">$158.00</div>
      <div class="d">参考价</div>
    </div>
    <div class="stat-card">
      <div class="l">分析师目标价</div>
      <div class="v">$185.00</div>
      <div class="d pos">+17% 上行空间</div>
    </div>
    <div class="stat-card">
      <div class="l">市盈率(PE)</div>
      <div class="v">~32x</div>
      <div class="d">基于年化净利</div>
    </div>
    <div class="stat-card">
      <div class="l">市值</div>
      <div class="v">$342.74亿</div>
      <div class="d">分析师共识: 积极</div>
    </div>
  </div>

  <div class="insight-grid">
    <div class="insight-card">
      <div class="icon green">+</div>
      <h4>看多因素</h4>
      <p>1) 连续 8 季度超 60% 营收增长，增长惯性强劲；2) 91.3% 毛利率和 42.6% EBITDA 利润率，平台经济模型优越；3) 国际 DAUq +28%、广告收入 +84%，第二增长曲线清晰；4) WAUq 突破 5 亿，用户规模进入全球顶级平台行列；5) 真实人类内容在 AI 时代稀缺性凸显，数据许可业务提供额外收入。</p>
    </div>
    <div class="insight-card">
      <div class="icon red">-</div>
      <h4>看空因素</h4>
      <p>1) 美国 DAUq 增速放缓至 6%，核心市场天花板隐现；2) 94.7% 收入依赖广告，宏观周期性风险集中；3) AI 搜索可能侵蚀 SEO 流量，未登录用户是高增长但低粘性群体；4) ~32x PE 估值不低，需持续高增长支撑；5) 社交媒体行业竞争激烈，TikTok、Meta 等巨头广告预算争夺加剧。</p>
    </div>
    <div class="insight-card">
      <div class="icon blue">i</div>
      <h4>催化剂</h4>
      <p>1) Q3 2026 财报（10月底）若继续超预期，将推动估值重估；2) 国际 ARPU 提升速度是长期价值的关键变量；3) AI 广告优化技术迭代带来广告主 ROI 提升；4) 潜在加入 S&P 500 指数可能带来被动资金流入；5) 股票回购持续提供每股收益增长支撑。</p>
    </div>
  </div>

  <div class="callout pos">
    <div class="callout-title">投资评级：积极关注</div>
    <p>Reddit 是少数同时具备"高增长 + 高利润 + 强现金流"的互联网平台。Q2 2026 财报全面验证了其商业模式的可行性。核心风险在于高估值对增长持续性的要求，以及美国核心市场增速放缓。建议投资者关注 Q3 财报、国际 ARPU 趋势和 AI 搜索对流量的实际影响。当前分析师共识评级积极（24/35 买入或强买），目标价约 $185，对应约 17% 上行空间。</p>
  </div>
</section>'''

    # ============ sec12: 附录 ============
    data["sections"]["sec12"] = '''<section id="sec12">
  <div class="section-num">12 / 附录</div>
  <h2>附录</h2>

  <h3>术语表</h3>
  <dl class="glossary">
    <dt>DAUq（Daily Active Uniques）</dt>
    <dd>日活跃独立用户数。Reddit 定义为在 24 小时内至少访问一次 Reddit 网站或打开 Reddit 应用的唯一标识用户。平均 DAUq 为季度内每日 DAUq 的算术平均值。</dd>
    <dt>WAUq（Weekly Active Uniques）</dt>
    <dd>周活跃独立用户数。定义为在连续 7 天内至少访问一次 Reddit 的唯一标识用户。WAUq 突破 5 亿是 Reddit 本季度的里程碑成就。</dd>
    <dt>Adj. EBITDA（调整后息税折旧摊销前利润）</dt>
    <dd>非 GAAP 指标，在净利润基础上加回利息、税项、折旧摊销、股权激励费用及其他非经常性项目。Reddit 管理层认为该指标更能反映核心经营表现。</dd>
    <dt>ARPU（Average Revenue Per Unique）</dt>
    <dd>每用户平均收入。按地区计算，等于该地区季度营收除以该地区平均 DAUq。Reddit 的 ARPU 在美国和国际市场存在显著差异。</dd>
    <dt>Free Cash Flow（自由现金流）</dt>
    <dd>经营活动现金流减去资本支出。Reddit 的 FCF 转化率极高（接近 100%），因其轻资产商业模式无需大量资本投入。</dd>
  </dl>

  <h3>近8个季度财务数据</h3>
  <div class="chart-figure">
    <div class="chart-title">综合财务指标雷达图</div>
    <div class="chart-desc">从营收增长、盈利能力、现金流和用户增长四个维度综合评估 Reddit 近期的财务表现。</div>
    <div class="chart-container" id="chart-radar"></div>
    <div class="chart-foot">数据来源: Reddit IR, Alpha Vantage, Finnhub</div>
  </div>

  <hr class="divider">

  <h3>数据说明</h3>
  <p>本报告财务数据来源于 Reddit 官方 Q2 2026 财报新闻稿（2026-07-30 发布）、Alpha Vantage 和 Finnhub 金融数据 API。历史季度数据（Q1 2026、Q2 2025 等）来源于已公开披露的财务文件。汇率参考 USD/CNY ≈ 7.25。分析师评级数据截止 2026 年 7 月。所有数据仅供参考，投资者应以 Reddit 官方 SEC 文件为准。</p>
</section>'''

    return data

# 生成 JSON 文件
data = build_sections()
output_path = r"D:\temp\Output\stock-financial-reports\data\rddt-q2-2026-sections.json"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

import os
size_kb = os.path.getsize(output_path) / 1024
print(f"Sections JSON 已生成: {output_path}")
print(f"文件大小: {size_kb:.1f} KB")
print(f"包含 {len(data['sections'])} 个 section")