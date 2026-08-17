/**
 * SNDK Q4 FY2026 财报图表 (ECharts SVG 渲染 / 无动画 / 响应式)
 * 7 个固定图表：chart-revenue-trend / chart-revenue-mix / chart-margin-trend /
 * chart-cashflow / chart-kpi-trend / chart-geo / chart-radar
 */
(function () {
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
    neutral: cssVar('--muted', '#6e6e73'),
    text: cssVar('--ink', '#1d1d1f'),
    textMuted: cssVar('--muted', '#6e6e73'),
    grid: cssVar('--rule', '#d2d2d7'),
    surface: cssVar('--bg2', '#ffffff'),
    series1: '#0071e3', series2: '#34c759', series3: '#af52de',
    series4: '#ff9500', series5: '#ff375f'
  };
  var isMobile = window.innerWidth <= 700;
  function fs(base) { return isMobile ? Math.round(base * 0.86) : base; }
  function makeGrid() {
    return isMobile
      ? { left: 38, right: 16, top: 34, bottom: 58, containLabel: true }
      : { left: 56, right: 28, top: 42, bottom: 48, containLabel: true };
  }
  function axisLabel() { return { color: palette.textMuted, fontSize: fs(12) }; }
  function makeChart(el) { return echarts.init(el, null, { renderer: 'svg' }); }
  function render(el, option) {
    if (!el) return null;
    var chart = makeChart(el);
    chart.setOption(option);
    window.addEventListener('resize', function () { chart.resize(); });
    return chart;
  }

  // 1. chart-revenue-trend: 营收与净利润趋势（近8季度，双柱+折线）
  function initRevenueTrend() {
    var el = document.getElementById('chart-revenue-trend');
    if (!el) return;
    var quarters = ['FY25Q1', 'FY25Q2', 'FY25Q3', 'FY25Q4', 'FY26Q1', 'FY26Q2', 'FY26Q3', 'FY26Q4'];
    var revenue = [15.2, 16.8, 17.5, 19.01, 23.15, 30.25, 59.4, 89.7];
    var netIncome = [-2.5, -1.8, -1.2, 0.5, 3.2, 8.03, 28.5, 69];
    var option = {
      animation: false,
      color: [palette.series1, palette.negative],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: {
        type: 'category', data: quarters,
        axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0, interval: 0 }),
        axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false }
      },
      yAxis: [
        { type: 'value', name: '亿美元', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: palette.grid } } },
        { type: 'value', name: '净利润', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { show: false } }
      ],
      series: [
        { name: '营收', type: 'bar', yAxisIndex: 0, data: revenue, barMaxWidth: isMobile ? 18 : 30, itemStyle: { color: palette.series1, borderRadius: [3, 3, 0, 0] } },
        { name: '净利润', type: 'line', yAxisIndex: 1, data: netIncome, smooth: false, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: palette.series5 }, itemStyle: { color: palette.series5 } }
      ]
    };
    render(el, option);
  }

  // 2. chart-revenue-mix: 营收构成（环形饼图）
  function initRevenueMix() {
    var el = document.getElementById('chart-revenue-mix');
    if (!el) return;
    var data = [
      { name: '企业级/数据中心SSD', value: 60.0 },
      { name: '消费级NAND/SSD', value: 19.7 },
      { name: '移动/嵌入式', value: 7.2 },
      { name: '其他', value: 2.8 }
    ];
    var pieColors = [palette.series1, palette.series2, palette.series4, palette.neutral];
    var legendConf = isMobile
      ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: palette.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var option = {
      animation: false, color: pieColors, legend: legendConf,
      tooltip: { trigger: 'item', formatter: '{b}: {c}亿美元 ({d}%)' },
      series: [{
        type: 'pie', radius: isMobile ? ['38%', '62%'] : ['52%', '72%'], center: isMobile ? ['50%', '42%'] : ['38%', '50%'],
        avoidLabelOverlap: true, itemStyle: { borderColor: palette.surface, borderWidth: 2 },
        label: { show: !isMobile, color: palette.text, fontSize: fs(12), formatter: '{d}%' },
        labelLine: { show: !isMobile }, data: data
      }]
    };
    render(el, option);
  }

  // 3. chart-margin-trend: 利润率趋势（多折线）
  function initMarginTrend() {
    var el = document.getElementById('chart-margin-trend');
    if (!el) return;
    var quarters = ['FY25Q1', 'FY25Q2', 'FY25Q3', 'FY25Q4', 'FY26Q1', 'FY26Q2', 'FY26Q3', 'FY26Q4'];
    var gm = [12, 18, 22, 28, 35, 48, 68, 84.6];
    var om = [-5, 2, 8, 15, 22, 35, 55, 66.7];
    var nm = [-16, -11, -7, 3, 14, 27, 48, 76.9];
    var option = {
      animation: false,
      color: [palette.series1, palette.series2, palette.series5],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis' },
      xAxis: {
        type: 'category', data: quarters,
        axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0, interval: 0 }),
        axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false }
      },
      yAxis: { type: 'value', name: '%', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, axisLabel: Object.assign({}, axisLabel(), { formatter: '{value}%' }), splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '毛利率', type: 'line', data: gm, smooth: false, symbol: 'circle', symbolSize: isMobile ? 5 : 7, lineStyle: { width: 2 } },
        { name: '营业利润率', type: 'line', data: om, smooth: false, symbol: 'circle', symbolSize: isMobile ? 5 : 7, lineStyle: { width: 2 } },
        { name: '净利率', type: 'line', data: nm, smooth: false, symbol: 'circle', symbolSize: isMobile ? 5 : 7, lineStyle: { width: 2 } }
      ]
    };
    render(el, option);
  }

  // 4. chart-cashflow: 现金流结构（近4季度分组柱状）
  function initCashflow() {
    var el = document.getElementById('chart-cashflow');
    if (!el) return;
    var quarters = ['FY26Q1', 'FY26Q2', 'FY26Q3', 'FY26Q4'];
    var ocf = [12, 18, 35, 75];
    var capex = [8, 9, 10, 12];
    var fcf = [4, 9, 25, 63];
    var option = {
      animation: false,
      color: [palette.series2, palette.series4, palette.series1],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: {
        type: 'category', data: quarters,
        axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0, interval: 0 }),
        axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false }
      },
      yAxis: { type: 'value', name: '亿美元', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '经营现金流', type: 'bar', data: ocf, barMaxWidth: isMobile ? 14 : 24, itemStyle: { borderRadius: [3, 3, 0, 0] } },
        { name: '资本支出', type: 'bar', data: capex, barMaxWidth: isMobile ? 14 : 24, itemStyle: { borderRadius: [3, 3, 0, 0] } },
        { name: '自由现金流', type: 'bar', data: fcf, barMaxWidth: isMobile ? 14 : 24, itemStyle: { borderRadius: [3, 3, 0, 0] } }
      ]
    };
    render(el, option);
  }

  // 5. chart-kpi-trend: 营收柱状+毛利率折线（双Y轴）
  function initKpiTrend() {
    var el = document.getElementById('chart-kpi-trend');
    if (!el) return;
    var quarters = ['FY25Q1', 'FY25Q2', 'FY25Q3', 'FY25Q4', 'FY26Q1', 'FY26Q2', 'FY26Q3', 'FY26Q4'];
    var revenue = [15.2, 16.8, 17.5, 19.01, 23.15, 30.25, 59.4, 89.7];
    var gm = [12, 18, 22, 28, 35, 48, 68, 84.6];
    var option = {
      animation: false,
      color: [palette.series1, palette.series5],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: {
        type: 'category', data: quarters,
        axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0, interval: 0 }),
        axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false }
      },
      yAxis: [
        { type: 'value', name: '营收(亿美元)', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: palette.grid } } },
        { type: 'value', name: '毛利率(%)', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, axisLabel: Object.assign({}, axisLabel(), { formatter: '{value}%' }), splitLine: { show: false } }
      ],
      series: [
        { name: '营收', type: 'bar', yAxisIndex: 0, data: revenue, barMaxWidth: isMobile ? 18 : 30, itemStyle: { color: palette.series1, borderRadius: [3, 3, 0, 0] } },
        { name: '毛利率', type: 'line', yAxisIndex: 1, data: gm, smooth: false, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: palette.series5 }, itemStyle: { color: palette.series5 } }
      ]
    };
    render(el, option);
  }

  // 6. chart-geo: 地区分布（饼图）
  function initGeo() {
    var el = document.getElementById('chart-geo');
    if (!el) return;
    var data = [
      { name: '美国', value: 40.4 },
      { name: '中国', value: 22.4 },
      { name: '韩国/日本', value: 13.5 },
      { name: '其他亚太', value: 8.9 },
      { name: '欧洲', value: 4.5 }
    ];
    var pieColors = [palette.series1, palette.series5, palette.series3, palette.series4, palette.neutral];
    var legendConf = isMobile
      ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: palette.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var option = {
      animation: false, color: pieColors, legend: legendConf,
      tooltip: { trigger: 'item', formatter: '{b}: {c}亿美元 ({d}%)' },
      series: [{
        type: 'pie', radius: isMobile ? ['38%', '62%'] : ['52%', '72%'], center: isMobile ? ['50%', '42%'] : ['38%', '50%'],
        avoidLabelOverlap: true, itemStyle: { borderColor: palette.surface, borderWidth: 2 },
        label: { show: !isMobile, color: palette.text, fontSize: fs(12), formatter: '{d}%' },
        labelLine: { show: !isMobile }, data: data
      }]
    };
    render(el, option);
  }

  // 7. chart-radar: 综合财务指标雷达图
  function initRadar() {
    var el = document.getElementById('chart-radar');
    if (!el) return;
    var option = {
      animation: false,
      color: [palette.series1, palette.neutral],
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: {},
      radar: {
        indicator: [
          { name: '营收增长', max: 100 },
          { name: '盈利能力', max: 100 },
          { name: '现金流', max: 100 },
          { name: '资产负债', max: 100 },
          { name: '股东回报', max: 100 },
          { name: '需求景气', max: 100 }
        ],
        radius: isMobile ? '58%' : '68%',
        axisName: { color: palette.textMuted, fontSize: fs(12) },
        splitLine: { lineStyle: { color: palette.grid } },
        splitArea: { areaStyle: { color: [palette.surface, 'rgba(0,113,227,0.03)'] } },
        axisLine: { lineStyle: { color: palette.grid } }
      },
      series: [{
        type: 'radar',
        data: [
          { name: '本季度', value: [95, 98, 92, 85, 90, 95], areaStyle: { color: 'rgba(0,113,227,0.2)' }, lineStyle: { width: 2 } },
          { name: '行业均值', value: [60, 50, 55, 65, 50, 60], areaStyle: { color: 'rgba(110,110,115,0.1)' }, lineStyle: { width: 2, type: 'dashed' } }
        ]
      }]
    };
    render(el, option);
  }

  function initAll() {
    initRevenueTrend();
    initRevenueMix();
    initMarginTrend();
    initCashflow();
    initKpiTrend();
    initGeo();
    initRadar();
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
