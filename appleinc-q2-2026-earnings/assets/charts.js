/**
 * Apple Q2 2026 ECharts 图表 (SVG 渲染 / 无动画 / 响应式)
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
    var categories = ['FY24Q4','FY25Q1','FY25Q2','FY25Q3','FY25Q4','FY26Q1','FY26Q2','FY26Q3'];
    var revenue = [857.8, 1243.0, 953.6, 940.4, 1024.7, 1437.6, 1111.8, 1094.2];
    var netIncome = [210.0, 363.3, 247.8, 234.3, 274.7, 421.0, 295.8, 297.9];
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
      { name: 'iPhone', value: 542.5 },
      { name: '服务', value: 307.4 },
      { name: 'Mac', value: 103.5 },
      { name: '可穿戴/家居', value: 78.8 },
      { name: 'iPad', value: 61.9 }
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
    var categories = ['FY24Q4','FY25Q1','FY25Q2','FY25Q3','FY25Q4','FY26Q1','FY26Q2','FY26Q3'];
    var grossMargin = [45.2, 46.9, 47.1, 46.5, 47.2, 48.2, 49.3, 50.1];
    var opMargin = [28.0, 34.5, 31.0, 30.0, 31.6, 35.4, 32.3, 31.5];
    var netMargin = [24.5, 29.2, 26.0, 24.9, 26.8, 29.3, 26.6, 27.2];
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
    var categories = ['FY25Q4','FY26Q1','FY26Q2','FY26Q3'];
    var operating = [297.3, 539.3, 287.0, 287.0];
    var investing = [-25.9, -48.9, -61.7, -30.0];
    var financing = [-274.8, -396.6, -222.8, -200.0];
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
    var categories = ['FY24Q4','FY25Q1','FY25Q2','FY25Q3','FY25Q4','FY26Q1','FY26Q2','FY26Q3'];
    var iphone = [380.0, 697.0, 474.0, 445.0, 462.2, 691.4, 521.0, 542.5];
    var services = [220.0, 263.4, 239.0, 274.4, 249.7, 277.0, 263.4, 307.4];
    var mac = [68.0, 89.9, 90.0, 80.4, 77.4, 90.0, 89.9, 103.5];
    var ipad = [58.0, 70.2, 56.0, 65.8, 60.0, 80.9, 55.0, 61.9];
    var wearables = [70.0, 119.5, 74.0, 74.1, 76.0, 117.5, 80.0, 78.8];
    var allVals = iphone.concat(services).concat(mac).concat(ipad).concat(wearables);
    var range = niceRange(allVals);
    var option = {
      animation: false, color: [palette.series1, palette.series2, palette.series3, palette.series4, palette.series5],
      grid: makeGrid(),
      legend: { top: 0, textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis' },
      xAxis: { type: 'category', data: categories, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0, interval: 0 }), axisLine: { lineStyle: { color: palette.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '亿美元', nameTextStyle: { color: palette.textMuted, fontSize: fs(11) }, min: range.min, max: range.max, axisLabel: axisLabel(), splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: 'iPhone', type: 'line', data: iphone, smooth: true, symbol: 'circle', symbolSize: fs(6), lineStyle: { width: 2.5 } },
        { name: '服务', type: 'line', data: services, smooth: true, symbol: 'circle', symbolSize: fs(6), lineStyle: { width: 2.5 } },
        { name: 'Mac', type: 'line', data: mac, smooth: true, symbol: 'diamond', symbolSize: fs(6), lineStyle: { width: 2 } },
        { name: 'iPad', type: 'line', data: ipad, smooth: true, symbol: 'triangle', symbolSize: fs(6), lineStyle: { width: 2 } },
        { name: '可穿戴', type: 'line', data: wearables, smooth: true, symbol: 'rect', symbolSize: fs(6), lineStyle: { width: 2, type: 'dashed' } }
      ]
    };
    render(el, option);
  }

  /* 6. chart-geo */
  function initGeo() {
    var el = document.getElementById('chart-geo');
    if (!el) return;
    var data = [
      { name: '美洲', value: 457.8 },
      { name: '欧洲', value: 294.0 },
      { name: '大中华区', value: 188.2 },
      { name: '亚太其他', value: 88.7 },
      { name: '日本', value: 65.5 }
    ];
    var pieColors = [palette.series1, palette.series3, palette.series7, palette.series4, palette.series6];
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
      { name: '营收规模', max: 1500 },
      { name: '毛利率', max: 55 },
      { name: '净利率', max: 35 },
      { name: '营收增速', max: 25 },
      { name: 'ROE', max: 150 },
      { name: '现金流', max: 600 }
    ];
    var option = {
      animation: false, color: [palette.series1, palette.series3],
      legend: { top: 0, data: ['本季度', '行业平均'], textStyle: { color: palette.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: {},
      radar: { center: ['50%', '55%'], radius: isMobile ? '55%' : '65%', indicator: indicators, axisName: { color: palette.textMuted, fontSize: fs(11) }, splitArea: { areaStyle: { color: ['rgba(0,113,227,0.02)', 'rgba(0,113,227,0.02)'] } }, splitLine: { lineStyle: { color: palette.grid } }, axisLine: { lineStyle: { color: palette.grid } } },
      series: [{ type: 'radar', data: [
        { name: '本季度', value: [1094.2, 50.1, 27.2, 16.4, 111.9, 287.0], areaStyle: { color: 'rgba(0,113,227,0.15)' }, lineStyle: { width: 2.5 } },
        { name: '行业平均', value: [400, 42, 18, 8, 60, 100], areaStyle: { color: 'rgba(139,92,246,0.08)' }, lineStyle: { width: 2, type: 'dashed' } }
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