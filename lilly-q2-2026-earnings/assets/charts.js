/**
 * Eli Lilly and Co Q2 2026 ECharts 图表 (SVG 渲染 / 无动画 / 响应式)
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
    accent:     cssVar('--accent', '#0071e3'),
    positive:   cssVar('--accent2', '#34c759'),
    negative:   cssVar('--neg', '#d93025'),
    neutral:    cssVar('--muted', '#6e6e73'),
    text:       cssVar('--ink', '#1d1d1f'),
    textMuted:  cssVar('--muted', '#6e6e73'),
    grid:       cssVar('--rule', '#d2d2d7'),
    surface:    cssVar('--bg2', '#ffffff'),
    series1:    '#0071e3',
    series2:    '#34c759',
    series3:    '#8b5cf6',
    series4:    '#f59e0b',
    series5:    '#ff6b35',
    series6:    '#10b981',
    series7:    '#ef4444'
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

  function axisLabel() {
    return { color: palette.textMuted, fontSize: fs(12) };
  }

  function makeChart(el) {
    return echarts.init(el, null, { renderer: 'svg' });
  }

  function render(el, option) {
    if (!el) return null;
    var chart = makeChart(el);
    chart.setOption(option);
    window.addEventListener('resize', function () { chart.resize(); });
    return chart;
  }

  /* 1. chart-revenue-trend */
  function initRevenueTrend() {
    var el = document.getElementById('chart-revenue-trend');
    if (!el) return;
    var categories = ['FY24Q4','FY25Q1','FY25Q2','FY25Q3','FY25Q4','FY26Q1','FY26Q2','FY26Q3E'];
    var revenue = [121.0, 135.2, 138.0, 155.0, 158.0, 172.0, 198.0, 229.7];
    var netIncome = [26.0, 30.5, 28.2, 56.7, 33.5, 45.0, 74.0, 71.0];
    var revRange = niceRange(revenue);
    var niRange = niceRange(netIncome);
    var option = {
      animation: false, color: [palette.series1, palette.series2],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: { type: 'category', data: categories, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0, interval: 0 }), axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false } },
      yAxis: [
        { type: 'value', name: '营收 (亿美元)', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: revRange.min, max: revRange.max, axisLabel: axisLabel(), splitLine: { lineStyle: { color: palette.grid } } },
        { type: 'value', name: '净利润 (亿美元)', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: niRange.min, max: niRange.max, axisLabel: axisLabel(), splitLine: { show: false } }
      ],
      series: [
        { name: '营收', type: 'bar', yAxisIndex: 0, data: revenue, barMaxWidth: isMobile ? 18 : 30, itemStyle: { color: palette.series1, borderRadius: [3, 3, 0, 0] } },
        { name: '净利润', type: 'line', yAxisIndex: 1, data: netIncome, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 3, color: palette.series2 }, itemStyle: { color: palette.series2 } }
      ]
    };
    render(el, option);
  }

  /* 2. chart-revenue-mix */
  function initRevenueMix() {
    var el = document.getElementById('chart-revenue-mix');
    if (!el) return;
    var data = [
      { name: 'Mounjaro', value: 99.4 },
      { name: 'Zepbound', value: 49.3 },
      { name: '其他药品', value: 68.0 },
      { name: '合作与特许权', value: 12.0 },
      { name: 'Foundayo', value: 0.98 }
    ];
    var pieColors = [palette.series1, palette.series2, palette.series3, palette.series4, palette.series5];
    var legendConf = isMobile
      ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: palette.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var option = {
      animation: false, color: pieColors, legend: legendConf,
      tooltip: { trigger: 'item', formatter: '{b}: ${c}亿 ({d}%)' },
      series: [{ type: 'pie', radius: isMobile ? ['38%', '62%'] : ['48%', '70%'], center: isMobile ? ['50%', '42%'] : ['40%', '50%'], avoidLabelOverlap: true, itemStyle: { borderColor: palette.surface, borderWidth: 2 }, label: { show: !isMobile, color: palette.text, fontSize: fs(12), formatter: '{b}\n{d}%' }, labelLine: { show: !isMobile }, data: data }]
    };
    render(el, option);
  }

  /* 3. chart-margin-trend */
  function initMarginTrend() {
    var el = document.getElementById('chart-margin-trend');
    if (!el) return;
    var categories = ['FY24Q4','FY25Q1','FY25Q2','FY25Q3','FY25Q4','FY26Q1','FY26Q2','FY26Q3E'];
    var grossMargin = [80.0, 81.0, 81.5, 82.0, 82.5, 83.5, 84.3, 85.8];
    var opMargin = [36.0, 38.0, 39.0, 40.0, 42.0, 45.0, 49.4, 54.2];
    var netMargin = [21.0, 22.0, 22.5, 23.0, 24.0, 25.0, 37.4, 30.9];
    var range = niceRange(grossMargin.concat(opMargin).concat(netMargin));
    var option = {
      animation: false, color: [palette.series1, palette.series3, palette.series2],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', valueFormatter: function(v) { return v + '%'; } },
      xAxis: { type: 'category', data: categories, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0, interval: 0 }), axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '%', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: range.min, max: range.max, axisLabel: Object.assign({}, axisLabel(), { formatter: '{value}%' }), splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '毛利率', type: 'line', data: grossMargin, smooth: true, symbol: 'circle', symbolSize: fs(7), lineStyle: { width: 2.5 } },
        { name: '营业利润率', type: 'line', data: opMargin, smooth: true, symbol: 'diamond', symbolSize: fs(7), lineStyle: { width: 2.5 } },
        { name: '净利率', type: 'line', data: netMargin, smooth: true, symbol: 'triangle', symbolSize: fs(7), lineStyle: { width: 2.5 } }
      ]
    };
    render(el, option);
  }

  /* 4. chart-cashflow */
  function initCashflow() {
    var el = document.getElementById('chart-cashflow');
    if (!el) return;
    var categories = ['FY25Q3','FY25Q4','FY26Q1','FY26Q2'];
    var operating = [40.0, 55.0, 53.3, 106.9];
    var investing = [-25.0, -30.0, -40.0, -55.0];
    var financing = [-15.0, -20.0, -25.0, 30.0];
    var allVals = operating.concat(investing).concat(financing);
    var range = niceRange(allVals);
    var option = {
      animation: false, color: [palette.series1, palette.series6, palette.series4],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: { type: 'category', data: categories, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 35 : 0, interval: 0 }), axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '亿美元', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: range.min, max: range.max, axisLabel: axisLabel(), splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '经营现金流', type: 'bar', data: operating, barMaxWidth: isMobile ? 14 : 26, itemStyle: { color: palette.series2, borderRadius: [3, 3, 0, 0] } },
        { name: '投资现金流', type: 'bar', data: investing, barMaxWidth: isMobile ? 14 : 26, itemStyle: { color: palette.series6, borderRadius: [3, 3, 0, 0] } },
        { name: '融资现金流', type: 'bar', data: financing, barMaxWidth: isMobile ? 14 : 26, itemStyle: { color: palette.series4, borderRadius: [3, 3, 0, 0] } }
      ]
    };
    render(el, option);
  }

  /* 5. chart-kpi-trend */
  function initKpiTrend() {
    var el = document.getElementById('chart-kpi-trend');
    if (!el) return;
    var categories = ['FY24Q4','FY25Q1','FY25Q2','FY25Q3','FY25Q4','FY26Q1','FY26Q2','FY26Q3E'];
    var mounjaro = [30.0, 40.0, 52.0, 65.0, 75.0, 86.0, 99.4, 105.0];
    var zepbound = [22.0, 28.0, 33.8, 35.0, 38.0, 42.2, 49.3, 55.0];
    var allVals = mounjaro.concat(zepbound);
    var range = niceRange(allVals);
    var option = {
      animation: false, color: [palette.series1, palette.series3],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: { type: 'category', data: categories, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0, interval: 0 }), axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '亿美元', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: range.min, max: range.max, axisLabel: axisLabel(), splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: 'Mounjaro', type: 'bar', data: mounjaro, barMaxWidth: isMobile ? 16 : 28, itemStyle: { color: palette.series1, borderRadius: [3, 3, 0, 0] } },
        { name: 'Zepbound', type: 'bar', data: zepbound, barMaxWidth: isMobile ? 16 : 28, itemStyle: { color: palette.series3, borderRadius: [3, 3, 0, 0] } }
      ]
    };
    render(el, option);
  }

  /* 6. chart-geo */
  function initGeo() {
    var el = document.getElementById('chart-geo');
    if (!el) return;
    var data = [
      { name: '美国', value: 143.7 },
      { name: '海外(美国以外)', value: 86.0 }
    ];
    var pieColors = [palette.series1, palette.series3];
    var legendConf = isMobile
      ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: palette.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var option = {
      animation: false, color: pieColors, legend: legendConf,
      tooltip: { trigger: 'item', formatter: '{b}: ${c}亿 ({d}%)' },
      series: [{ type: 'pie', radius: isMobile ? ['38%', '62%'] : ['48%', '70%'], center: isMobile ? ['50%', '42%'] : ['40%', '50%'], avoidLabelOverlap: true, itemStyle: { borderColor: palette.surface, borderWidth: 2 }, label: { show: !isMobile, color: palette.text, fontSize: fs(12), formatter: '{b}\n{d}%' }, labelLine: { show: !isMobile }, data: data }]
    };
    render(el, option);
  }

  /* 7. chart-radar */
  function initRadar() {
    var el = document.getElementById('chart-radar');
    if (!el) return;
    var indicators = [
      { name: '营收规模', max: 250 },
      { name: '毛利率', max: 100 },
      { name: '净利率', max: 50 },
      { name: '营收增速', max: 60 },
      { name: 'ROE', max: 100 },
      { name: '现金流', max: 120 }
    ];
    var option = {
      animation: false, color: [palette.series1, palette.series3],
      legend: { top: 0, data: ['本季度', '行业平均'], textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: {},
      radar: { center: ['50%', '55%'], radius: isMobile ? '55%' : '65%', indicator: indicators, axisName: { color: palette.textMuted, fontSize: fs(11) }, splitArea: { areaStyle: { color: ['rgba(0,113,227,0.02)', 'rgba(0,113,227,0.02)'] } }, splitLine: { lineStyle: { color: palette.grid } }, axisLine: { lineStyle: { color: palette.grid } } },
      series: [{ type: 'radar', data: [
        { name: '本季度', value: [229.7, 85.8, 30.9, 48.0, 78.8, 106.9], areaStyle: { color: 'rgba(0,113,227,0.15)' }, lineStyle: { width: 2.5 } },
        { name: '行业平均', value: [60, 45, 18, 8, 30, 30], areaStyle: { color: 'rgba(139,92,246,0.08)' }, lineStyle: { width: 2, type: 'dashed' } }
      ] }]
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
