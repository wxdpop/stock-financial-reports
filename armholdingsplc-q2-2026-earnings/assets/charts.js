/**
 * Arm Holdings Q2 2026 财报图表 (SVG 渲染 / 无动画 / 响应式)
 * 7 个固定图表：chart-revenue-trend / chart-revenue-mix / chart-margin-trend
 *               chart-cashflow / chart-kpi-trend / chart-geo / chart-radar
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
    primary:    cssVar('--accent', '#0071e3'),
    accent:     cssVar('--accent2', '#34c759'),
    positive:   cssVar('--accent2', '#34c759'),
    negative:   cssVar('--neg', '#d93025'),
    neutral:    cssVar('--muted', '#6e6e73'),
    text:       cssVar('--ink', '#1d1d1f'),
    textMuted:  cssVar('--muted', '#6e6e73'),
    grid:       cssVar('--rule', '#d2d2d7'),
    surface:    '#ffffff',
    series1:    '#0071e3',
    series2:    '#34c759',
    series3:    '#af52de',
    series4:    '#ff9f0a',
    series5:    '#ff375f'
  };

  var isMobile = window.innerWidth <= 700;

  function fs(base) { return isMobile ? Math.round(base * 0.86) : base; }

  function niceRange(values) {
    var min = Infinity, max = -Infinity, i, v;
    for (i = 0; i < values.length; i++) {
      v = values[i];
      if (v == null || typeof v !== 'number' || isNaN(v)) continue;
      if (v < min) min = v;
      if (v > max) max = v;
    }
    if (min === Infinity) { min = 0; max = 1; }
    if (min === max) { min = min - 1; max = max + 1; }
    var pad = (max - min) * 0.1;
    return { min: +(min - pad).toFixed(2), max: +(max + pad).toFixed(2) };
  }

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

  /* 1. chart-revenue-trend: 营收与净利润趋势（柱+折线，双Y轴） */
  function initRevenueTrend() {
    var el = document.getElementById('chart-revenue-trend');
    if (!el) return;
    var quarters = ['24Q4', '25Q1', '25Q2', '25Q3', '25Q4', '26Q1', '26Q2'];
    var revenue = [9.83, 12.41, 10.53, 11.35, 12.42, 14.90, 12.89];
    var netIncome = [2.52, 2.10, 1.30, 2.38, 2.23, 3.13, 2.70];
    var revRange = niceRange(revenue);
    var niRange = niceRange(netIncome);
    var option = {
      animation: false,
      color: [palette.series1, palette.series2],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: {
        type: 'category', data: quarters,
        axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 30 : 0, interval: 0 }),
        axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false }
      },
      yAxis: [
        { type: 'value', name: '营收(亿美元)', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: revRange.min, max: revRange.max, axisLabel: axisLabel(), splitLine: { lineStyle: { color: palette.grid } } },
        { type: 'value', name: '净利润(亿美元)', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: niRange.min, max: niRange.max, axisLabel: axisLabel(), splitLine: { show: false } }
      ],
      series: [
        { name: '营业收入', type: 'bar', yAxisIndex: 0, data: revenue, barMaxWidth: isMobile ? 18 : 32, itemStyle: { color: palette.series1, borderRadius: [3,3,0,0] } },
        { name: '净利润', type: 'line', yAxisIndex: 1, data: netIncome, smooth: false, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: palette.series2 }, itemStyle: { color: palette.series2 } }
      ]
    };
    render(el, option);
  }

  /* 2. chart-revenue-mix: 营收构成（环形饼图） */
  function initRevenueMix() {
    var el = document.getElementById('chart-revenue-mix');
    if (!el) return;
    var data = [
      { name: '特许权收入', value: 715 },
      { name: '授权和其他收入', value: 574 }
    ];
    var pieColors = [palette.series1, palette.series2];
    var legendConf = isMobile
      ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: palette.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var option = {
      animation: false,
      color: pieColors,
      legend: legendConf,
      tooltip: { trigger: 'item', formatter: '{b}: {c} 百万美元 ({d}%)' },
      series: [{
        type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true, itemStyle: { borderColor: palette.surface, borderWidth: 2 },
        label: { show: !isMobile, color: palette.text, fontSize: fs(12), formatter: '{d}%' },
        labelLine: { show: !isMobile }, data: data
      }]
    };
    render(el, option);
  }

  /* 3. chart-margin-trend: 利润率趋势（折线图） */
  function initMarginTrend() {
    var el = document.getElementById('chart-margin-trend');
    if (!el) return;
    var quarters = ['24Q4', '25Q1', '25Q2', '25Q3', '25Q4', '26Q1', '26Q2'];
    var grossMargin = [94.8, 95.8, 94.3, 97.4, 94.2, 93.1, 98.1];
    var netMargin = [25.6, 16.9, 12.3, 21.0, 18.0, 21.0, 20.9];
    var option = {
      animation: false,
      color: [palette.series1, palette.series2],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', formatter: function(p){ return p[0].axisValue + '<br/>' + p.map(function(x){return x.marker+' '+x.seriesName+': '+x.value+'%';}).join('<br/>'); } },
      xAxis: {
        type: 'category', data: quarters,
        axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 30 : 0, interval: 0 }),
        axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false }
      },
      yAxis: { type: 'value', name: '百分比(%)', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: 0, max: 100, axisLabel: axisLabel(), splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '毛利率', type: 'line', data: grossMargin, smooth: false, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2 }, itemStyle: { color: palette.series1 } },
        { name: '净利率', type: 'line', data: netMargin, smooth: false, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2 }, itemStyle: { color: palette.series2 } }
      ]
    };
    render(el, option);
  }

  /* 4. chart-cashflow: 现金流结构（分组柱状图） */
  function initCashflow() {
    var el = document.getElementById('chart-cashflow');
    if (!el) return;
    var quarters = ['25Q2', '25Q3', '25Q4', '26Q1', '26Q2'];
    var ocf = [332, 567, 365, 260, 902];
    var capex = [161, 138, 184, 90, 237];
    var fcf = [171, 429, 181, 170, 665];
    var allVals = ocf.concat(capex).concat(fcf);
    var range = niceRange(allVals);
    var option = {
      animation: false,
      color: [palette.series1, palette.series4, palette.series2],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: {
        type: 'category', data: quarters,
        axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 30 : 0, interval: 0 }),
        axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false }
      },
      yAxis: { type: 'value', name: '百万美元', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: range.min, max: range.max, axisLabel: axisLabel(), splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '经营现金流', type: 'bar', data: ocf, barMaxWidth: isMobile ? 12 : 22, itemStyle: { color: palette.series1, borderRadius: [3,3,0,0] } },
        { name: '资本支出', type: 'bar', data: capex, barMaxWidth: isMobile ? 12 : 22, itemStyle: { color: palette.series4, borderRadius: [3,3,0,0] } },
        { name: '自由现金流', type: 'bar', data: fcf, barMaxWidth: isMobile ? 12 : 22, itemStyle: { color: palette.series2, borderRadius: [3,3,0,0] } }
      ]
    };
    render(el, option);
  }

  /* 5. chart-kpi-trend: 关键运营指标趋势（柱+折线，双Y轴） */
  function initKpiTrend() {
    var el = document.getElementById('chart-kpi-trend');
    if (!el) return;
    var quarters = ['25Q2', '25Q3', '25Q4', '26Q1', '26Q2'];
    var royalty = [588, 605, 632, 680, 715];
    var royaltyGrowth = [18, 20, 21, 22, 22];
    var revRange = niceRange(royalty);
    var growRange = niceRange(royaltyGrowth);
    var option = {
      animation: false,
      color: [palette.series1, palette.accent],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: {
        type: 'category', data: quarters,
        axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 30 : 0, interval: 0 }),
        axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false }
      },
      yAxis: [
        { type: 'value', name: '特许权收入(百万美元)', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: revRange.min, max: revRange.max, axisLabel: axisLabel(), splitLine: { lineStyle: { color: palette.grid } } },
        { type: 'value', name: '同比增速(%)', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: growRange.min, max: growRange.max, axisLabel: Object.assign({}, axisLabel(), { formatter: '{value}%' }), splitLine: { show: false } }
      ],
      series: [
        { name: '特许权收入', type: 'bar', yAxisIndex: 0, data: royalty, barMaxWidth: isMobile ? 16 : 28, itemStyle: { color: palette.series1, borderRadius: [3,3,0,0] } },
        { name: '同比增速', type: 'line', yAxisIndex: 1, data: royaltyGrowth, smooth: false, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: palette.accent }, itemStyle: { color: palette.accent } }
      ]
    };
    render(el, option);
  }

  /* 6. chart-geo: 地区营收分布（环形饼图） */
  function initGeo() {
    var el = document.getElementById('chart-geo');
    if (!el) return;
    var data = [
      { name: '亚太地区(含中国)', value: 52 },
      { name: '北美地区', value: 28 },
      { name: '欧洲地区', value: 14 },
      { name: '其他地区', value: 6 }
    ];
    var pieColors = [palette.series1, palette.series2, palette.series3, palette.series4];
    var legendConf = isMobile
      ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: palette.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var option = {
      animation: false,
      color: pieColors,
      legend: legendConf,
      tooltip: { trigger: 'item', formatter: '{b}: {d}%' },
      series: [{
        type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true, itemStyle: { borderColor: palette.surface, borderWidth: 2 },
        label: { show: !isMobile, color: palette.text, fontSize: fs(12), formatter: '{d}%' },
        labelLine: { show: !isMobile }, data: data
      }]
    };
    render(el, option);
  }

  /* 7. chart-radar: 综合财务雷达图 */
  function initRadar() {
    var el = document.getElementById('chart-radar');
    if (!el) return;
    var option = {
      animation: false,
      color: [palette.series1, palette.series4],
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: {},
      radar: {
        indicator: [
          { name: '营收增长', max: 100 },
          { name: '盈利能力', max: 100 },
          { name: '现金流', max: 100 },
          { name: '市场地位', max: 100 },
          { name: '估值吸引力', max: 100 },
          { name: '研发投入', max: 100 }
        ],
        shape: 'polygon',
        splitNumber: 5,
        axisName: { color: palette.textMuted, fontSize: fs(11) },
        splitLine: { lineStyle: { color: palette.grid } },
        splitArea: { areaStyle: { color: ['rgba(0,0,0,0.02)', 'rgba(0,0,0,0.04)'] } },
        axisLine: { lineStyle: { color: palette.grid } }
      },
      series: [{
        type: 'radar',
        data: [
          { value: [85, 92, 95, 90, 35, 80], name: 'Arm 本季表现', areaStyle: { color: 'rgba(0,113,227,0.15)' }, lineStyle: { width: 2, color: palette.series1 }, itemStyle: { color: palette.series1 } },
          { value: [70, 75, 70, 65, 60, 65], name: '行业平均水平', areaStyle: { color: 'rgba(255,159,10,0.10)' }, lineStyle: { width: 2, color: palette.series4 }, itemStyle: { color: palette.series4 } }
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
